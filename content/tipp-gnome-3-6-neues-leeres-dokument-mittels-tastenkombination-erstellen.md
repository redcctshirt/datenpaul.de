Title: Tipp: Gnome 3.6 - neues leeres Dokument mittels Tastenkombination erstellen
Date: 2013-02-19 21:12
Author: heiko
Category: Gnome
Tags: accels, Dateimanager, Fedora, Gnome, Gnome3, Linux, nautilus, touch
Slug: tipp-gnome-3-6-neues-leeres-dokument-mittels-tastenkombination-erstellen

Bei Gnome 3.6 ist der Eintrag "Neues Leeres Dokument" im Kontextmenü des
Dateimanagers nicht mehr vorhanden. Lediglich die Funktion "Neuer
Ordner" existiert noch. Es ist auch leicht möglich mit dem jeweiligen
Programm oder per Befehl touch eine neue Datei zu erstellen. Wer
dennoch, wenigsten mit Hilfe einer Tastenkombination, ein neues leeres
Dokument erzeugen will kann die Datei `~/.config/nautilus/accels`
mittels eines Texteditor abändern. Zum Beispiel durch den Befehl
`nano ~/.config/nautilus/accels`. Man editiert folgende Zeile:

`; (gtk_accel_path "<Actions>/DirViewActions/New Empty Document" "")`

Das Semikolon wird ganz am Anfang entfernt und zwischen den beiden
Anführungszeichen "" gibt man eine Tastenkombination seiner Wahl an. So
könnte die modifizierte Zeile so aussehen:

`(gtk_accel_path "<Actions>/DirViewActions/New Empty Document" "<Alt>n")`

Mit Strg+O und anschliessend Strg+X werden die Veränderungen gesichert
und nano wird beendet. Ab sofort wird per Tastenkombination Alt+n im
Dateimanager eine neue leere Datei angelegt. (Hinweis:
Dateimanagerfenster schliessen und neu öffnen um Änderungen wirksam zu
machen) Ausserdem gibt es die Möglichkeit den Kontextmenüeintrag "Neues
Leeres Dokument" zurückzuholen. Unter Zuhilfenahme des Kommandos
`touch ~/Vorlagen/neu` erzeugt man ein neues Dokument im Ordner Vorlagen
(engl. Templates). Nach dem Neustart des Dateimanagers ist die Funktion
wieder verfügbar. Den Vorlagen-Ordner kann man übrigens in der Datei
`~/.config/user-dirs.dirs` bestimmen.
(`XDG_TEMPLATES_DIR="$HOME/Vorlagen"`)
