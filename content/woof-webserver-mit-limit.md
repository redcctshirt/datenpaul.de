Title: woof - Webserver mit Limit
Date: 2012-10-19 01:07
Author: heiko
Category: Linux
Tags: Fedora, Gnome, Linux, Python, web, webserver, woof, www
Slug: woof-webserver-mit-limit

An dieser Stelle wird der kleine [Webserver][] woof (web offer one file)
vorgestellt. woof ist in [Python][] geschrieben. Das Besondere ist, dass
es ein Download- und Upload-Limit gibt, sobald diese Grenze erreicht
wird schaltet sich der Webserver von alleine aus. Das Skript findet man
auf der Webseite <http://www.home.unix-ag.org/simon/woof.html>. Klickt
man das Skript im Downloadbereich an, kann man den Inhalt auf der
Webseite sehen. Der Datei-Menüpunkt "Seite Speichern unter" im
Webbrowser kann nun benutzt werden um woof an die gewünschte Stelle im
Dateisystem zu kopieren. Das Zugriffsrecht "Datei als Programm
ausführen" muss für das Skript noch markiert werden und schon steht woof
zum Einsatz bereit. Eine Hilfestellung erscheint nach der Eingabe
`./woof.py`. Mit der Option -i wird die IP-Adresse, durch -c das Limit
und mit -p wird der Port bestimmt. Ohne Angaben werden die Standardwerte
genutzt. (Port 8080, Limit 1, IP 127.0.0.1).

Beispiel:  
`./woof.py dateiname` (Jene Anweisung ermöglicht ein Download der
Datei, durch den Zugriff auf http://127.0.0.1:8080).  
`./woof.py -c 2 dateiname` (2 Downloads möglich bis der Dienst beendet
wird)  
Mittels `./woof.py -U` erlaubt man einen Upload bevor woof beendet
wird.

  [Webserver]: https://de.wikipedia.org/wiki/Webserver "WP:Webserver"
  [Python]: https://de.wikipedia.org/wiki/Python_%28Programmiersprache%29
    "WP:Python"
