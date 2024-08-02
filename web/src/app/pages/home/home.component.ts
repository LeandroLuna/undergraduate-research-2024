import { Component, OnInit } from '@angular/core';
import { DataService } from '../../services/data.service';
import { Predictions } from '../../interfaces/predictions';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent implements OnInit {
  predictions!: Predictions;

  constructor(private dataService: DataService) { }

  ngOnInit() {
    this.dataService.getAllPredictions().subscribe({
      next: (data: Predictions) => {
        this.predictions = data;
      },
      error: (error) => {
        console.error(error);
      }
    })
  }
}
