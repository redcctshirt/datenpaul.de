Title: Gnome3 - Looking Glass
Date: 2012-03-21 22:23
Author: heiko
Category: Gnome
Tags: Fedora, Gnome, Gnome3, Linux, Looking Glass
Slug: gnome-looking-glass

Looking Glass ist ein Inspektor-Tool von Gnome-Shell, bzw. eine
Javascript-Konsole für die Fehlersuche. Gestartet wird das Tool durch
Alt+F2 und die Eingabe lg. Beendet wird die Konsole durch ESC. Es
existieren 5 Areale. (Evaluator, Windows, Errors, Memory, Extensions)
Der Evaluator ist ein interaktiver Javascript-Dialog. Einfache
Rechenaufgaben können an dieser Stelle z.B. ausgeführt werden. Jedes
Ergebnis wird gespeichert und kann wieder ausgegeben werden durch r(Nr).

`> 1+2 r(0) = 3 > 2+3 r(1) = 5 > r(0) r(2) = 3 > r(1) r(3) = 5 > r(0) + r(1) r(4) = 8`

Eine History-Funktion besteht. Das bedeutet durch die Cursor-Tasten Hoch
und Runter kann man zwischen den Eingaben, die man schon getätigt hat,
hin- und herspringen. Gespeichert wird die History unter dem
dconf-Eintrag /org/gnome/shell/looking-glass-history. Durch die Vergabe
von False und True beim Eintrag /org/gnome/shell/development-tools kann
Looking Glass deaktiviert und aktiviert werden.

`dconf read /org/gnome/shell/looking-glass-history # Looking-Glass-History anzeigen lassen dconf read /org/gnome/shell/development-tools # Wert auslesen dconf write /org/gnome/shell/development-tools false # Looking Glass deaktivieren dconf write /org/gnome/shell/development-tools true # Looking Glass aktivieren`

Die Fenster werden unter Windows aufgelistet. Unter Errors findet man
eine Ansicht für die Shell-Log-Nachrichten. Eine eigene Meldung kann
durch die Eingabe global.log("Meldung") hinzugefügt werden.
Speicherinformationen enthält der Bereich Memory. Unter Extensions
werden die Erweiterungen angezeigt. Die definierten Funktionen von
Looking Glass findet man in der Datei
/usr/share/gnome-shell/js/ui/LookingGlass.js. Das Aussehen von Looking
Glass kann man verändern in der Datei
/usr/share/gnome-shell/theme/gnome-shell.css im Abschnitt /\* Looking
Glass \*/.
