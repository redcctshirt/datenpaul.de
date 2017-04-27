Title: Gnome3 - Ordner vor Dateien anzeigen
Date: 2013-02-15 18:39
Author: heiko
Category: Gnome
Tags: donf-editor, Gnome, Gnome3, gsettings, Linux, nautilus, sort-directories-first
Slug: gnome3-ordner-vor-dateien-anzeigen

Die Dateien können im Dateimanager nach Name, Größe, Typ und
Änderungsdatum sortiert werden. Dabei kann es vorkommen, dass Ordner
ganz unten im Fenster landen und nicht oben angezeigt werden.  
![nautilus - Dateien sortieren][]  
Um die Ordner vor den Dateien zu sortieren klickt man auf Dateien, geht
zu den Einstellungen und setzt ein Häkchen bei "Ordner vor Dateien
anzeigen".  
![nautilus - Einstellungen][]  
Im `dconf-editor` findet man diese Einstellung unter
org.gnome.nautilus.preferences sort-directories-first.  
![dconf-editor-Einstellung][]  
Per Befehl
`gsettings get org.gnome.nautilus.preferences sort-directories-first`
kann man den Einstellungszustand abfragen. Mittels set kann man die
Einstellung ändern, true für das Häkchen und false für kein Häkchen.
(`gsettings set org.gnome.nautilus.preferences sort-directories-first true|false`)

  [nautilus - Dateien sortieren]: http://www.datenpaul.de/archive/sortdirfirst0.png
  [nautilus - Einstellungen]: http://www.datenpaul.de/archive/sortdirfirst2.png
  [dconf-editor-Einstellung]: http://www.datenpaul.de/archive/sortdirfirst1.png
