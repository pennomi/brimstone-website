import {Component, OnInit} from 'angular2/core';
import {RouteParams} from 'angular2/router';
import {RevisionFormComponent} from './revision-form.component'
import {CardService} from '../../foundation/services/card.service'

@Component({
    selector: 'card-detail-page',
    templateUrl: 'app/cards/components/card-detail-page.component.html',
    directives: [RevisionFormComponent]
})
export class CardDetailPageComponent {
    constructor(private _cardService: CardService, private _routeParams: RouteParams) { }

    ngOnInit() {
        let id = +this._routeParams.get('id');
        this._cardService.getCard(id).subscribe(
            data => this.card = data,
            err => console.error(err)
        );
    }
}