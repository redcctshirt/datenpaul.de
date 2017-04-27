Title: jQuery - $()-Aufruf deaktivieren
Date: 2012-06-02 23:57
Author: heiko
Category: jQuery
Tags: HTML, HTML5, Javascript, jQuery, Programmierung, World Wide Web, www
Slug: jquery-aufruf-deaktivieren

Es ist völlig egal ob man z.B. \$("div").css("color","blue") oder
jQuery("div").css("color","blue") als jQuery-Anweisung schreibt, beides
funktioniert. Aber es ist machbar die \$()-Funktion zu deaktivieren um
möglichen Konflikten mit anderen Javascript-Frameworks entgegenzuwirken.
Mittels jQuery.noConflict(); wird der \$()-Aufruf unwirksam. Beispiel.
(Die Anweisung in Zeile 3 wird somit ignoriert.)

    jQuery.noConflict();
    jQuery(document).ready(function() {
    $("div#two").css("color","green");
    jQuery("div#one").css("color","blue");
    });

