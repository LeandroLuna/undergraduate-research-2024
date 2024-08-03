import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PanelComponent } from './panel/panel.component';
import { TabViewModule } from 'primeng/tabview';
import { DividerModule } from 'primeng/divider';
import { ImageModule } from 'primeng/image';

@NgModule({
  declarations: [
    PanelComponent
  ],
  imports: [
    CommonModule,
    TabViewModule,
    DividerModule,
    ImageModule
  ],
  exports: [
    PanelComponent
  ]
})
export class ComponentsModule { }
