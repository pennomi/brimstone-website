import {Injectable, Inject} from 'angular2/core';
import {Http, Response} from 'angular2/http';


@Injectable()
export class CardService {
    constructor(private http:Http) { }

    getCardList() {
        return this.http.get('http://localhost:8000/api/cards/')
                   .map((res:Response) => res.json())
    }

    getCard(id: number) {
        return this.http.get('http://localhost:8000/api/cards/' + id + '/')
                   .map((res:Response) => res.json())
    }
}