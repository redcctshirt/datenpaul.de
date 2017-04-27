Title: CouchDB - Datenbankinformationen
Date: 2012-05-21 19:12
Author: heiko
Category: CouchDB
Tags: CouchDB, Fedora, Linux, NoSQL
Slug: couchdb-datenbankinformationen

Bei [Fedora][] werden die binären Datenbankdateien im Verzeichnis
/var/lib/couchdb gespeichert. Informationen über eine Datenbank bekommt
man mittels Eingabe `curl -X GET http://localhost:5984/datenbankname` in
der Kommandozeile präsentiert. Folgende Informationen werden
aufgelistet:  

` db_name - Name der Datenbank doc_count - Anzahl der Dokumente in der Datenbank doc_del_count - Anzahl der gelöschten Dokumente update_seq - aktuelle Anzahl der Aktualisierungen der Datenbank purge_seq - Zahl der Säuberungs-Operationen der Datenbank compact_running - Anzeige ob die compact-Funktion gerade ausgeführt wird (true, false) disk_size - wie viel Speicherplatz die Datenbank benötigt instance_start_time - wann die Datenbank erstellt wurde disk_format_version - Version des Formats für die Datenspeicherung committed_update_seq - Anzahl der committed Update`

  [Fedora]: https://de.wikipedia.org/wiki/Fedora_%28Linux-Distribution%29
    "Fedora"
