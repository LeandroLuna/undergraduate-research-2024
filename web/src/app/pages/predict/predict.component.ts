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

  constructor(private dataService: DataService){}

  onFileSelected(event: any): void {
    if (event.files && event.files.length > 0) {
      this.imageFile = event.files[0];
    }
  }

  onSubmit(): void {
    if (this.imageFile && this.selectedModel) {
      this.dataService.predictFracturesOnImage(this.imageFile, this.selectedModel).subscribe({
        next: (data: Prediction) => {
          this.prediction = data.results;
        },
        error: (error) => {
          console.error(error)
        }
      })
    }
  }
}