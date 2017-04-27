Title: CouchDB - Installation
Date: 2012-04-10 17:19
Author: heiko
Category: CouchDB
Tags: CouchDB, Datenbank, Fedora, Linux, NoSQL
Slug: couchdb-installation

[CouchDB][] ist ein Open-Source-NoSQL-Datenbanksystem. CouchDB ist ein
dokumentenorientiertes und schemaloses Datenbanksystem. Es ist also kein
relationales Datenbanksystem wie z.B. [MySQL][]. Die Daten werden in
einem Dokument im [JSON-Format][] gespeichert. Mittels Paketmanager kann
CouchDB problemlos bei jeder Linux-Distribution installiert werden. Die
Installation in der Kommandozeile bei Fedora wird durch folgende Eingabe
durchgeführt:

`su -c "yum install couchdb"`

Gestartet wird CouchDB durch die Eingabe:

`su -c "systemctl start couchdb.service"`

Durch eine einfache HTTP-Anfrage testet man ob CouchDB läuft. Den
Browser starten und folgendes eintippen:

`http://localhost:5984`

Als Antwort bekommt man sofort ein JSON-Objekt zu Gesicht. Zum Beispiel:

`{ "couchdb": "Welcome", "version": "1.0.3"}`

Ebenso kann man die HTTP-Anfrage auch in der Kommandozeile stellen:

`curl http://localhost:5984`

Beendet wird CouchDB durch die Eingabe:

`su -c "systemctl stop couchdb.service"`

  [CouchDB]: http://de.wikipedia.org/wiki/CouchDB "WP:couchdb"
  [MySQL]: http://de.wikipedia.org/wiki/mysql "WP:MySQL"
  [JSON-Format]: http://de.wikipedia.org/wiki/JSON "WP:JSON"
