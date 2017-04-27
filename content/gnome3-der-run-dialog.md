Title: Gnome3 - der Run-Dialog
Date: 2012-03-11 19:25
Author: heiko
Category: Gnome
Tags: Fedora, Gnome, Gnome3, Linux
Slug: gnome3-der-run-dialog

In diesem Artikel steht der Run-Dialog von Gnome3 im Mittelpunkt. Sowie
zeitgleich die Tasten Alt und F2 gedrückt werden erscheint der
Run-Dialog. Der Zweck des Run-Dialogs besteht in der Ausführung von
Kommandos, die manuell vom Benutzer eingegeben werden. Der Run-Dialog
kann an eine andere Tastenkombination gebunden werden. Unter
Systemeinstellungen - Tastatur - Tastaturkürzel - System - Den Befehl
ausführen-Dialog kann man dies bewerkstelligen. Die Funktionen des
Run-Dialogs werden in der Datei
/usr/share/gnome-shell/js/ui/runDialog.js in der Programmiersprache
Javascript definiert. Um die Datei zu modifizieren führt man folgenden
Befehl in einem Terminal aus:

`su -c "nano /usr/share/gnome-shell/js/ui/runDialog.js"`

So ist es z.B. realisierbar den Kommandoeingabetext oder die internen
Kommandos (r,restart,rt,lg,debugexit) zu editieren. Die gespeicherten
(nano: Strg+O - Speichern, Strg+X - Beenden) Abänderungen werden durch
einen Gnome-Shell-Neustart (Alt+F2 r) wirksam.

Der Erscheinungsbild des Run-Dialogs wird in der
Datei /usr/share/gnome-shell/theme/gnome-shell.css festgelegt. Ebenso
ist es möglich in dieser Datei die Werte zu bearbeiten, die für das
Aussehen des Run-Dialogs verantwortlich sind. In der Sektion Run Dialog
ist man nunmehr in der Lage die Schriftfarbe, die Schriftgröße etc. zu
verändern. Die gespeicherten (nano: Strg+O - Speichern, Strg+X -
Beenden) Modifikationen werden durch einen Gnome-Shell-Neustart (Alt+F2
r) sichtbar.

Beispiele:

`su -c "nano /usr/share/gnome-shell/theme/gnome-shell.css"`  

` /* Run Dialog */ .run-dialog-entry { color: white; /* Schriftfarbe ändern */ } .lightbox { background-color: rgba(0, 0, 0, 0.4);  /* Bildschirmhintergrundfarbe ändern */ } .run-dialog { background-color: red; /* Hintergrundfarbe vom Run Dialog ändern */ }`
