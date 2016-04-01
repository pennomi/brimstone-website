import {Component, OnInit} from 'angular2/core';
import {CardFormComponent} from './card-form.component'
import {CardService} from '../../foundation/services/card.service'

@Component({
    selector: 'card-list-page',
    templateUrl: 'app/cards/components/card-list-page.component.html',
    directives: [CardFormComponent],
    providers: []
})
export class CardListPageComponent {
    constructor(private _cardService: CardService) { }

    ngOnInit() {
        this._cardService.getCardList().then(cards => this.cards = cards);
    }

    cardSelected(card) {
        this.selectedCard = card;
    }
}