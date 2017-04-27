Title: bottle - dynamisches Routing
Date: 2012-06-10 22:01
Author: heiko
Category: Programmierung
Tags: bottle, Fedora, Linux, Programmierung, Python, WSGI
Slug: bottle-dynamisches-routing

Dynamische Routen enthalten Platzhalter für die jegliche Zeichenketten
oder Werte eingesetzt werden können. Es sind Variablen. Diese Variable
wird an die angedockte Funktion weitergegeben und mittels
Funktionsalgorithmus verarbeitet. Ein Beispiel:

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    from bottle import route, run, debug

    @route('/hallo/<name>')
    def hello(name):
        return "Hello {0} !".format(name)

    debug(True)
    run(reloader=True)

Nach /hallo/ können nun Zeichenketten verwendet werden. (z.B.
/hallo/paul /hallo/ina ...) Die eingesetzte Zeichenkette wird in der
Variable name gespeichert und in Zeile 7 ersetzt diese Zeichenkette den
Platzhalter {0}. Platzhalter können auch durch folgende Filter
spezifiziert werden.  

@route('/route/<id:int>') - nur Integer-Werte sind erlaubt 
@route('/route/<id:float>') - nur float-Werte sind erlaubt 
@route('/route/<name:re:[a-z]+>') - erlaubt reguläre Ausdrücke 
@route('/route/<path:path>') - erlaubt Verzeichnisangaben
 
Durch die Zeile 9 mit dem Inhalt debug(True) werden hilfreiche
Fehlermeldungen mit Einzelheiten angezeigt. Der reloader, der in Zeile
10 auf True gesetzt wird, bewirkt dass bei Veränderungen des Skripts
kein Neustart des Programms notwendig ist. ([bottle][])

  [bottle]: http://bottlepy.org "bottle"
