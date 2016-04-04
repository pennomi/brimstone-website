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
        // Fetch the card
        this.card = {latest_revision: {}};
        let id = +this._routeParams.get('id');
        this._cardService.getCard(id).subscribe(
            data => {
                // Save the response data
                this.card = data;

                // Generate a new revision that copies data from the latest
                this.blankRevision = JSON.parse(JSON.stringify(this.card.latest_revision))
                this.blankRevision.id = undefined;
            },
            err => this.error = "Could not retrieve card."
        );

        // Fetch all revisions of this card
        this.revisions = [];
        this._cardService.getRevisionsForCard(id).subscribe(
            data => this.revisions = data,
            err => this.error = "Could not retrieve card revisions."
        );
    }

    approveClicked(revision) {
        this._cardService.approveRevision(revision.id).subscribe(
            data => console.log("Approved"),
            err => this.error = "Could not approve."
        );
    }

    rejectClicked(revision) {
        this._cardService.rejectRevision(revision.id).subscribe(
            data => console.log("Rejected"),
            err => this.error = "Could not reject."
        );
    }
}