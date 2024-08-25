import { Component } from '@angular/core';

@Component({
  selector: 'app-team',
  templateUrl: './team.component.html',
  styleUrl: './team.component.scss'
})
export class TeamComponent {
  teamMembers: {name: string, linkedin: string}[] = [
    { name: 'Carlos Henrique', linkedin: 'https://www.linkedin.com/in/carlos-henrique7/' },
    { name: 'Felipe Silva', linkedin: 'https://www.linkedin.com/in/felipegabrielsilva/' },
    { name: 'Guilherme Campanha', linkedin: 'https://www.linkedin.com/in/guilhermecampanha/' },
    { name: 'Isabela Brito', linkedin: 'https://www.linkedin.com/in/isabela-brito-pessoa-3b1a061a0/' },
    { name: 'Leandro Luna', linkedin: 'https://www.linkedin.com/in/luna-leandro/' },
    { name: 'Marcos Santos', linkedin: 'https://www.linkedin.com/in/marcos-ms06/' }
  ];
}
