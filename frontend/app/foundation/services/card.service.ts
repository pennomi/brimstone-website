import {Injectable, Inject} from 'angular2/core';
import {Http, Headers, Response, RequestOptions} from 'angular2/http';
import {AuthenticationService} from './authentication.service';


@Injectable()
export class CardService {
    constructor(private http:Http, private _authenticationService:AuthenticationService) { }

    // A basic request method that standardizes authentication
    _api(method, url, body=undefined) {
        // TODO: This is failing on Firefox for some stupid reason.
        var headers = new Headers({
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        });
        if (this._authenticationService.getAuthToken()) {
            headers.append('Authorization', 'Basic ' + this._authenticationService.getAuthToken());
        }
        let options = new RequestOptions({ headers: headers });
        return this.http[method](
            `http://localhost:8000/api/${url}`, JSON.stringify(body), options
        ).map((res:Response) => res.json());
    }


    // Cards
    getCardList() {
        return this._api('get', 'cards/');
    }

    getCard(id: number) {
        return this._api('get', `cards/${id}/`);
    }


    // Card Types
    getTypeList() {
        // TODO: Cache since this should almost never change
        return this._api('get', 'card-types/');
    }

    // Stat Types
    getStatList() {
        // TODO: Cache since this should almost never change
        return this._api('get', 'stat-types/');
    }

    // Revisions
    getRevisionsForCard(cardId) {
        return this._api('get', `card-revisions/?card=${cardId}`);
    }

    saveRevision(revision) {
        if (revision.id) {
            console.log(revision);
            return this._api('put', `card-revisions/${revision.id}/`, revision);
        } else {
            return this._api('post', 'card-revisions/', revision);
        }
    }

    approveRevision(revisionId) {
        return this._api('post', `card-revisions/${revisionId}/approve/`);
    }

    rejectRevision(revisionId) {
        return this._api('post', `card-revisions/${revisionId}/reject/`);
    }
}