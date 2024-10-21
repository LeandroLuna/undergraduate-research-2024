import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HomeComponent } from './home/home.component';
import { ComponentsModule } from '../components/components.module';
import { PredictComponent } from './predict/predict.component';
import { FormsModule } from '@angular/forms';
import { SearchComponent } from './search/search.component';
import { TeamComponent } from './team/team.component';
import { ResultComponent } from './result/result.component';

@NgModule({
  declarations: [
    HomeComponent,
    PredictComponent,
    SearchComponent,
    TeamComponent,
    ResultComponent
  ],
  imports: [
    CommonModule,
    ComponentsModule, 
    FormsModule
  ]
})
export class PagesModule { }
