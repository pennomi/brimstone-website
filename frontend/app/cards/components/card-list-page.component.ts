import {Component, OnInit} from 'angular2/core';
import {RouteParams, ROUTER_DIRECTIVES} from 'angular2/router';
import {CardService} from '../../foundation/services/card.service';


@Component({
    selector: 'card-list-page',
    templateUrl: 'app/cards/components/card-list-page.component.html',
    directives: [ROUTER_DIRECTIVES]
})
export class CardListPageComponent {
    constructor(private _cardService: CardService) { }

    ngOnInit() {
        this._cardService.getCardList().then(cards => this.cards = cards);
    }
}