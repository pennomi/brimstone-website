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
        if (!this.table) {
            this.table = [];
        }
        this.tableCopy = JSON.parse(JSON.stringify(this.table));
    }

    valueChanged(r, c, value) {
        this.table[r][c] = value;
        this.tableChanged.emit();
    }

    addRow() {
        if (!this.table[0]) {
            let width = 1;
        } else {
            let width = Math.min(this.table[0].length, 1);
        }
        this.table.push(Array(width).fill(""));
        this.tableCopy.push(Array(width).fill(""));
        this.tableChanged.emit();
    }
}
