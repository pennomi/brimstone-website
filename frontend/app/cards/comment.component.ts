import {Component, Input} from 'angular2/core';
import {FriendlyDatePipe} from '../pipes/friendly-date.pipe'


@Component({
    selector: 'comment',
    templateUrl: 'app/cards/comment.component.html',
    styleUrls: ['app/cards/comment.component.css'],
    pipes: [FriendlyDatePipe]
})
export class CommentComponent {
    @Input() comment;
}
