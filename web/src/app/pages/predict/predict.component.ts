import { AfterViewInit, Component, ElementRef, ViewChild } from '@angular/core';
import { DataService } from '../../services/data.service';
import { Prediction, PredictionModel } from '../../interfaces/predictions';
import { MessageService } from 'primeng/api';

@Component({
  selector: 'app-predict',
  templateUrl: './predict.component.html',
  styleUrls: ['./predict.component.scss']
})
export class PredictComponent implements AfterViewInit {
  imageFile: File | null = null;
  capturedImage: string | null = null;
  selectedSource: string = 'file';
  selectedModel: string = '';
  prediction!: PredictionModel;
  loading: boolean = false;
  
  WIDTH = 640;
  HEIGHT = 480;
  
  @ViewChild('video') video!: ElementRef;
  @ViewChild('canvas') canvas!: ElementRef;

  error: any;
  isCaptured: boolean = false;

  constructor(private dataService: DataService, private messageService: MessageService) {}

  ngAfterViewInit() {
    if (this.selectedSource === 'webcam') {
      this.setupDevices();
    }
  }

  async setupDevices() {
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        this.video.nativeElement.srcObject = stream;
        this.video.nativeElement.play();
        this.error = null;
      } catch (err: any) {
        this.error = "Erro ao acessar a câmera: " + err.message;
      }
    } else {
      this.error = "Dispositivo não suporta acesso a webcam.";
    }
  }

  capture() {
    this.drawImageToCanvas(this.video.nativeElement);
    this.capturedImage = this.canvas.nativeElement.toDataURL('image/png');
    this.isCaptured = true;
    this.messageService.add({ severity: 'success', summary: 'Imagem capturada.', detail: 'A imagem foi capturada com sucesso.' });
  }

  removeCurrent() {
    this.isCaptured = false;
    this.capturedImage = null;
  }

  drawImageToCanvas(image: any) {
    const context = this.canvas.nativeElement.getContext('2d');
    context.clearRect(0, 0, this.WIDTH, this.HEIGHT);
    context.drawImage(image, 0, 0, this.WIDTH, this.HEIGHT);
  }

  onFileSelected(event: any): void {
    if (event.files && event.files.length > 0) {
      this.imageFile = event.files[0];
      this.capturedImage = null;
      this.messageService.add({ severity: 'success', summary: 'Imagem selecionada.', detail: this.imageFile!.name });
    }
  }

  onSubmit(): void {
    if ((this.imageFile || this.capturedImage) && this.selectedModel) {
      this.loading = true;

      let imageData: File | string = this.imageFile || this.capturedImage as string;
      
      if (typeof imageData === 'string') {
        const byteString = atob(imageData.split(',')[1]);
        const mimeString = imageData.split(',')[0].split(':')[1].split(';')[0];
        const buffer = new ArrayBuffer(byteString.length);
        const data = new Uint8Array(buffer);
        for (let i = 0; i < byteString.length; i++) {
          data[i] = byteString.charCodeAt(i);
        }
        const blob = new Blob([buffer], { type: mimeString });
        imageData = new File([blob], "captured-image.png", { type: mimeString });
      }

      this.dataService.predictFracturesOnImage(imageData, this.selectedModel).subscribe({
        next: (data: Prediction) => {
          this.prediction = data.results;
          this.loading = false;
        },
        error: (error) => {
          this.loading = false;
          console.error(error);
        }
      });
    }
  }
}
