import {Component, OnInit} from 'angular2/core';
import {CardFormComponent} from './card-form.component'
import {CardService} from '../../foundation/services/card.service'

@Component({
    selector: 'card-detail-page',
    templateUrl: 'app/cards/components/card-detail-page.component.html',
    directives: [CardFormComponent]
})
export class CardDetailPageComponent {
    constructor(private _cardService: CardService) { }

    ngOnInit() {
        this._cardService.getCardList().then(cards => this.cards = cards);
    }

    cardSelected(card) {
        this.selectedCard = card;
    }
}