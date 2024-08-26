import { Component } from '@angular/core';
import { Predictions } from '../../interfaces/predictions';
import { DataService } from '../../services/data.service';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrl: './search.component.scss'
})

export class SearchComponent {
  searchId: number | null = null;
  prediction: Predictions | null = null;
  error: string | null = null;
  loading: boolean = false;

  constructor(private dataService: DataService) { }

  onSearch(): void {
    if (this.searchId !== null) {
      this.loading = true;
      this.prediction = null;
      this.error = null;

      this.dataService.getPredictionById(this.searchId).subscribe({
        next: (data: Predictions) => {
          this.prediction = data;
          this.loading = false;
        },
        error: (_err) => {
          this.error = `Predição de ID '${this.searchId}' não encontrada.`;
          this.loading = false;
        }
      });
    }
  }
}
