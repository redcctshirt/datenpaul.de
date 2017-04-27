Title: Gnome3 - ein eigenes user-Theme
Date: 2012-10-05 17:35
Author: heiko
Category: Gnome
Tags: CSS, Fedora, Gnome, gnome-tweak-tool, Gnome3, Linux, user-Theme
Slug: gnome3-ein-eigenes-user-theme

In vielen Artikeln der Reihe [Gnome3][] wurde schon oftmals darauf
hingewiesen, dass Erscheinungsbildveränderungen erreicht werden indem
man mit [Root][]rechten die Werte in der Datei gnome-shell.css im
Verzeichnis /usr/share/gnome-shell/theme/ abändert. Es wurde beschrieben
wie man die Hintergrundfarbe vom Dash und die Schrift im Run-Dialog nach
seinem Geschmack verändern kann. In diesem Beitrag möchte ich nun
erläutern wie diese gerade erwähnte Datei unangetastet bleibt und
Aussehensabwandlungen dennoch durch die Erstellung eines eigenen
user-Theme realisierbar sind. Vorraussetzung dafür ist die Installation
des Pakets gnome-shell-extension-user-theme und die Aktivierung der
Erweiterung, z.B. per gnome-tweak-tool unter Shell-Erweiterungen.
Anschliessend erstellt man den versteckten Ordner .themes im
Home-Verzeichnis, gibt seinem Theme einen Namen, erstellt im Verzeichnis
\~/.themes dazu einen Ordner und legt den Ordner gnome-shell in diesem
Ordner an. In dem Ordner gnome-shell wird die Datei gnome-shell.css
angelegt, so dass folgende Struktur entsteht:
\~/.themes/\<name\>/gnome-shell/gnome-shell.css. Durch diese
[css][]-Datei werden nun mittels Importierung alle globalen Werte
übernommen und können einzeln editiert werden. Jenes neue user-Theme
kann anhand des gnome-tweak-tools unter Thema ausgewählt werden.
Werte-Änderungen werden erst nach einem Theme-Neustart (Alt+F2 drücken
und rt eingeben) sichtbar. Beispiel um die Dash-Hintergrundfarbe zu
ändern:

Installation der beiden erwähnten Pakete bei Fedora:
`su -c "yum install gnome-shell-extension-user-theme gnome-tweak-tool"`

\~/.themes/james/gnome-shell/gnome-shell.css

    @import url("/usr/share/gnome-shell/theme/gnome-shell.css");

    #dash {
        background-color: red;
    }

  [Gnome3]: https://de.wikipedia.org/wiki/Gnome "WP:Gnome"
  [Root]: https://de.wikipedia.org/wiki/Root-Konto "WP:Root"
  [css]: https://de.wikipedia.org/wiki/Cascading_Style_Sheets "WP:CSS"
