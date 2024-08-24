import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Prediction, PredictionsList } from '../interfaces/predictions';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  private _BASE_URL = environment.baseUrl;
  
  constructor(private http: HttpClient) { }

  getAllPredictions(limit: number = 10, offset: number = 0): Observable<PredictionsList> {
    return this.http.get<PredictionsList>(`${this._BASE_URL}/v1/predictions/all`, {
      params: {
        limit: limit.toString(),
        offset: offset.toString()
      }
    });
  }

  getPredictionById(id: number): Observable<Prediction> {
    return this.http.get<Prediction>(`${this._BASE_URL}/v1/predictions/${id}`);
  }

  predictFracturesOnImage(image: File, model: string): Observable<Prediction> {
    const formData = new FormData();
    formData.append('file', image);

    return this.http.post<Prediction>(`${this._BASE_URL}/v1/${model}/predict`, formData, {
      headers: {
        'Accept': 'application/json'
      }
    });
  }
}
