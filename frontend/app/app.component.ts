import {Component, OnInit} from 'angular2/core';
import {HTTP_PROVIDERS} from 'angular2/http';
import {RouteConfig, ROUTER_DIRECTIVES, ROUTER_PROVIDERS} from 'angular2/router';

import {HomePageComponent} from './home/home-page.component';
import {CardListPageComponent} from './cards/card-list-page.component';
import {CardDetailPageComponent} from './cards/card-detail-page.component';
import {LoginPageComponent} from './auth/login-page.component';

import {CardService} from './services/card.service';
import {AuthenticationService} from './services/authentication.service';


@Component({
    selector: 'app',
    templateUrl: 'app/app.component.html',
    styleUrls: ['app/app.component.css'],
    directives: [ROUTER_DIRECTIVES],
    providers: [ROUTER_PROVIDERS, HTTP_PROVIDERS, CardService, AuthenticationService]
})
@RouteConfig([
    {
        path: '/',
        name: 'Home',
        component: HomePageComponent
    },
    {
        path: '/login',
        name: 'Login',
        component: LoginPageComponent
    },
    {
        path: '/cards',
        name: 'CardList',
        component: CardListPageComponent
    },
    {
        path: '/cards/:id',
        name: 'CardDetail',
        component: CardDetailPageComponent
    },
])
export class AppComponent { }
