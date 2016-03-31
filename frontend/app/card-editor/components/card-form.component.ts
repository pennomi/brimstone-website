import {Component, Input} from 'angular2/core';

@Component({
    selector: 'card-form',
    templateUrl: 'app/card-editor/components/card-form.component.html'
})
export class CardFormComponent {
    @Input() card: [string: any];
}
