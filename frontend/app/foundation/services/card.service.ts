import {Injectable, Inject} from 'angular2/core';
import {Http, Headers, Response} from 'angular2/http';


@Injectable()
export class CardService {
    constructor(private http:Http) { }

    // A basic request method that standardizes authentication
    _api(method, url, body=undefined) {
        var headers = new Headers();
        headers.append('Content-Type', 'application/json');
        headers.append('Authorization', 'Token 1234');
        return this.http[method](
            `http://localhost:8000/api/${url}`, JSON.stringify(body), {headers: headers}
        ).map((res:Response) => res.json());
    }

    getCardList() {
        return this._api('get', 'cards/');
    }

    getCard(id: number) {
        return this._api('get', `cards/${id}/`);
    }

    saveRevision(revision) {
        if (revision.id) {
            console.log(revision);
            return this._api('put', `card-revisions/${revision.id}/`, revision);
        } else {
            return this._api('post', 'card-revisions/', revision);
        }
    }
}