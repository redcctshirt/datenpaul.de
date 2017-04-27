Title: bottle - statische Dateien
Date: 2012-06-20 21:57
Author: heiko
Category: Programmierung
Tags: bottle, Fedora, Linux, Programmierung, Python, WSGI
Slug: bottle-statische-dateien

Routen für statische Dateien wie z.B. CSS-Dateien, Bildern und
pdf-Dateien sind nicht automatisch Bestandteil einer bottle-App. Für
jede einzelne Datei muss eine Route definiert werden. Per Dynamischer
Route kann dies durch eine einzige @route-Anweisung erledigt werden. Um
Zugriff auf Dateien mittels Web zu ermöglichen gibt es die Funktion
static\_file. Um die Funktion zu aktivieren muss zusätzlich die Klasse
static\_file von bottle importiert werden. Als ersten Parameter gibt man
den Dateinamen an und als zweiten Parameter das lokale Verzeichnis in
dem diese Datei zu finden ist. Hier ein Beispiel: (z.B.
http://localhost:8080/static/index.png greift auf /home/paul/index.png
zu)

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    from bottle import route, run, debug, static_file

    @route('/static/<filepath:path>')
    def hallo(filepath):
        return static_file(filepath, root='/home/paul/')

    debug(True)
    run(reloader=True)

