Title: bottle.py auf Uberspace installieren
Date: 2013-10-19 01:28
Author: admin
Category: Programmierung
Tags: bash, bottle, bottle.py, Flask, Linux, Python, Sinatra, Tutorial, Uberspace, web, WSGI, www
Slug: bottle-py-auf-uberspace-installieren

[bottle.py][] ist ein einfaches, in Python geschriebenes,
Mikro-Framework für Webanwendungen, ähnlich wie [Flask][] (Python) oder
[Sinatra][] (Ruby). Freiesmagazin.de erklärt [hier][] kurz und bündig
wie bottle.py genutzt werden kann. In den folgenden Zeilen möchte ich
erläutern wie man bottle.py auf [Uberspace][] installieren kann.

**bottle.py installieren**

Nach dem Einloggen (per ssh) wechselt man ins Verzeichnis \~/bin um dort
ein neues Projekt-Verzeichnis zu erstellen. (z.B. bottlepy) Anschließend
wird bottle.py mittels Kommando wget heruntergeladen und man schreibt
sein erstes Skript, z.B. in die Datei index.py. In diesem Beispiel wird
in der run-Zeile ein Webserver gestartet der auf Port 8787 läuft.

    cd bin

\# ins Verzeichnis bin wechseln

    mkdir bottlepy

\# ein neues Verzeichnis mit dem Namen bottlepy erstellen

    cd bottlepy

\# in das neue Verzeichnis bottlepy wechseln

    wget https://github.com/defnull/bottle/raw/master/bottle.py

\# bottle.py herunterladen

    cat <<__EOF__ > ./index.py
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    from bottle import route, run, debug

    @route('/')
    def hallo():
        return 'Hallo Welt!'

    debug(True)
    run(reloader=True, host='127.0.0.1', port=8787)
    __EOF__

\# Python-Skript mit bottle.py erstellen, im Verzeichnis \~/bin/bottlepy

**Daemon erstellen**

Was es mit dem Daemon auf sich hat und wie man einen erstellt wird im
[Wiki von Uberspace][] genaustens erklärt.

    test -d ~/service || uberspace-setup-svscan

    mkdir ~/etc/run-my-daemon
    cat <<__EOF__ > ~/etc/run-my-daemon/run
    #!/bin/sh
    cd ~/bin/bottlepy 
    /usr/bin/env python ~/bin/bottlepy/index.py
    __EOF__
    chmod +x ~/etc/run-my-daemon/run
    mkdir ~/etc/run-my-daemon/log
    cat <<__EOF__ > ~/etc/run-my-daemon/log/run
    #!/bin/sh
    exec multilog t ./main
    __EOF__
    chmod +x ~/etc/run-my-daemon/log/run
    ln -s ~/etc/run-my-daemon ~/service/my-daemon

**.htaccess konfigurieren**

Am Ende wird die .htaccess-Datei für den Apache-Webserver im Verzeichnis
\~/html so konfiguriert, dass die an den Webserver gerichteten Anfragen
an den lokalen Port 8787 weitergeleitet werden, also an den laufenden
Webserver der mit dem index.py-Skript und bottle.py gestartet wurde.

    cat <<__EOF__ > ~/html/.htaccess
    RewriteEngine On
    RewriteRule (.*) http://127.0.0.1:8787/$1 [P]
    __EOF__

Nun sollte alles funktionieren und bei einer Anfrage an den Webserver
(http://www.beispieldomain.de/) wird man nun mit einem Hallo Welt!
begrüßt.

[Artikel steht unter der Lizenz:
<http://creativecommons.org/licenses/by/3.0/>  
(by datenpaul.de)]

  [bottle.py]: http://bottlepy.org "bottle.py"
  [Flask]: https://github.com/JonasGroeger/flask-uberspace-quickstart
    "Flask"
  [Sinatra]: http://blog.sangyye.de/2012/06/sinatra-on-uberspace/
    "Sinatra"
  [hier]: http://www.freiesmagazin.de/mobil/freiesMagazin-2011-02.html#11_02_bottle
    "bottle"
  [Uberspace]: https://uberspace.de/ "uberspace"
  [Wiki von Uberspace]: https://uberspace.de/dokuwiki/system:daemontools
    "uberspace wiki"
