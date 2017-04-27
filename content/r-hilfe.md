Title: R - Hilfe
Date: 2014-06-22 16:30
Author: heiko
Category: R
Tags: Linux, Linux Mint, R, Programmierung, Statistik
Slug: r-hilfe

![r - hilfe][]

[R](http://www.r-project.org) wird nach der Installation mittels R [ENTER] in der Kommandozeile gestartet.
Der schnellste Weg um flott zu einer Funktionsbeschreibung zu kommen, die vielleicht helfen kann, ist über das Fragezeichen (?) am Anfang vor einer Funktion. So könnte man z.B. eingeben
	
    ?license

wenn man mehr über die Funktion license() erfahren möchte. Die Anzeige kann man mit der Taste q beenden.
Durch help erreicht man das Gleiche, man gibt help ein und anschließend in runden Klammern den Namen der Funktion, z.B.

    help(license)

Apropos sucht speziell nach bestimmten Zeichenketten. Um zum Beispiel nach plot zu suchen tippt man ein

    apropos("plot")

Mittels **help.start()** wird in einem Webbrowser eine Seite geöffnet mit mehreren Links zu R-Anleitungen und Dokumentationen. Unter Zuhilfenahme von RSiteSearch('Suchbegriff') wird in Webseiten über R nach dem angegebenen Begriff gesucht, z.B.

    RSiteSearch('plot')



[1. Bild](http://pixabay.com/de/button-tasten-computer-design-2076/) by [PublicDomainPictures](http://pixabay.com/de/users/PublicDomainPictures/), [CC Zero](https://creativecommons.org/publicdomain/zero/1.0) 

  [r - hilfe]: http://www.datenpaul.de/archive/r-hilfe.jpg

