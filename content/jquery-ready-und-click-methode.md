Title: jQuery - ready- und click-Methode
Date: 2012-07-05 22:41
Author: heiko
Category: jQuery
Tags: HMTL5, HTML, Javascript, jQuery, web, www
Slug: jquery-ready-und-click-methode

Die ready-Methode sorgt dafür dass bei dem Ereignis (Event), wenn das
ganze Dokument vollständig geladen wurde, die Funktion innerhalb der
Klammern, in diesem Fall eine anonyme Funktion, ausgeführt wird. Diese
Anweisung kann ruhig mehrmals in einer Datei stehen. Die click-Methode
hingegen verwirklicht die angegebene Funktion bei einem Mausklick. Durch
.hide() versteckt man die selektierten Elemente.

    <!DOCTYPE html>
    <html>
    <head>
    <style>
    div { font-size: 5em; color: red; cursor: pointer; }
    </style>
    <script src="http://code.jquery.com/jquery-1.7.2.min.js"></script>
    </head>
    <body>

    <div>Hallo Welt</div>
    <div>jQuery</div>

    <script>
    $(document).ready(function() {
      $("div").click(function() {
        $(this).hide();
    });
    });
    </script>
    </body>
    </html>

In Zeile 7 wird das jQuery-Framework geladen. Von Zeile 14 bis 20 werden
die jQuery-Anweisungen definiert. Sobald das ganze Dokument vollständig
geladen wurde steht die click-Methode für alle div-Container bereit.
\$(this) bezieht sich auf das jeweile Element (hier ein div-Container)
auf das gerade geklickt wird. Durch die hide-Methode in der 17. Zeile
wird das Element bei einem Mausklick versteckt.
