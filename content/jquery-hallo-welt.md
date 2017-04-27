Title: jQuery - Hallo Welt
Date: 2012-06-02 23:36
Author: heiko
Category: jQuery
Tags: HTML, HTML5, Javascript, jQuery, Programmierung, World Wide Web, www
Slug: jquery-hallo-welt

[jQuery][] ist ein freies, umfangreiches und leicht erweiterbares
[Javascript][]-Framework. Dieses wundersame Rahmenwerk und Toolset
erfreut sich großer Beliebtheit und wird in vielen bekannten
[Content-Management-Systemen][] eingesetzt. Es vereinfacht
Javascript-Lösungswege und lässt Dynamik und Interaktivität in eine
Website mit einfließen. Animationen können einfach erstellt, Inhalt
hinzugefügt und Elemente verändert werden. Mittels \$-Funktion oder der
jQuery-Funktion wird ein jQuery-Objekt erstellt. Als erstes wird
bestimmt was manipuliert werden soll. Die selektierten Elemente können
dann durch jQuery-Methoden verändert werden. Beispiel:

    <!DOCTYPE html>
    <html>
    <head>
    <style>
    div { font-size: 5em; color: red; }
    </style>
    <script src="http://code.jquery.com/jquery-1.7.2.min.js"></script>
    </head>
    <body>

    <div id="one">Hallo Welt</div>
    <div id="two">jQuery</div>

    <script>
    $(document).ready(function() {
    $("div").css("color","blue");
    });
    </script>
    </body>
    </html>

Per `<script src="http://code.jquery.com/jquery-1.7.2.min.js"></script>`
in Zeile 7 wird jQuery in eine HTML-Seite eingebunden. Durch
\$(document).ready(function() { }); in Zeile 15 und 17 wird das ganze
Dokument geladen bevor die enthaltenen jQuery-Anweisungen ausgeführt
werden. In Zeile 16 kommt es dann zur Veränderung der Textfarbe
innerhalb aller div-Container. Anhand von \$("div") werden alle
div-Container ausgewählt. Mittels \$("div").css("color","blue"); wird
die Eigenschaft color (Textfarbe) mit dem Wert blue belegt. Statt rot,
wie in Zeile 5 durch color: red; festgelegt, wird der Text in allen
div-Containern in blau angezeigt. Eine Spezifizierung auf einen
bestimmten div-Container ist durch die id möglich. Wird
\$("div").css("color","blue"); durch \$("div\#one").css("color","blue");
ersetzt erscheint nur der Inhalt "Hallo Welt" vom div-Container mit der
id one in blau.

  [jQuery]: https://de.wikipedia.org/wiki/JQuery "WP:jQuery"
  [Javascript]: https://de.wikipedia.org/wiki/Javascript "WP:Javascript"
  [Content-Management-Systemen]: https://de.wikipedia.org/wiki/Content-Management-System
    "WP:CMS"
