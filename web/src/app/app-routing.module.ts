import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { PredictComponent } from './pages/predict/predict.component';
import { SearchComponent } from './pages/search/search.component';
import { TeamComponent } from './pages/team/team.component';
import { ResultComponent } from './pages/result/result.component';

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
    path: 'team',
    component: TeamComponent
  },
  {
    path: 'result',
    component: ResultComponent
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
