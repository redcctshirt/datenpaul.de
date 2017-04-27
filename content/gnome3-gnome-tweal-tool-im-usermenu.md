Title: Gnome3 - gnome-tweal-tool im userMenu
Date: 2012-07-11 23:15
Author: heiko
Category: Gnome
Tags: Fedora, Gnome, gnome-tweak-tool, Gnome3, Javascript, Linux, Programmierung, userMenu, userMenu.js
Slug: gnome3-gnome-tweal-tool-im-usermenu

Das [gnome-tweak-tool][] ist ein erweitertes Einstellungstool für
[Gnome3][]. Es gehört oft nicht zum Standard der meist genutzten
Linux-Distributionen, muss bei Bedarf also über den herkömmlichen
Paketmanager nachinstalliert werden. (Beispiel für Fedora:
`su -c "yum install gnome-tweak-tool`") Um sich leichten Zugang zum
gnome-tweak-tool zu verschaffen ist es möglich das userMenu zu
erweitern. Der einfachste Weg führt dabei über die [Gnome3-Extension][]
"Advanced Settings in UserMenu" auf der Website
<https://extensions.gnome.org/extension/130/advanced-settings-in-usermenu/>.
Ebenso ist es machbar die userMenu.js-Datei im Verzeichnis
/usr/share/gnome-shell/js/ui zu modifizieren. Nach der Bearbeitung wird
die Veränderung durch einen Gnome-Shell-Neustart, mittels Alt+F2 r,
wirksam. Die Modifikationen können durch einen Texteditor erfolgen.
(z.B. bei Fedora:
`su -c "nano /usr/share/gnome-shell/js/ui/userMenu.js"`) Folgende Zeilen
kommen hinzu: (647-649 und 717-721)

/usr/share/gnome-shell/js/ui/userMenu.js

    item = new PopupMenu.PopupMenuItem(_("System Settings"));
    item.connect('activate', Lang.bind(this, this._onPreferencesActivate));
    this.menu.addMenuItem(item);

    item = new PopupMenu.PopupMenuItem(_("Gnome-Tweak-Tool"));
    item.connect('activate', Lang.bind(this, this._onGnometweaktoolActivate));
    this.menu.addMenuItem(item);

    item = new PopupMenu.PopupSeparatorMenuItem();
    this.menu.addMenuItem(item);


    _onPreferencesActivate: function() {
        Main.overview.hide();
        let app = Shell.AppSystem.get_default().lookup_app('gnome-control-center.desktop');
        app.activate();
    },

   _onGnometweaktoolActivate: function() {
    Main.overview.hide();
    let app = Shell.AppSystem.get_default().lookup_app('gnome-tweak-tool.desktop');
        app.activate();
    },

    _onLockScreenActivate: function() {
        Main.overview.hide();
        this._screenSaverProxy.LockRemote();
    },

![Screenshot: Gnome3 userMenu mit gnome-tweak-tool-Eintrag][]

  [gnome-tweak-tool]: https://live.gnome.org/GnomeTweakTool/
    "gnome-tweak-tool"
  [Gnome3]: https://de.wikipedia.org/wiki/Gnome "WP:Gnome"
  [Gnome3-Extension]: https://extensions.gnome.org
    "extensions.gnome.org"
  [Screenshot: Gnome3 userMenu mit gnome-tweak-tool-Eintrag]: http://www.datenpaul.de/archive/gtt_userMenu.png
