Title: SimpleHTTPServer - schnell mal Dateien über www verfügbar machen
Date: 2012-05-25 19:27
Author: heiko
Category: Programmierung
Tags: Fedora, Linux, Python, SimpleHTTPServer, web, webserver, www
Slug: simplehttpserver-schnell-mal-dateien-uber-www-verfugbar-machen

SimpleHTTPServer ist ein [Webserver][], in [Python][] geschrieben und
für den einfachen, schnellen, temporären Einsatz gedacht, um z.B.
Dateien oder statische Webseiten per World Wide Web abrufbereit zu
machen. SimpleHTTPServer muss bei den meisten grossen
[Linux-Distribution][] nicht nachinstalliert werden, denn er ist ein
Modul von Python. Gestartet wird der Webserver mittels Befehl
`python -m SimpleHTTPServer` im jeweiligen Verzeichnis. Dieses
Verzeichnis wird gewissermassen zum Wurzelverzeichnis des Webservers. Im
Browser tippt man nunmehr `http://localhost:8000` ein um auf die Dateien
zugreifen zu können. 8000 ist die Standardportnummer. Die Portnummer
kann man auch abändern indem man eine andere beim Start angibt. z.B.
`python -m SimpleHTTPServer 8080` Die dazugehörigen Python-Dateien
findet man übrigens bei Fedora 16 (64bit) im Verzeichnis
/usr/lib64/python2.7/.

  [Webserver]: https://de.wikipedia.org/wiki/Webserver "WP:Webserver"
  [Python]: https://de.wikipedia.org/wiki/Python_%28Programmiersprache%29
    "WP:Python"
  [Linux-Distribution]: https://de.wikipedia.org/wiki/Linux-Distribution
    "WP:Linux-Distributionen"
