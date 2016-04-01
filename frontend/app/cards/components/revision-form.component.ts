import {Component, Input} from 'angular2/core';

@Component({
    selector: 'revision-form',
    templateUrl: 'app/cards/components/revision-form.component.html'
})
export class RevisionFormComponent {
    @Input() revision: [string: any];
}
