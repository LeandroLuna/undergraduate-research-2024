import { Component } from '@angular/core';
import { DataService } from '../../services/data.service';
import { Prediction, PredictionModel } from '../../interfaces/predictions';

@Component({
  selector: 'app-predict',
  templateUrl: './predict.component.html',
  styleUrl: './predict.component.scss'
})
export class PredictComponent {
  imageFile: File | null = null;
  selectedModel: string = '';
  prediction!: PredictionModel;
  loading: boolean = false; 

  constructor(private dataService: DataService){}

  onFileSelected(event: any): void {
    if (event.files && event.files.length > 0) {
      this.imageFile = event.files[0];
    }
  }

  onSubmit(): void {
    if (this.imageFile && this.selectedModel) {
      this.loading = true;
      this.dataService.predictFracturesOnImage(this.imageFile, this.selectedModel).subscribe({
        next: (data: Prediction) => {
          this.prediction = data.results;
          this.loading = false;
        },
        error: (error) => {
          this.loading = false;
          console.error(error)
        }
      })
    }
  }
}