import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HomeComponent } from './home/home.component';
import { ComponentsModule } from '../components/components.module';
import { PredictComponent } from './predict/predict.component';
import { FormsModule } from '@angular/forms';
import { SearchComponent } from './search/search.component';

@NgModule({
  declarations: [
    HomeComponent,
    PredictComponent,
    SearchComponent
  ],
  imports: [
    CommonModule,
    ComponentsModule, 
    FormsModule
  ]
})
export class PagesModule { }
