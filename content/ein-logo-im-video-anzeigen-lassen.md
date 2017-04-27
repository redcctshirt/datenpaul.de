Title: Ein Logo im Video anzeigen lassen
Date: 2011-08-25 21:54
Author: heiko
Category: Videobearbeitung
Tags: Fedora, ffmpeg, Linux, Logo, Videobearbeitung
Slug: ein-logo-im-video-anzeigen-lassen

Mit [ffmpeg][] und dem Videofilter overlay ist man in der Lage ein Logo
ins Video zu zaubern. Um Übersichtlichkeit zu gewährleisten lasse ich
hier bei diesem Beispiel mit ffmpeg alle anderen Optionen die man sonst
so benutzt wie z.B. -b für die [Bitrate][] einfach weg.

Hilfreiche Daten für das Beispiel:  
Input-Videodatei: a.ogv  
Output-Videodatei: b.webm  
Videogröße: 1280x720 (Breite: 1280 Pixel, Höhe: 720 Pixel)  
Bilddatei: logo.png  
Bildgröße: 50x50 (Breite: 50 Pixel, Höhe: 50 Pixel)

Mit folgendem Muster setzt man den Videofilter overlay ein:  
`-vf "movie=bilddatei.png [logo]; [in][logo] overlay=x:y [out]"`

Die Bilddatei mit dem Logo wird durch movie=bilddatei.png [logo]
definiert. Durch overlay=x:y kann man die Stelle angeben wo das Logo
dann erscheinen soll. (z.B. overlay=10:10 - das Logo wird nun oben links
in der Ecke angezeigt)

Einige hilfreiche Variablen die eingesetzt werden können:  
main\_w oder W - für die Breite des Videos (hier 1280)  
main\_h, H - für die Höhe des Videos (hier 720)  
overlay\_w, w - für die Breite des Logos (hier 50)  
overlay\_h, h - für die Höhe des Logos (hier 50)

Beispiele:

`ffmpeg -i a.ogv -vf "movie=logo.png [logo]; [in][logo] overlay=10:10 [out]" b.webm # Logo oben links`

ffmpeg -i a.ogv -vf "movie=logo.png [logo]; [in][logo]
overlay=main\_w-overlay\_w-10:10 [out]" b.webm  
\# Logo oben rechts, mit Zahlen: overlay=1280-50-10:10 -\>
overlay=1220:10

ffmpeg -i a.ogv -vf "movie=logo.png [logo]; [in][logo]
overlay=10:main\_h-overlay\_h-10 [out]" b.webm  
\# Logo unten links, mit Zahlen: overlay=10:720-50-10 -\>
overlay=10:660

ffmpeg -i a.ogv -vf "movie=logo.png [logo]; [in][logo]
overlay=main\_w-overlay\_w-10:main\_h-overlay\_h-10 [out]" b.webm  
\# Logo unten rechts, mit Zahlen: overlay=1280-50-10:720-50-10 -\>
overlay=1220:660

ffmpeg -i a.ogv -vf "movie=logo.png [logo1]; movie=logo2.png [logo2];
[in][logo1] overlay=main\_w-overlay\_w-10:main\_h-overlay\_h-10
[in+logo1]; [in+logo1][logo2] overlay=10:10 [out]" b.webm  
\# 2 Logos  
</code>

  [ffmpeg]: http://de.wikipedia.org/wiki/Ffmpeg "WP:ffmpeg"
  [Bitrate]: http://de.wikipedia.org/wiki/Bitrate "WP:Bitrate"
