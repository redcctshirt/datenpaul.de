Title: farbige Vierecke im Video anzeigen lassen
Date: 2011-08-27 23:45
Author: heiko
Category: Videobearbeitung
Tags: Fedora, ffmpeg, Linux, Videobearbeitung
Slug: farbige-vierecke-im-video-anzeigen-lassen

Mit [ffmpeg][], dem Videofilter overlay und der Videoquelle color ist es
möglich farbige Vierecke ins Video zu zaubern. Der [Videofilter
overlay][] sollte inzwischen bekannt sein. Auch bei diesem Beispiel
lasse ich alle unnötigen Optionen einfach weg.

Hilfreiche Daten für das Beispiel:  
Input-Videodatei: a.ogv  
Output-Videodatei: b.webm  
Videogröße: 1280×720 (Breite: 1280 Pixel, Höhe: 720 Pixel)

Mit folgendem Muster erstellt man eine Farbquelle:  
"color=Farbe:Framegröße:Framerate" (Farbe: 0xRRGGBB[AA] oder def.
Farbe,  
z.B. "color=red@1.0:100x200:25")

Beispiele:

`ffmpeg -i a.ogv -vf "color=red@0.3:100x200:25 [color]; [in][color] overlay [out]" b.webm # durchsichtiges rotes Viereck (Breite: 100 Pixel, Höhe: 200 Pixel) an der Stelle 0:0 im Video`

ffmpeg -i a.ogv -vf "color=blue@1.0:200x100:25 [color]; [in][color]
overlay=100:100 [out]" b.webm  
\# blaues Viereck (Breite: 200 Pixel, Höhe: 100 Pixel) an der Stelle
100:100 im Video

ffmpeg -i a.ogv -vf "color=blue@1.0:200x100:25 [color1];
color=red@0.2:100x100:25 [color2] [in][color1] overlay=100:100
[in+color1]; [in+color1][color2] overlay=500:100 [out]" b.webm  
\# 2 Vierecke

ffmpeg -i a.ogv -vf "movie=logo.png [logo]; color=red@0.2:100x100:25
[color]; [in][color] overlay=10:10 [in+color]; [in+color][logo]
overlay=10:10 [out]" b.webm  
\# Logo + Viereck</code>

  [ffmpeg]: http://de.wikipedia.org/wiki/Ffmpeg "Link zu WP:ffmpeg"
  [Videofilter overlay]: http://www.datenpaul.de/archives/121
    "Link zu overlay-Artikel"
