Title: Videobilder spiegeln
Date: 2011-12-02 16:23
Author: heiko
Category: Videobearbeitung
Tags: ffmpeg, hflip, Linux, vflip, Videobearbeitung, Videofilter
Slug: videobilder-spiegeln

Das Tool [ffmpeg][] macht es möglich. Der Videofilter hflip spiegelt die
Videobilder  
horizontal und der Videofilter vflip spiegelt sie vertikal. Unnötige
Optionen  
und Paramenter lasse ich bei diesen Beispielen weg.

Beispiele:  

` ffmpeg -i a.ogv -vf "vflip" b.webm # Den Videoinput a.ogv vertikal spiegeln, Ergebnis: b.webm`

ffmpeg -i a.ogv -vf "hflip" b.webm  
\# Den Videoinput a.ogv horizontal spiegeln, Ergebnis: b.webm</code>

  [ffmpeg]: http://de.wikipedia.org/wiki/Ffmpeg "ffmpeg"
