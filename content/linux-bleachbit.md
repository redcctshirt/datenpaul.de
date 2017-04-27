Title: Linux - Bleachbit
Date: 2012-09-11 17:58
Author: heiko
Category: Linux
Tags: bleachbit, Fedora, Linux
Slug: linux-bleachbit

Bleachbit kann eingesetzt werden um die Geschwindigkeit zu optimieren,
aber hauptsächlich wird es benutzt um Daten zu löschen die die
Privatsphäre betreffen, wie z.B. Cookies, temporäre files, Logs, den
Browserverlauf usw.. Sowohl für Windows, als auch für
Linux-Distributionen steht das Programm zur Verfügung. Es wurde in
Python geschrieben, steht unter der [GPL-Lizenz][] und wurde bisher in
56 Sprachen übersetzt. Bleachbit findet man auf der Website
[bleachbit.sourceforge.net][]. Die Installation erfolgt über den
Paketmanager oder mittels Befehl `su -c "yum install bleachbit"`. (bei
Fedora). Unter Aktivitäten - Anwendungen - Systemwerkzeuge wird das Tool
eingegliedert.  
![Bleachbit Screenshot][]  
Die Vorschau-Option gibt Auskunft darüber welche Dateien entfernt
werden. Sobald der Button Löschen betätigt wurde beginnt die
Reinigungsaktion. Durch das XML-Format CleanerML ist es machbar selbst
zu definieren welche Dateien gelöscht werden sollen. Man kann selbst
neue Cleaner für bestimmte Programme schreiben. Diese xml-Dateien
befinden sich im Verzeichnis /usr/share/bleachbit/cleaners. In der
Kommandozeile kann bleachbit ebenso zum Einsatz kommen. bleachbit -l
listet alle Cleaner und Optionen auf. Die Vorschau wird mittels
--preview oder -p angestoßen (z.B. bleachbit -p bash.history) und
--delete --overwrite oder -d -o ist die Reinigungsanweisung (z.B.
bleachbit -d -o bash.history). Die Konfigurationsdatei befindet sich im
Verzeichnis \~/.config/bleachbit/ und heisst bleachbit.ini.

  [GPL-Lizenz]: http://de.wikipedia.org/wiki/GPL "WP:GPL"
  [bleachbit.sourceforge.net]: http://bleachbit.sourceforge.net
    "bleachbit"
  [Bleachbit Screenshot]: http://www.datenpaul.de/archive/bleachbit.png
