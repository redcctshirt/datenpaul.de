Title: PDF-Seiten in Bilder umwandeln
Date: 2012-05-31 22:05
Author: heiko
Category: Linux
Tags: Fedora, Linux, pdf, pdfimages, pdftocairo, pdftoppm
Slug: pdf-seiten-in-bilder-umwandeln

In diesem Artikel möchte ich 3 Tools vorstellen. Das Tool `pdftoppm`
verwandelt Seiten von einem [PDF-Dokument][] in Bilder. Mögliche
Optionen werden nach der Eingabe `pdftoppm --help` aufgelistet.
`pdftoppm dateiname.pdf dateiname` konvertiert jede Seite zu einem
[ppm-Bild][]. Mittels Option -png können [PNG-Bilder][] erstellt werden.
Per -jpeg kommt es zur Ausgabe von JPG-Bildern. Außerdem existiert das
Tool `pdftocairo`, mit ähnlichen Funktionen. Durch den Befehl
`pdftocairo --help` werden alle Optionen sichtbar.
`pdftocairo dateiname.pdf -png dateiname` generiert PNG-Bilder. Ebenso
gibt es noch die Schaffungsoptionen -jpeg, -ps, -pdf und -svg. Durch das
Tool `pdfimages` können Bilder innerhalb einer PDF-Datei extrahiert
werden. `pdfimages dateiname.pdf dateiname` ist das Muster für die
Ausführung des Kommandos. Anhand der Optionen -f und -l kann übrigens
bei allen 3 Tools eine Selektion durchgeführt werden. (-f n - bestimmt
die erste Seite für die Ausgabe, -l n - bestimmt die letzte Seite für
die Ausgabe)

  [PDF-Dokument]: https://de.wikipedia.org/wiki/Pdf "WP:PDF"
  [ppm-Bild]: https://de.wikipedia.org/wiki/Portable_Pixmap "WP:PPM"
  [PNG-Bilder]: https://de.wikipedia.org/wiki/Portable_Network_Graphics
    "WP:PNG"
