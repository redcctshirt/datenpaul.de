Title: popcorn.js - Hallo Welt
Date: 2012-05-29 19:34
Author: heiko
Category: Programmierung
Tags: HTML5, Javascript, popcorn.js, Programmierung, video, Videobearbeitung
Slug: popcorn-js-hallo-welt

Durch diesen Artikel möchte ich auf [popcorn.js][] aufmerksam machen.
popcorn.js ist ein [HTML5][] Media Javascript Framework von [Mozilla][].
Jeder der interaktive Medien ins Web bringen möchte kann dieses
Framework einsetzen. Auf der Seite [mozillapopcorn.js][] findet man das
Projekt popcorn. Für das Framework gibt es die Seite [popcornjs.org][].
Demos und Dokumentationen geben eine Übersicht über die Features die
dieses Framework mit sich bringt. Dynamische Inhalte können abhängig von
der Zeitposition eines Videos angezeigt werden. Ein Beispiel:

    <html><head>
    <script src="http://popcornjs.org/code/dist/popcorn-complete.js"></script>
    <script>
    document.addEventListener("DOMContentLoaded", function() {

    var popcorn = Popcorn("#video");

    popcorn.footnote({
            start: 0,
            end: 3,
            target: "footnote",
            text: "Hallo Welt"
           })
    .footnote({
            start: 3,
            end: 6,
            target: "footnote",
            text: "popcorn.js"
    });

    popcorn.play();
    popcorn.volume(0); // 0 .. 1.0

    }, false );
    </script>
    </head>
    <body>
        <video height="800" width="600" id="video" src="o.ogv" controls="true" preload="none"></video>
        <h1><div id="footnote"></div></h1>
    </body>
    </html>

In Zeile 2 wird das popcorn.js Framework geladen. Durch das Attribut src
im Video-Tag (Zeile 28) wird die Videodatei festgelegt und per Attribut
id wird die einmalige Identifikationszeichenkette bestimmt. Neben dem
Video-Tag gibt es ebenso einen div-Container (Zeile 29) mit der id
footnote. Mittels Funktion
`document.addEventListener("DOMContentLoaded", function() { }, false);`
in Zeile 4 wird sichergestellt dass die Seite vollständig geladen wird
bevor die Javascript-Anweisungen ausgeführt werden. Anhand des Befehls
`var popcorn = Popcorn("#video");` in Zeile 6 wird eine neue
Popcorn-Instanz bezüglich der Video-Tag id video erstellt. Das Plugin
footnote macht es möglich dass Text (Fussnoten) zu einem Element auf der
Website hinzugefügt wird und kommt in Zeile 8 und 14 zum Einsatz. Von
Sekunde 0 bis 3 wird der Text "Hallo Welt" im div-Container mit der id
footnote angezeigt. Von Sekunden 3 bis 6 wird der Text "popcorn.js"
ebenso im div-Container mit der id footnote angezeigt. Durch den Befehl
`popcorn.play();` in Zeile 21 wird das Video abgespielt.
`popcorn.volume(0);` in Zeile 22 setzt die Lautstärke auf 0.

  [popcorn.js]: http://popcornjs.org/ "popcornjs"
  [HTML5]: https://de.wikipedia.org/wiki/HTML5 "WP:HTML5"
  [Mozilla]: https://de.wikipedia.org/wiki/Mozilla "WP:Mozilla"
  [mozillapopcorn.js]: http://mozillapopcorn.js "popcorn Project"
  [popcornjs.org]: http://popcornjs.org/ "popcorn.js"
