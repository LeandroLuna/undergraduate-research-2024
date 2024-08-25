import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { PredictComponent } from './pages/predict/predict.component';
import { SearchComponent } from './pages/search/search.component';

const routes: Routes = [
  {
    path: 'predict',
    component: PredictComponent
  },
  {
    path: 'search',
    component: SearchComponent
  },
  {
    path: '',
    component: HomeComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
