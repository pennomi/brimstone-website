import {Component, Input, Output, EventEmitter} from 'angular2/core';
import {CardService} from '../services/card.service'


// TODO: This fails spectacularly if the input is not an array.
@Component({
    selector: 'card-stat-field',
    templateUrl: 'app/cards/card-stat-field.component.html'
})
export class CardStatFieldComponent {
    constructor(private _cardService: CardService) { }

    private statList: any[] = [];

    @Input() stats: any;
    @Output() statsChanged: EventEmitter<any> = new EventEmitter();

    ngOnInit() {
        // Fetch the stat names and icons
        this._cardService.getStatList().subscribe(
            data => this.statList = data,
            err => console.error(err)
        );
    }

    addStatClicked() {
        // Do error validation
        if (!this.stats || !(this.stats.constructor === Array)) {
            console.log("Fixing a bad model thingy");
            this.stats = [];
        }

        // Add a new line
        this.stats.push({id:`${this.statList[0].id}`, value:""});

        // Propagate the event
        this.statsChanged.emit(this.stats);
    }

    removeStatClicked(stat) {
        let index = this.stats.indexOf(stat);
        if (index > -1) {
            this.stats.splice(index, 1);
        }
    }
}
