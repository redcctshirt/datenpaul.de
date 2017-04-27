Title: CouchDB - Dokumente erstellen und löschen
Date: 2012-06-30 23:40
Author: heiko
Category: CouchDB
Tags: CouchDB, curl, Datenbank, Fedora, futon, Linux, NoSQL
Slug: couchdb-dokumente-erstellen-und-loschen

Jedes Dokument besitzt mindestens die beiden Felder \_id für die
einmalige Identifikationsnummer und \_rev für die Versionsnummer.
Betätigt man in einer Datenbank, mittels Webinterface Futon, den Button
New Document um ein neues Dokument zu erstellen wird ein Hash-Wert als
\_id-Wert vorgeschlagen. Die Versionsnummer wird automatisch
gespeichert. Ebenso ist es machbar einen eigenen \_id-Wert zu bestimmen.
Am Anfang darf es keinen Unterstrich geben und auf Sonderzeichen sollte
man verzichten. Bei jeder Änderung in einem Dokument gibt es, wie bei
Wikis, eine neue Version. Die Versionsnummer \_rev wird geändert. Um
sich Hash-Werte im Terminal für die \_id anzeigen zu lassen muss
folgender Befehl eingegeben werden:
`curl -X GET http://localhost:5984/_uuids`  
Mittels `curl -X GET http://localhost:5984/_uuids?count=10` werden 10
davon ausgegeben. Erstellt wird ein Dokument mittels Kommando
`curl -X PUT http://localhost:5984/dbname/hashwert -d {}`. Alle
Dokumente in einer Datenbank werden nach der Eingabe
`curl -X GET http://localhost:5984/dbname/_all_docs` aufgelistet.
Außerdem ist es möglich den New Document-Job durch den Befehl
`curl -X POST http://localhost:5984/dbname/ -H "Content-Type: application/json" -d {}`
zu initiieren. Die \_id wird diesmal automatisch vergeben. Gelöscht wird
ein Dokument per Befehl
`curl -X DELETE http://localhost:5984/dbname/hashwert?rev=Versionsnummer`.
