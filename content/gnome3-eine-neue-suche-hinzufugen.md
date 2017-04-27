Title: Gnome3 - eine neue Suche hinzufügen
Date: 2012-09-28 18:18
Author: heiko
Category: Gnome
Tags: Fedora, Gnome, Gnome3, Linux, Suche
Slug: gnome3-eine-neue-suche-hinzufugen

Bei der neuen Suche wird als Beispiel die Suchmaschine
[duckduckgo.com][] eingesetzt. Die Such-URL bei duckduckgo sieht wie
folgt aus: https://duckduckgo.com/?q=Suchbegriff  
Sobald man den Aktivitäten-Modus (mit dem Mauspfeil links oben in die
Ecke wandern) wählt, erscheint oben rechts eine Sucheingabe, mit dem
Text Suchbegriff eingeben.  
![Gnome3 Suchbox Screenshot][]  
Gibt man etwas ein wird in den Anwendungen, Einstellungen, bei den
Kontakten und bei der Dokumentverwaltung danach gesucht. Ebenso
erscheinen unten 2 Buttons (Wikipedia, Google), die es ermöglichen, dass
nach diesem Eintrag auch in einer Suchmaschine gestöbert wird. Diese
Suchmaschinen findet man im Verzeichnis
`/usr/share/gnome-shell/open-search-providers/`. Um eine neue Suche
hinzuzufügen kopiert man einfach eine dieser xml-Dateien und modifiziert
die neue Datei. Das Kopieren wird mittels Befehl (bei [Fedora][])
`su -c "cp /usr/share/gnome-shell/open-search-providers/wikipedia.xml /usr/share/gnome-shell/open-search-providers/duckduckgo.xml"`
bewerkstelligt. Die Modifizierung erfolgt durch einen Texteditor, z.B.
durch
`su -c "nano /usr/share/gnome-shell/open-search-providers/duckduckgo.xml"`
(Strg+O - Speichern, Strg+X - nano Beenden). \<ShortName\>,
\<Description\> und \<Url template\> sind die wichtigsten Anpassungen
die durchgeführt werden müssen.  
Bsp: /usr/share/gnome-shell/open-search-providers/duckduckgo.xml

    <ShortName>DuckDuckGo</ShortName>
    <Description>DuckDuckGo, free Search</Description>
    <InputEncoding>UTF-8</InputEncoding>
    <Url type="text/html" method="GET" template="https://duckduckgo.com/?q={searchTerms}"/>

Nach einem Neustart mit Alt+F2 r ist DuckDuckGo nun ebenfalls bei den
Suchmaschinen mit dabei. Die Funktionen für die Suche, in Javascript
geschrieben, befinden sich in den Dateien
`/usr/share/gnome-shell/js/ui/search.js` und
`/usr/share/gnome-shell/js/ui/searchDisplay.js`. Das Aussehen kann man
in der Datei `/usr/share/gnome-shell/theme/gnome-shell.css`
beeinflussen. 2 Beispiele: Im Bereich Search Box unter \#searchArea kann
man z.B. die Hintergrundfarbe der Suchbox verändern. Im Teil Search
Results unter .dash-search-button ist es machbar die Hintergrundfarbe
der Suchbuttons zu ändern. Natürlich sind viele Änderungen mehr möglich.
Nach einem Neustart mittels Alt+F2 r werden die Abänderungen sichtbar.
Bsp: /usr/share/gnome-shell/theme/gnome-shell.css

    /* Search Box */

    #searchArea {
        padding: 0px 24px;
        background-color: red;
    }
    /* Search Results */
    .dash-search-button {
        border-radius: 16px;
        padding-top: 4px;
        padding-bottom: 5px;
        width: 300px;
        font-weight: bold;
        background-color: green;
    }

  [duckduckgo.com]: http://duckduckgo.com "Suchmaschine duckduckgo.com"
  [Gnome3 Suchbox Screenshot]: http://www.datenpaul.de/archive/gnome_suchbox.png
  [Fedora]: https://de.wikipedia.org/wiki/Fedora_%28Linux-Distribution%29
    "WP:Fedora"
