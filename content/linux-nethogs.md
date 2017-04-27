Title: Mit nethogs ermitteln wie viel Bandbreite die einzelnen Prozesse nutzen
Date: 2015-08-05 18:51
Author: heiko
Category: Linux
Tags: Linux, nethogs
Slug: linux-nethogs

![linux - nethogs][]

Netzwerk-top-Kommando - so könnte man nethogs umschreiben. `nethogs` ermittelt wie viel Bandbreite die einzelnen Prozesse nutzen. Inzwischen gibt es viele verschiedene Netzwerk-[Monitoring](https://de.wikipedia.org/wiki/Monitoring)-Tools unter Linux. Auf der Webseite [nethogs.sourceforge.net](http://nethogs.sourceforge.net) befinden sich Informationen, über das einfach zu bedienende [OpenSource](https://de.wikipedia.org/wiki/Open_Source)-Tool für die Konsole. Das Programm wird per Paketmanager installiert.

    sudo apt-get install nethogs # bei Linux Mint

Mittels `sudo nethogs` wird das Tool gestartet. Man kann erkennen welche Prozesse viel Bandbreite nutzen und welche Prozesse eher weniger. Drückt man die Taste `q` wird nethogs beendet. Tippt man `sudo nethogs` und anschließend eine bestimmte Netzwerk-Schnittstelle ein, so wird nur diese Schnittstelle überwacht. Standardmäßig wird nethogs jede Sekunde aktualisiert. Durch `-d` kann man die Wartedauer zwischen den Aktualisierungen bestimmen, z.B. `sudo nethogs -d 3` für 3 Sekunden. 
Mit den Tasten `s` und `r` kann man nach gesendet und empfangen sortieren. Ob die Anzeige in Byte, KByte oder MByte ist, kann man durch das Drücken der Taste `m` regeln.

  [linux - nethogs]: http://www.datenpaul.de/archive/nethogs.png



