import {Injectable} from 'angular2/core';

@Injectable()
export class CardService {
    private CARDS = [
        {id:1, title: "A"},
        {id:2, title: "B"},
        {id:3, title: "C"},
        {id:4, title: "D"},
        {id:5, title: "E"},
        {id:6, title: "F"}
    ];

    getCardList() {
        return Promise.resolve(this.CARDS);
    }
}