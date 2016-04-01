import {Component, OnInit} from 'angular2/core';
import {RouteParams} from 'angular2/router';
import {CardFormComponent} from './card-form.component'
import {CardService} from '../../foundation/services/card.service'

@Component({
    selector: 'card-detail-page',
    templateUrl: 'app/cards/components/card-detail-page.component.html',
    directives: [CardFormComponent]
})
export class CardDetailPageComponent {
    constructor(private _cardService: CardService, private _routeParams: RouteParams) { }

    ngOnInit() {
        let id = +this._routeParams.get('id');
        this._cardService.getCard(id).then(card => this.card = card);
    }
}