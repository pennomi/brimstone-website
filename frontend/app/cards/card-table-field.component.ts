import {Component, Input, Output, EventEmitter} from 'angular2/core';


// TODO: This fails spectacularly if the input is not an array.
@Component({
  selector: 'card-table-field',
  templateUrl: 'app/cards/card-table-field.component.html'
})
export class CardTableFieldComponent {
  @Input() table: any;
  @Output() tableChanged: EventEmitter<any> = new EventEmitter();

  getTableWidthValues() {
    return Array(this.table.length).fill(0).map((x,i)=>i);
  }

  getTableHeightValues() {
    let row = this.table[0]
    return Array(row.length).fill(0).map((x,i)=>i);
  }

  addRow() {
    var width = 1;
    if (this.table[0]) {
      width = Math.max(this.table[0].length, 1);
    } else {
      this.table = [];
      this.tableChanged.emit(this.table);
    }
    this.table.push(Array(width).fill("TODO"));
    this.tableChanged.emit(this.table);
  }

  addColumn() {
    if (this.table.length == 0) {
      this.addRow();
      return;
    }

    for (let row of this.table) {
      row.push("TODO");
    }
    this.tableChanged.emit(this.table);
  }

  removeRow(i) {
    this.table.splice(i, 1);
  }

  removeColumn(j) {
    for (let row of this.table) {
      row.splice(j, 1);
    }
  }
}
