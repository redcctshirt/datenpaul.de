Title: Ruby - Hallo Welt
Date: 2012-05-23 18:57
Author: heiko
Category: Ruby
Tags: Fedora, Gnome, Linux, Programmierung, Ruby, Shebang
Slug: ruby-hallo-welt

[Ruby][]-Quelltextdateien erkennt man an der Endung .rb und können mit
einfachen Texteditoren verändert bzw. überhaupt erst erstellt werden.
Eine .rb-Datei öffnet man mit einem Doppelklick, so wird die Datei mit
dem Standard-Texteditor (z.B. [gedit][]) geöffnet.

    puts "Hallo Welt"

sorgt für die Ausgabe Hallo Welt.

    print "Hallo Welt"

ist ebensfalls eine Ausgabe-Anweisung. Durch `ruby datei.rb` werden die
Befehle in der Datei durch den Ruby-Interpreter ausgeführt. Die
[Shebang][]-Zeile,

    #!/usr/bin/env ruby
    puts "Hallo Welt"
    print "Hallo Welt"

ganz oben, und das Zugriffsrecht "Datei als Programm ausführen"
(`chmod +x datei.rb`) machen die Datei ausführbar. Diese kann nun
mittels `./datei.rb` ausgeführt werden.

  [Ruby]: https://de.wikipedia.org/wiki/Ruby_%28Programmiersprache%29
    "WP:Ruby"
  [gedit]: https://de.wikipedia.org/wiki/Gedit "WP:gedit"
  [Shebang]: https://de.wikipedia.org/wiki/Shebang "WP:Shebang"
