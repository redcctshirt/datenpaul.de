Title: bottle - ein schnelles und einfaches WSGI-Microframework
Date: 2012-06-06 23:37
Author: heiko
Category: Programmierung
Tags: bottle, Fedora, Linux, Programmierung, Python, WSGI
Slug: bottle-ein-schnelles-und-einfaches-wsgi-microframework

Bottle ist in der [Programmiersprache Python][] geschrieben und auf der
Seite [bottlepy.org][] zu finden. Bottle ist ein schnelles und einfaches
[WSGI][]-Microframework. Es besteht aus einer einzelnen Modul-Datei und
hat keine Abhängigkeiten. Installiert wird bottle bei Fedora mittels
Kommando `su -c "easy_install bottle"`. Ebenso kann bottle durch den
Paketmanager oder durch den direkten Download der Modul-Datei ins
Betriebssystem gelangen. Ein Beispiel zeigt wie einfach es nun ist mit
bottle eine Webapplication zu erstellen.

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    from bottle import route, run

    @route('/hallo')
    def hallo():
        return '<b>Hallo Welt!</b>'

    run()

In Zeile 3 werden die erforderlichen Klassen von bottle importiert.
Ebenso wäre das Importieren von allen Klassen durch `import bottle`
möglich. @route('/hallo') erzeugt eine Seite wobei die folgende Funktion
an diese Route gebunden wird. Die Ausgabe erfolgt am Ende durch den
Befehl return. Es kann nur eine Funktion an die Route gebunden werden.
Aber es ist machbar mehrere Routen an eine Funktion zu binden. In Zeile
9 wird die Webapplication gestartet. Sobald das Skript mit python
ausgeführt wird, sieht man die Ausgabe Hallo Welt, nach der Eingabe
http://localhost:8080/hallo, im Browser. Beendet wird die Webapplication
anhand von Strg+C.

  [Programmiersprache Python]: https://de.wikipedia.org/wiki/Python_%28Programmiersprache%29
    "WP:Python"
  [bottlepy.org]: http://bottlepy.org "bottlepy.org"
  [WSGI]: https://de.wikipedia.org/wiki/Web_Server_Gateway_Interface
    "WP:WSGI"
