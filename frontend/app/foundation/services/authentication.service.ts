import {Injectable, Inject} from 'angular2/core';
import {Http, Headers, Response} from 'angular2/http';


@Injectable()
export class AuthenticationService {
    authenticate(username, password) {
        let creds = btoa(`${username}:${password}`)
        // TODO: Test that this login is valid
        localStorage.setItem('auth', creds);
    }

    getAuthToken() {
        return localStorage.getItem('auth');
    }
}