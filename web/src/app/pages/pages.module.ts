import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HomeComponent } from './home/home.component';
import { ComponentsModule } from '../components/components.module';
import { ProgressSpinnerModule } from 'primeng/progressspinner';
import { PredictComponent } from './predict/predict.component';
import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    HomeComponent,
    PredictComponent
  ],
  imports: [
    CommonModule,
    ComponentsModule, 
    ProgressSpinnerModule,
    FormsModule
  ]
})
export class PagesModule { }
