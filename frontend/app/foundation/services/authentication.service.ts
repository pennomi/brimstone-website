import {Injectable, Inject} from 'angular2/core';
import {Http, Headers, Response} from 'angular2/http';


@Injectable()
export class AuthenticationService {
    storedCredentials = "";

    authenticate(username, password) {
        this.storedCredentials = btoa(`${username}:${password}`)
        // TODO: Test that this login is valid
    }
}