Title: Gnome3 - den Running-Indicator ändern
Date: 2011-08-21 22:50
Author: heiko
Category: Gnome
Tags: Dash, Fedora, Gnome, Gnome3, Linux, running-indicator
Slug: gnome3-den-running-indicator-andern

Sobald ein Programm läuft wird das Programm in der Favoritenliste, auch
Dash genannt, besonders gekennzeichnet. Zu der Favoritenliste kommt man
über Aktivitäten. (links oben) Wenn man z.B. den Dateimanager startet
wird prompt im Hintergrund des Icons ein kleiner weißer Schatten
angezeigt. Das ist der Running-Indicator.

![running-indicator1][]

Die Grafik dazu findet man im Verzeichnis /usr/share/gnome-shell/theme.
Die Datei heißt running-indicator.svg.

![running-indicator2][]

Nun gibt es mehrere Möglichkeiten um den Running-Indicator zu ändern.

​1. Möglichkeit - mit Inkscape (oder einem anderen SVG-Editor) die Datei
running-indicator.svg ändern

**su -c "yum install inkscape"** (Paket installieren, falls noch nicht
vorhanden)  
**su -c "inkscape /usr/share/gnome-shell/theme/running-indicator.svg"**

​2. Möglichkeit - den Running-Indicator deaktivieren  
Um jenes zu erreichen editiert man die Datei
/usr/share/gnome-shell/theme/gnome-shell.css und kommentiert die Zeile
background-image: url("running-indicator.svg") aus.

**su -c "nano /usr/share/gnome-shell/theme/gnome-shell.css"**  

`644 .app-well-app.running > .overview-icon { 645 text-shadow: black 0px 2px 2px; 646 /* background-image: url("running-indicator.svg") */ 647 }`  
*[ Speichern - Strg+O, Programm beenden - Strg+X]*

![running-indicator3][]

​3. Möglichkeit - eine andere Grafikdatei nutzen  
(Grafikdatei name.svg vorher ins Verzeichnis kopieren, mittels su -c
"cp name.svg /usr/share/gnome-shell/theme/")

**su -c "nano /usr/share/gnome-shell/theme/gnome-shell.css"**  

`644 .app-well-app.running > .overview-icon { 645 text-shadow: black 0px 2px 2px; 646 background-image: url("name.svg") 647 }`  
*[ Speichern - Strg+O, Programm beenden - Strg+X]*

![running-indicator4][]

​4. Möglichkeit - eine Hintergrundfarbe benutzen

**su -c "nano /usr/share/gnome-shell/theme/gnome-shell.css"**  

`644 .app-well-app.running > .overview-icon { 645 text-shadow: black 0px 2px 2px; 646 background-color: #D2B48C; 647 }`  
*[ Speichern - Strg+O, Programm beenden - Strg+X]*

![running-indicator5][]

Um die Änderung sichtbar zu machen ist am Ende ein Gnome-Theme-Neustart
erforderlich. Hierzu benutzt man die Tastenkombination Alt+F2 und gibt
rt ein.

  [running-indicator1]: http://www.datenpaul.de/archive/running-indicator1.png
  [running-indicator2]: http://www.datenpaul.de/archive/running-indicator2.png
  [running-indicator3]: http://www.datenpaul.de/archive/running-indicator3.png
  [running-indicator4]: http://www.datenpaul.de/archive/running-indicator4.png
  [running-indicator5]: http://www.datenpaul.de/archive/running-indicator5.png
