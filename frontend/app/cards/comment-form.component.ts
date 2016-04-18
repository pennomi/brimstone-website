import {Component, Input} from 'angular2/core';
import {CardService} from '../services/card.service'
import {CardTypeFieldComponent} from './card-type-field.component'
import {CardStatFieldComponent} from './card-stat-field.component'

@Component({
    selector: 'comment-form',
    template: `
        <textarea [(ngModel)]="commentText" placeholder="Comment"></textarea>
        <button (click)="submitClicked()">Submit</button>
    `,
    directives: [CardTypeFieldComponent, CardStatFieldComponent]
})
export class CommentFormComponent {
    constructor(private _cardService: CardService) { }

    commentText: string;
    @Input() card;

    submitClicked() {
        this._cardService.createComment(this.card.id, this.commentText).subscribe(
            // TODO: Show these to the user.
            // TODO: Emit a signal that passes the new revision to the parent
            data => console.log("Saved"),
            err => console.error(err)
        );
    }
}
