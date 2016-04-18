import {Component, OnInit} from 'angular2/core';
import {RouteParams} from 'angular2/router';
import {RevisionFormComponent} from './revision-form.component';
import {CommentComponent} from './comment.component';
import {CommentFormComponent} from './comment-form.component';
import {CardService} from '../services/card.service';
import {FriendlyDatePipe} from '../pipes/friendly-date.pipe';
declare var _;


@Component({
    selector: 'card-detail-page',
    templateUrl: 'app/cards/card-detail-page.component.html',
    styleUrls: ['app/cards/card-detail-page.component.css'],
    directives: [RevisionFormComponent, CommentFormComponent, CommentComponent],
    pipes: [FriendlyDatePipe]
})
export class CardDetailPageComponent {
    constructor(private _cardService: CardService, private _routeParams: RouteParams) { }

    editMode: boolean = false;
    viewRevisionMode: boolean = false;
    public card;
    public blankRevision;
    public imagePreviewUrl: string = "";
    private error: string = "";
    private revisions: any[] = [];
    private comments: any[] = [];
    private users: any[] = [];

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
        this._cardService.getRevisionsForCard(id).subscribe(
            data => this.revisions = data,
            err => this.error = "Could not retrieve card revisions."
        );

        // Fetch all comments of this card
        this._cardService.getCommentsForCard(id).subscribe(
            data => this.comments = data,
            err => this.error = "Could not retrieve card comments."
        );

        // Fetch all users
        this._cardService.getUsers().subscribe(
            data => this.users = data,
            err => this.error = "Could not retrieve users."
        );
    }

    getUserInfo(userId) {
        if (typeof this.users == 'undefined' || this.users.length <= 0) {
            return {};
        }
        return _.find(this.users, ['id', userId]);
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

    refreshPreview() {
        this._cardService.previewRevision(this.blankRevision).subscribe(
            data => this.imagePreviewUrl = data._body,
            err => this.error = "Could not preview."
        );
    }
}
