Eventunity
==========

Find community events near you.  
http://eventunity.seminar.io/

Eventunity is an HTML5 app created with the [Ubuntu SDK](http://developer.ubuntu.com/apps/html-5/) to participate in the [Ubuntu App Showdown 2014](http://developer.ubuntu.com/2014/02/announcing-the-latest-ubuntu-app-showdown-contest/).


Importing events
----------------

From the command line or a crontab job

```
python eventunity-server/manage.py importevents <community id> <events file>
```

the events file must be a JSON list of events like this

```
[
    {
        "coordinates": {
            "lat": 43.6557309,
            "lng": -79.384164
        },
        "date": "2014-04-18 00:00:00+00:00",
        "description": "Trusty Tahr Toronto Release Party!\nFree coffee and decorate-your-own cupcakes as usual.",
        "location": "Alio Lounge (Toronto, Ontario, Canada)",
        "name": "Trusty Tahr Toronto Release Party",
        "url": "http://loco.ubuntu.com/events/ubuntu-ca/2701-trusty-tahr-toronto-release-party/"
    },
    {
        "coordinates": {
            "lat": 46.9471699,
            "lng": 7.4395125
        },
        "date": "2014-05-10 12:00:00+00:00",
        "description": "In 2014 the Swiss Ubucon will take place in Bern at Saturday, May 10, 2014.",
        "location": "Digicomp Bern (Bern, Switzerland)",
        "name": "Ubucon 14",
        "url": "http://loco.ubuntu.com/events/ubuntu-ch/2721-ubucon-14/"
    }
]
```

Contributing
------------

Want to contribute? Great! Bug reports, code and documentation patches are greatly appreciated.  
Please file bugs and send pull requests using the [issue tracker](https://github.com/pabluk/eventunity/issues).


License
-------

* eventunity-html5-app is licensed under [GPL v3](http://www.gnu.org/licenses/gpl-3.0.txt). See [LICENSE](https://raw.github.com/pabluk/eventunity/master/eventunity-html5-app/LICENSE) for details.
* eventunity-server is licensed under [AGPL v3](http://www.gnu.org/licenses/agpl-3.0.txt). See [LICENSE](https://raw.github.com/pabluk/eventunity/master/eventunity-server/LICENSE) for details.

Copyright (C) 2014 Pablo SEMINARIO <pablo@seminar.io>
