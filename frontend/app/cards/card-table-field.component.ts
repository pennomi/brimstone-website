import {Component, Input, Output, EventEmitter} from 'angular2/core';


// TODO: This fails spectacularly if the input is not an array.
@Component({
    selector: 'card-table-field',
    templateUrl: 'app/cards/card-table-field.component.html'
})
export class CardTableFieldComponent {
    @Input() table: any;
    @Output() tableChanged: EventEmitter<any> = new EventEmitter();

    ngOnInit() {
        this.tableCopy = JSON.parse(JSON.stringify(this.table));
    }

    valueChanged(r, c, value) {
        this.table[r][c] = value;
        console.log(JSON.stringify(this.table));
    }

//    addStatClicked() {
//        // Do error validation
//        if (!this.stats || !(this.stats.constructor === Array)) {
//            console.log("Fixing a bad model thingy");
//            this.stats = [];
//        }
//
//        // Add a new line
//        this.stats.push({id:`${this.statList[0].id}`, value:""});
//
//        // Propagate the event
//        this.statsChanged.emit(this.stats);
//    }
//
//    removeStatClicked(stat) {
//        let index = this.stats.indexOf(stat);
//        if (index > -1) {
//            this.stats.splice(index, 1);
//        }
//    }

}
