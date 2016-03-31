import {Component, Input} from 'angular2/core';

@Component({
    selector: 'card-edit',
    templateUrl: 'app/card.edit.component.html'
})
export class CardEditComponent {
    @Input()
    card: [string: any];
}
