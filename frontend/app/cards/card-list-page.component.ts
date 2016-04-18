import {Component, OnInit} from 'angular2/core';
import {ROUTER_DIRECTIVES} from 'angular2/router';
import {CardService} from '../services/card.service';
import {RevisionFormComponent} from './revision-form.component'
declare var _;


@Component({
    selector: 'card-list-page',
    templateUrl: 'app/cards/card-list-page.component.html',
    styleUrls: ['app/cards/card-list-page.component.css'],
    directives: [ROUTER_DIRECTIVES, RevisionFormComponent]
})
export class CardListPageComponent {
    constructor(private _cardService: CardService) { }

    private cards: any[] = [];
    private cardTypes: any[] = [];

    ngOnInit() {
        // Fetch Cards
        this._cardService.getCardList().subscribe(
            data => this.cards = data,
            err => console.error(err)
        );

        // Fetch Card Types
        this._cardService.getTypeList().subscribe(
            data => this.cardTypes = data,
            err => console.error(err)
        );
    }

    getTypeName(card) {
        return _.find(this.cardTypes, ['id', card.latest_revision.type]).name;
    }
}
