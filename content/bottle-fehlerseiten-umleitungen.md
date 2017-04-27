Title: bottle - Fehlerseiten, Umleitungen
Date: 2012-06-29 21:30
Author: heiko
Category: Programmierung
Tags: bottle, Linux, Programmierung, Pyhon, web, WSGI, www
Slug: bottle-fehlerseiten-umleitungen

Eine eigene Fehlerseite für den [HTTP Status Code][] 404 - Not Found
(Seite nicht gefunden) kann durch den error decorator erstellt werden.
Ein Beispiel:

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    from bottle import error, route, run, debug

    @error(404)
    def error404(error):
        return 'Seite nicht gefunden'

    debug(True)
    run(reloader=True)

Fehlermeldungen (HTTP Error Pages) können ebenso mittels
abort()-Funktion  
programmiert werden.

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    from bottle import abort, route, run, debug

    @route('/hallo')
    def hallo():
        abort(401, 'Leider kein Zugriff möglich !'

    debug(True)
    run(reloader=True)

Umleitungen zu einer anderen URL werden durch redirect (HTTP Status Code
- 303) erstellt.

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    from bottle import redirect, route, run, debug

    @route('/hallo')
    def hallo():
        return 'Hallo'

    @route('/303')
    def uml():
        redirect('/hallo')

    debug(True)
    run(reloader=True)

  [HTTP Status Code]: https://de.wikipedia.org/wiki/HTTP-Statuscode
    "WP:HTTP Status Code"
