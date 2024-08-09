import { Component, Input } from '@angular/core';
import { Predictions } from '../../interfaces/predictions';

@Component({
  selector: 'app-panel',
  templateUrl: './panel.component.html',
  styleUrl: './panel.component.scss'
})
export class PanelComponent {
  tabs = ["original", "detecção", "segmentação"];
  @Input() prediction!: Predictions; 

  constructor() {}

  isTabDisabled(tab: string): boolean {
    if (tab === 'detecção' && this.prediction.detect) { 
      return this.prediction.detect.id === null;
    }
    if (tab === 'segmentação' && this.prediction.segment) {
      return this.prediction.segment.id === null;
    }
    return false;
  }
}
