import { Component, OnInit } from '@angular/core';
import { DataService } from '../../services/data.service';
import { PredictionsList } from '../../interfaces/predictions';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent implements OnInit {
  predictions!: PredictionsList;

  constructor(private dataService: DataService) { }

  ngOnInit() {
    this.dataService.getAllPredictions().subscribe({
      next: (data: PredictionsList) => {
        this.predictions = data;
        console.log(this.predictions);
      },
      error: (error) => {
        console.error(error);
      }
    })
  }
}
