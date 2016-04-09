import {Component, OnInit} from 'angular2/core';
import {AuthenticationService} from '../services/authentication.service';


@Component({
    selector: 'login-page',
    templateUrl: 'app/foundation/login-page.component.html',
    directives: []
})
export class LoginPageComponent {
    constructor(private _authenticationService: AuthenticationService) { }
    username = "";
    password = "";

    loginClicked() {
        this._authenticationService.authenticate(this.username, this.password)
    }
}