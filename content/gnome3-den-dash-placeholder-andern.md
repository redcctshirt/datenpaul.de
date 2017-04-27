Title: Gnome3 - den Dash-Placeholder ändern
Date: 2011-09-03 20:52
Author: heiko
Category: Gnome
Tags: Dash, Fedora, Gnome, Gnome3, Linux, Placeholder
Slug: gnome3-den-dash-placeholder-andern

In der Favoritenliste (Dash) wird der Dash-Placeholder dann angezeigt
wenn ein Icon an einen anderen Platz gezogen wird. Die Grafikdatei
/usr/share/gnome-shell/theme/dash-placeholder.svg wird unter dem Icon
angezeigt. (ein kleiner weißer Strich mit einem weißen Punkt in der
Mitte) Vom Prinzip her ist es genau das Gleiche wie beim
[Running-Indicator][]. Es existieren die gleichen Möglichkeiten um den
Dash-Placeholder zu ändern.

​1. Möglichkeit – mit einem [SVG-Editor][] die Datei
dash-placeholder.svg ändern

​2. Möglichkeit – den Dash-Placeholder deaktivieren

`su -c “nano /usr/share/gnome-shell/theme/gnome-shell.css” 434 .dash-placeholder { 435 /* background-image: url("dash-placeholder.svg") */ 436 height: 27px; 437 width: 48px; 438 } [ Speichern - Strg+O, Programm beenden - Strg+X]`

​3. Möglichkeit – eine andere Grafikdatei nutzen

`su -c “nano /usr/share/gnome-shell/theme/gnome-shell.css” 434 .dash-placeholder { 435 background-image: url("name.svg") 436 height: 27px; 437 width: 48px; 438 } [ Speichern - Strg+O, Programm beenden - Strg+X]`

​4. Möglichkeit – eine Hintergrundfarbe benutzen

`su -c “nano /usr/share/gnome-shell/theme/gnome-shell.css” 434 .dash-placeholder { 435 background-color: #D4E1F3; 436 height: 27px; 437 width: 48px; 438 } [ Speichern - Strg+O, Programm beenden - Strg+X]`

Um den neuen Dash-Placeholder im Dash sichtbar zu machen ist ein
Gnome-Theme-Neustart erforderlich. Hierzu drückt man gleichzeitig die
Tasten Alt und F2 und tippt rt ein.

  [Running-Indicator]: http://www.datenpaul.de/archives/111
    "Gnome - den Running-Indicator aendern"
  [SVG-Editor]: http://de.wikipedia.org/wiki/Scalable_Vector_Graphics
    "WP:SVG"
