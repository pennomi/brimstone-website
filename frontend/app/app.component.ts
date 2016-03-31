import {Component} from 'angular2/core';

@Component({
    selector: 'app',
    templateUrl: 'app/app.component.html'
})
export class AppComponent {
    cards = CARDS;

    cardSelected = function (card) {
        this.selectedCard = card;
    }
}

var CARDS = [
    {id:1, title: "A"},
    {id:2, title: "B"},
    {id:3, title: "C"},
    {id:4, title: "D"},
    {id:5, title: "E"},
    {id:6, title: "F"}
];