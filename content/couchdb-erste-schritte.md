Title: CouchDB - erste Schritte
Date: 2012-04-11 16:53
Author: heiko
Category: CouchDB
Tags: CouchDB, Datenbank, Fedora, Linux, NoSQL
Slug: couchdb-erste-schritte

Gestartet wird [CouchDB][] bei Fedora per Kommando:

`su -c "systemctl start couchdb.service"`

Der Test ob CouchDB läuft erfolgt mittels Eingabe

`localhost:5984`

beim Browser oder in der Kommandozeile per

`curl http://localhost:5984`

Alle vorhandenen Datenbanken werden durch die Eingabe

`curl http://localhost:5984/_all_dbs`

gezeigt. CouchDB besitzt eine [RESTful JSON API][]. Das bedeutet, die
Aktionen auf die Ressourcen geschehen durch eine HTTP-Methode. Anhand
der Eingabe

`curl -X PUT http://localhost:5984/test`

wird eine neue Datenbank mit dem Namen test erstellt. Mittels

`curl -X DELETE http://localhost:5984/test`

kann die Datenbank wieder gelöscht werden. Außerdem verfügt CouchDB über
ein Webinterface namens Futon, das man mit

`http://localhost:5984/_utils/`

erreichen kann.

  [CouchDB]: http://de.wikipedia.org/wiki/CouchDB "WP:CouchDB"
  [RESTful JSON API]: https://de.wikipedia.org/wiki/RESTful "WP:RESTfuö"
