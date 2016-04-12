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

    addRow() {
        let width = this.table[0].length
        this.table.push(Array(width).fill(""))
        this.tableCopy.push(Array(width).fill(""))
    }
}
