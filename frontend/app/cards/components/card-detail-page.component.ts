import {Component, OnInit} from 'angular2/core';
import {RouteParams} from 'angular2/router';
import {RevisionFormComponent} from './revision-form.component'
import {CardService} from '../../foundation/services/card.service'


let processRevision = (r) => {
    // TODO: Consider moving this to the service
    r.created_at_date = new Date(r.created_at);
    r.approved_at_date = new Date(r.approved_at);
    r.rejected_at_date = new Date(r.rejected_at);
};


@Component({
    selector: 'card-detail-page',
    templateUrl: 'app/cards/components/card-detail-page.component.html',
    directives: [RevisionFormComponent]
})
export class CardDetailPageComponent {
    constructor(private _cardService: CardService, private _routeParams: RouteParams) { }

    editMode: bool = false

    ngOnInit() {
        // Fetch the card
        this.card = {latest_revision: {}};
        let id = +this._routeParams.get('id');
        this._cardService.getCard(id).subscribe(
            data => {
                // Save the response data
                this.card = data;
                processRevision(this.card.latest_revision);

                // Generate a new revision that copies data from the latest
                this.blankRevision = JSON.parse(JSON.stringify(this.card.latest_revision))
                this.blankRevision.id = undefined;
            },
            err => this.error = "Could not retrieve card."
        );

        // Fetch all revisions of this card
        this.revisions = [];
        this._cardService.getRevisionsForCard(id).subscribe(
            data => {
                this.revisions = data;
                for (let r of this.revisions) {
                    processRevision(r);
                }
            },
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