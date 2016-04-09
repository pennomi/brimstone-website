import {Component, Input} from 'angular2/core';
import {FriendlyDatePipe} from '../pipes/friendly-date.pipe';
import {CardService} from '../services/card.service';


@Component({
    selector: 'comment',
    templateUrl: 'app/cards/comment.component.html',
    styleUrls: ['app/cards/comment.component.css'],
    pipes: [FriendlyDatePipe]
})
export class CommentComponent {
    @Input() comment;

    constructor(private _cardService: CardService) { }

    ngOnInit() {
        // Fetch the comment's user
        this.user = {};
        this._cardService.getUsers().subscribe(
            data => this.user = _.find(data, ['id', this.comment.user]),
            err => this.error = "Could not retrieve user."
        );
    }
