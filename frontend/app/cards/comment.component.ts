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
  constructor(private _cardService: CardService) { }

  @Input() comment;
  private user: any = {};
  private error: string = "";

  ngOnInit() {
    // Fetch the comment's user
    this._cardService.getUsers().subscribe(
      data => this.user = _.find(data, ['id', this.comment.user]),
      err => this.error = "Could not retrieve user."
    );
  }
}
