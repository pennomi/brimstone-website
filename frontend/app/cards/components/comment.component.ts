import {Component, Input} from 'angular2/core';
import {FriendlyDatePipe} from '../../foundation/pipes/friendly-date.pipe'


@Component({
    selector: 'comment',
    templateUrl: 'app/cards/components/comment.component.html',
    pipes: [FriendlyDatePipe]
})
export class CommentComponent {
    @Input() comment;
}
