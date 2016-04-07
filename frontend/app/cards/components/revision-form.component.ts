import {Component, Input} from 'angular2/core';
import {CardService} from '../../foundation/services/card.service'
import {CardTypeFieldComponent} from './card-type-field.component'
import {CardStatFieldComponent} from './card-stat-field.component'

@Component({
    selector: 'revision-form',
    templateUrl: 'app/cards/components/revision-form.component.html',
    directives: [CardTypeFieldComponent, CardStatFieldComponent]
})
export class RevisionFormComponent {
    constructor(private _cardService: CardService) { }

    @Input() revision: [string: any];
    ngOnInit() {
        if (!this.revision) {
            this.revision = {stats: []};
        }
    }

    modifyStats(newStats) {
        this.revision.stats = newStats;
    }

    submitClicked() {
        this._cardService.saveRevision(this.revision).subscribe(
            // TODO: Show these to the user.
            // TODO: Emit a signal that passes the new revision to the parent
            data => console.log("Saved"),
            err => console.error(err)
        );
    }
}
