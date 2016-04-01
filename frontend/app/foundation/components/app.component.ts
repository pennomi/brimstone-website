import {Component, OnInit} from 'angular2/core';
import {HTTP_PROVIDERS} from 'angular2/http';
import {RouteConfig, ROUTER_DIRECTIVES, ROUTER_PROVIDERS} from 'angular2/router';
import {HomePageComponent} from '../../home/components/home-page.component';
import {CardListPageComponent} from '../../cards/components/card-list-page.component';
import {CardDetailPageComponent} from '../../cards/components/card-detail-page.component';
import {CardService} from '../services/card.service';


@Component({
    selector: 'app',
    templateUrl: 'app/foundation/components/app.component.html',
    styleUrls: ['app/foundation/components/app.component.css'],
    directives: [ROUTER_DIRECTIVES],
    providers: [ROUTER_PROVIDERS, HTTP_PROVIDERS, CardService]
})
@RouteConfig([
    {
        path: '/',
        name: 'Home',
        component: HomePageComponent
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