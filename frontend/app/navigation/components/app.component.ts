import {Component, OnInit} from 'angular2/core';
import {RouteConfig, ROUTER_DIRECTIVES, ROUTER_PROVIDERS} from 'angular2/router';
import {HomePageComponent} from '../../home/components/home-page.component'
import {CardEditorComponent} from '../../card-editor/components/card-editor.component'

@Component({
    selector: 'app',
    templateUrl: 'app/navigation/components/app.component.html',
    styleUrls: ['app/navigation/components/app.component.css'],
    directives: [ROUTER_DIRECTIVES],
    providers: [ROUTER_PROVIDERS]
})
@RouteConfig([
  {
    path: '/',
    name: 'Home',
    component: HomePageComponent
  },
  {
    path: '/cards',
    name: 'Cards',
    component: CardEditorComponent
  },
])
export class AppComponent { }