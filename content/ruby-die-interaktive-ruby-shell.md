Title: Ruby - die interaktive Ruby Shell
Date: 2012-05-23 18:43
Author: heiko
Category: Ruby
Tags: Fedora, Gnome, Gnome3, Linux, Programmierung, Ruby
Slug: ruby-die-interaktive-ruby-shell

[Ruby][] ist eine [objektorientierte][] Interpretersprache die 1995 von
einem Japaner veröffentlicht wurde. Sie ist meistens bei allen großen
[Linux-Distributionen][] vorinstalliert. Bei [Fedora][] ist das nicht
der Fall. Mittels Befehl `su -c "yum install ruby ruby-irb"` müssen die
Pakete nachinstalliert werden. Ruby besitzt eine interaktive Ruby-Shell
in der eine Eingabe sofort ausgeführt wird und ein Ergebnis ausgegeben
wird. Mittels `irb` wird die interaktive Ruby-Shell gestartet und es
folgt eine Eingabeaufforderung. Ruby-Kommandos können nun ausprobiert
werden. Durch den Befehl `puts "Hallo Welt"` kommt es zur Ausgabe Hallo
Welt. Die Zeilennummer und die Blockebene werden angezeigt.
`irb(main):<Zeilennr>:<Blockebene>>`. Per quit oder exit kann man die
interaktive Ruby-Shell wieder verlassen. Weitere Optionen werden durch
`irb --help` sichtbar. Die Option `--simple-prompt` unterdrückt die
Zeilennummer- und Blockzifferanzeige. Auf der Website [tryruby.org][]
kann Ruby ebenso, auch ohne Installation, ausprobiert werden.

  [Ruby]: https://de.wikipedia.org/wiki/Ruby_%28Programmiersprache%29
    "WP:Ruby"
  [objektorientierte]: https://de.wikipedia.org/wiki/Objektorientierte_Programmierung
    "WP:OOP"
  [Linux-Distributionen]: https://de.wikipedia.org/wiki/Linux-Distribution
    "WP:Linux-Distribution"
  [Fedora]: https://de.wikipedia.org/wiki/Fedora_%28Linux-Distribution%29
    "WP:Fedora"
  [tryruby.org]: http://www.tryruby.org "try ruby"
