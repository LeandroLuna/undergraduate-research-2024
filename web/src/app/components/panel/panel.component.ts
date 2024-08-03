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
    if (tab === 'detecção') {
      return !this.prediction.detect;
    }
    if (tab === 'segmentação') {
      return !this.prediction.segment;
    }
    return false;
  }
}
