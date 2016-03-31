import {Component, OnInit} from 'angular2/core';
import {CardFormComponent} from './card-form.component'
import {CardService} from '../services/card.service'

@Component({
    selector: 'card-editor',
    templateUrl: 'app/card-editor/components/card-editor.component.html',
    styleUrl: 'app/navigation/components/app.component.css',
    directives: [CardFormComponent],
    providers: [CardService]
})
export class CardEditorComponent {
    constructor(private _cardService: CardService) { }

    ngOnInit() {
        this._cardService.getCardList().then(cards => this.cards = cards);
    }

    cardSelected(card) {
        this.selectedCard = card;
    }
}