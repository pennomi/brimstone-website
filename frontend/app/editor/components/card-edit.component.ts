import {Component, Input} from 'angular2/core';

@Component({
    selector: 'card-edit',
    templateUrl: 'app/editor/components/card-edit.component.html'
})
export class CardEditComponent {
    @Input() card: [string: any];
}
