import {Pipe, PipeTransform} from 'angular2/core';

@Pipe({name: 'friendlyDate'})
export class FriendlyDatePipe implements PipeTransform {
    transform(value:str): str {
        // TODO: Take in either string, date, or Moment.
        // Convert it to a friendly time, such as "1h ago", or "just now",
        // "yesterday", "Mar 13", "Apr 01, 2015", etc.
        let d = new Date(value)
        return d;
    }
}