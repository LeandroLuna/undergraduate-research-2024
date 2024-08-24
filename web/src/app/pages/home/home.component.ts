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
  limit: number = 10;
  offset: number = 0; 

  constructor(private dataService: DataService) {}

  ngOnInit() {
    this.loadPredictions();
  }

  loadPredictions() {
    this.dataService.getAllPredictions(this.limit, this.offset).subscribe({
      next: (data: PredictionsList) => {
        this.predictions = data;
      },
      error: (error) => {
        console.error(error);
      }
    });
  }

  paginate(event: any) {
    this.limit = event.rows; 
    this.offset = event.first;
    this.loadPredictions();
  }
}
