import {Component, Input} from 'angular2/core';
import {CardService} from '../../foundation/services/card.service'
import {CardTypeFieldComponent} from './card-type-field.component'

@Component({
    selector: 'revision-form',
    templateUrl: 'app/cards/components/revision-form.component.html',
    directives: [CardTypeFieldComponent]
})
export class RevisionFormComponent {
    constructor(private _cardService: CardService) { }

    @Input() revision: [string: any];
    ngOnInit() {
        if (!this.revision) {
            this.revision = {};
        }
    }

    submitClicked() {
        this._cardService.saveRevision(this.revision).subscribe(
            // TODO: Show these to the user.
            data => console.log("Saved"),
            err => console.error(err)
        );
    }
}
