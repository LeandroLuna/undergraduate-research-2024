import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { PredictionsList } from '../interfaces/predictions';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  private _BASE_URL = environment.baseUrl;

  constructor(private http: HttpClient) { 
    console.log(this._BASE_URL);
  }

  getAllPredictions(): Observable<PredictionsList> {
    return this.http.get<PredictionsList>(`${this._BASE_URL}/v1/predictions/all`);
  }
}
