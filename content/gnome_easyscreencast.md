Title: Gnome - einfache Bildschirmaufnahmen mit EasyScreenCast
Date: 2015-06-29 18:58
Author: heiko
Category: Gnome
Tags: Linux, Fedora, Gnome, Easyscreencast, Screencasting
Slug: gnome-easyscreencast

![easyscreencast - options][]

Die Bildschirmaktivitäten in ein Video fließen zu lassen, diese Funktion ist schon von Anfang an
ein Bestandteil der [Gnome-Shell](https://de.wikipedia.org/wiki/Gnome_Shell). Die Tastenkombination **Strg+Alt+Shift+R** startet und beendet die [Aufnahme der Desktopumgebung](https://fedoraproject.org/wiki/ScreenCasting). Der rote Kreis, rechts oben in der Leiste, signalisiert, jetzt gerade läuft eine Aufnahme.
Die Aufnahme dauert mit der Standardeinstellung maximal 30 Sekunden. Die Dauer der Aufnahme kann mittels [**gsettings**](https://developer.gnome.org/gio/stable/gsettings-tool.html) in der Kommandozeile oder mit dem [dconf-editor](https://wiki.ubuntuusers.de/GNOME_Konfiguration/dconf) nach oben geschraubt werden. Die Einstellung dazu findet man unter **org.gnome.settings-daemon.plugins.media-keys max-screencast-length**. Statt 30 Sekunden könnten es z.B. 600 sein, 10 Minuten. Angenehm und einfach sind Aufnahmen mit der Gnome-Shell-Erweiterung [EasyScreenCast](https://extensions.gnome.org/extension/690/easyscreencast/). Diese [Screencasting](https://de.wikipedia.org/wiki/Screencast)-Erweiterung findet man unter den vielen anderen Erweiterungen auf der Webseite [extensions.gnome.org](https://extensions.gnome.org). Für die Installation von EasyScreenCast klickt man auf Off und anschließend auf den Button Installieren, sodass ein On erscheint. 

![easyscreencast][]

Ein Klick auf das Kamerasymbol, oben rechts, und es ist machbar per EasyScreenCast eine Aufnahme zu starten und zu stoppen. Die Aufnahmen landen als [webm](https://de.wikipedia.org/wiki/WebM)-Videodateien im Verzeichnis Videos. Die Einstellungen entdeckt man unter Options. Die Aufnahmen durch EasyScreenCast sind mit dem Video-Codec [VP8](https://de.wikipedia.org/wiki/VP8). Die mittels der Tastenkombination **Strg+Alt+Shift+R** erstellten Screencasts laufen mit dem Nachfolger von VP8, dem Video-Codec [VP9](https://de.wikipedia.org/wiki/VP9).



  [easyscreencast - options]: http://www.datenpaul.de/archive/easyscreencast0.png
  [easyscreencast]: http://www.datenpaul.de/archive/easyscreencast1.png


