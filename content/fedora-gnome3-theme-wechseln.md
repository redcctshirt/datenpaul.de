Title: Fedora - Gnome3 - Theme wechseln
Date: 2011-07-30 22:53
Author: heiko
Category: Gnome
Tags: Fedora, Gnome, gnome-tweak-tool, Gnome3, Linux, Theme
Slug: fedora-gnome3-theme-wechseln

Hier möchte ich kurz und knapp erklären wie man [Gnome3][] ein neues
Erscheinungsbild spendieren kann, sprich wie man das Design ändert. Hat
man erst mal den Installationsbefehl
`su -c "yum install gnome-shell-extension-theme-selector"` ausgeführt,
ist die Hälfte der Arbeit schon getan. Die beiden Pakete
gnome-shell-extensions-common und gnome-shell-extensions-user-theme
werden ebenso installiert. Die Installation ist übrigens ebenfalls
mittels gpk-application machbar. Ein Gnome-Shell-Neustart per Alt+F2 r
aktiviert die 3 neuen Erweiterungen und macht sie im
[gnome-tweak-tool][] sichtbar. Falls gnome-tweak-tool noch nicht im
System verfügbar ist, wird die Nachinstallation durch
`su -c "yum install gnome-tweak-tool"` gestartet.

Nun sucht man sich ein Theme im Internet und lädt es herunter. (Quellen:
<http://gnome-shell.deviantart.com/gallery/28081982>,
<http://gnome-look.org/>) Im gnome-tweak-tool unter Shell installiert
man das Theme jetzt. Man klickt auf den Button (keine), wählt das
heruntergeladene Theme-Paket, klickt auf den Button Öffnen, und das
Theme ist installiert. Abschließend ist nochmal ein Gnome-Shell-Neustart
per Alt+F2 r erforderlich. Die Themes findet man im übrigen im
Persönlichen Ordner, im versteckten Verzeichnis .themes wieder.

Anhand des gnome-tweak-tools, unter Shell, neben den schon benutzten
Button (keine), ist man nunmehr im Stande das Theme zu wechseln.
Andernfalls geht man auf Aktivitäten, klickt auf Themes, neben Fenster
und Anwendungen, und ist in der Lage ein neues Erscheinungsbild (Theme)
zu bestimmen.

  [Gnome3]: http://de.wikipedia.org/wiki/Gnome "WP:Gnome"
  [gnome-tweak-tool]: https://live.gnome.org/GnomeTweakTool
    "gnome-tweak-tool"
