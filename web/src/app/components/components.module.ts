import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PanelComponent } from './panel/panel.component';
import { TabViewModule } from 'primeng/tabview';
import { DividerModule } from 'primeng/divider';

@NgModule({
  declarations: [
    PanelComponent
  ],
  imports: [
    CommonModule,
    TabViewModule,
    DividerModule
  ],
  exports: [
    PanelComponent
  ]
})
export class ComponentsModule { }
