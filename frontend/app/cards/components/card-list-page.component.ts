import {Component, OnInit} from 'angular2/core';
import {RouteParams, ROUTER_DIRECTIVES} from 'angular2/router';
import {CardService} from '../../foundation/services/card.service';
import {RevisionFormComponent} from './revision-form.component'


@Component({
    selector: 'card-list-page',
    templateUrl: 'app/cards/components/card-list-page.component.html',
    directives: [ROUTER_DIRECTIVES, RevisionFormComponent]
})
export class CardListPageComponent {
    constructor(private _cardService: CardService) { }

    ngOnInit() {
        this._cardService.getCardList().subscribe(
            data => this.cards = data,
            err => console.error(err)
        );
    }
}