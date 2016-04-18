import {Component, Input} from 'angular2/core';
import {CardService} from '../services/card.service'


@Component({
    selector: 'card-type-field',
    templateUrl: 'app/cards/card-type-field.component.html'
})
export class CardTypeFieldComponent {
    constructor(private _cardService: CardService) { }

    private type: any = {};
    private typeList: any[] = [];

    @Input() revision;
    ngOnInit() {
        this._cardService.getTypeList().subscribe(
            data => {
                this.typeList = data;
                this.type = _.find(this.typeList, ['id', this.revision.type]);
                if (!this.type) {
                    this.type = this.typeList[0];
                    this.revision.type = this.type.id;
                }
            },
            err => console.error(err)
        );
    }

    typeChanged(typeId) {
        this.type = _.find(this.typeList, ['id', +typeId]);
        this.revision.type = this.type.id;
    }
}
