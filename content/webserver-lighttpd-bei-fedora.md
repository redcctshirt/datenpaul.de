Title: Webserver lighttpd bei Fedora
Date: 2012-10-22 22:48
Author: heiko
Category: Linux
Tags: Fedora, lighttpd, Linux, web, webserver, www
Slug: webserver-lighttpd-bei-fedora

In diesem Beitrag soll kurz der ressourcensparende Webserver
[lighttpd][] (ausgesprochen: lighty) vorgestellt werden. lighttpd wurde
in der [Programmiersprache C][] geschrieben, ist auf der Webseite
[www.lighttpd.net][] daheim und die Funktionalität kann durch Module
erweitert werden. Er gehört bei vielen [Linux][]-Distributionen zur
Paketsammlung und kann somit kinderleicht mittels Paketmanager
installiert werden. Bei [Fedora][] lautet der Installationsbefehl
`su -c "yum install lighttpd"`. Bei der Installation wurde das
Konfigurationsverzeichnis /etc durch die Einstellungsdateien von
lighttpd erweitert. Diese befinden sich im Pfad /etc/lighttpd.
/etc/lighttpd/lighttpd.conf ist die Einstellungsdatei von lighttpd. Die
WorldWideWeb-Ressourcen, sprich [HTML][]-Dateien, CSS-Dateien usw.,
werden im Ordner /var/www/lighttpd abgelegt. Der Start des Webservers
erfolgt per Anweisung `su -c "systemctl start lighttpd.service"`. Durch
den Webbrowser kann man nun auf die HTML-Dateien zugreifen, die Eingabe
localhost und die Begrüßungsseite wird geladen. Ein Neustart wird
mittels `su -c "systemctl restart lighttpd.service"` ausgelöst. Beendet
wird der Webserver prompt nach der Eingabe
`su -c "sytemctl stop lighttpd.service"`.

  [lighttpd]: https://de.wikipedia.org/wiki/Lighttpd "WP:lighttpd"
  [Programmiersprache C]: https://de.wikipedia.org/wiki/C_%28Programmiersprache%29
    "WP:C"
  [www.lighttpd.net]: http://www.lighttpd.net "www.lighttpd.net"
  [Linux]: https://de.wikipedia.org/wiki/Linux "WP:Linux"
  [Fedora]: https://de.wikipedia.org/wiki/Fedora_%28Linux-Distribution%29
    "WP:Fedora"
  [HTML]: https://de.wikipedia.org/wiki/HTML "WP:HTML"
