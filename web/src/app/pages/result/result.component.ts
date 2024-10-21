import { Component, Inject, OnInit, PLATFORM_ID } from '@angular/core';
import { PredictionModel } from '../../interfaces/predictions';
import { isPlatformBrowser } from '@angular/common';

@Component({
  selector: 'app-result',
  templateUrl: './result.component.html',
  styleUrl: './result.component.scss'
})
export class ResultComponent implements OnInit {
  prediction!: PredictionModel;
  
  constructor(@Inject(PLATFORM_ID) private platformId: Object) {}

  ngOnInit(): void {
    if (isPlatformBrowser(this.platformId)) {
      const storedPrediction = localStorage.getItem('lastPrediction');
      if (storedPrediction) {
        this.prediction = JSON.parse(storedPrediction);
      }
  
      window.addEventListener('storage', (event) => {
        if (event.key === 'lastPrediction' && event.newValue) {
          this.prediction = JSON.parse(event.newValue);
          console.log('New prediction:', this.prediction);
        }
      });
    }
  }
}
