import {Component, OnInit} from 'angular2/core';
import {HomePageComponent} from './home-page.component'
import {CardEditComponent} from './card-edit.component'
import {CardService} from '../services/card.service'

@Component({
    selector: 'app',
    templateUrl: 'app/editor/components/app.component.html',
    directives: [HomePageComponent, CardEditComponent],
    providers: [CardService]
})
export class AppComponent {
    constructor(private _cardService: CardService) { }

    ngOnInit() {
        this._cardService.getCardList().then(cards => this.cards = cards);
    }

    cardSelected(card) {
        this.selectedCard = card;
    }
}