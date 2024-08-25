import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PanelComponent } from './panel/panel.component';
import { TabViewModule } from 'primeng/tabview';
import { DividerModule } from 'primeng/divider';
import { ImageModule } from 'primeng/image';
import { FileUploadModule } from 'primeng/fileupload';
import { RadioButtonModule } from 'primeng/radiobutton';
import { ProgressSpinnerModule } from 'primeng/progressspinner';
import { PaginatorModule } from 'primeng/paginator';
import { ToastModule } from 'primeng/toast';

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
    PanelComponent,
    ImageModule,
    FileUploadModule,
    RadioButtonModule,
    ProgressSpinnerModule,
    PaginatorModule,
    ToastModule
  ]
})
export class ComponentsModule { }
