import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { PredictionsList } from '../interfaces/predictions';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  private _BASE_URL = 'http://localhost:8000/v1';

  constructor(private http: HttpClient) { }

  getAllPredictions(): Observable<PredictionsList> {
    return this.http.get<PredictionsList>(`${this._BASE_URL}/predictions/all`);
  }
}
