Title: Opus - freier Audio-Codec
Date: 2012-09-12 20:59
Author: heiko
Category: Linux
Tags: Audio-Codec, Fedora, Linux, opus, opusdec, opusenc, opusinfo
Slug: opus-freier-audio-codec

[Opus][] ist ein neuer, freier und offener Audio-Codec. Die Bandbreite
reicht von 8kHz bis 48kHz. Für die Speicherung ist eine Bitrate von
6kbit/s bis 510kbit/s möglich. CBR und [VBR][], das heisst konstante und
variable Bitraten werden unterstützt. Er kann sowohl für
[Voice-over-IP,][] als auch für hochwertige Musik verwendet werden.
Weitere Informationen findet man auf der Website [opus-codec.org][]. Um
Opus zu implementieren muss das Paket opus installiert werden. Das Paket
opus-tools enthält die Programme opusenc, opusdec und opusinfo. Die
Installation bei [Fedora][] erfolgt durch den Paketmanager oder mittels
Befehl `su -c "yum install opus opus-tools"`. opusenc wird eingesetzt um
.wav-Dateien in .opus-Dateien umzuwandeln. opusdec hingegen konvertiert
.opus-Dateien in .wav-Dateien. Informationen über .opus-Dateien werden
unter Zuhilfenahme von opusinfo eingeblendet. Mehrere Optionen stehen
für jedes Programm zur Verfügung. Mit Firefox 15 können .opus-Dateien
geöffnet und abgespielt werden. Beispiele für die opus-tools:

`opusinfo --help # Optionen werden aufgelistet`

opusinfo datei.opus \# Informationsanzeige über die Opus-Datei

opusenc --help \# Optionen werden aufgelistet

opusenc --bitrate 224 datei.wav output.opus \# .wav in .opus umwandeln,
mit Bitrate 224000bit/s

opusdec --help \# Optionen werden aufgelistet

opusdec datei.opus output.wav \# .opus in .wav umwandeln</code>

  [Opus]: http://de.wikipedia.org/wiki/Opus_(Audioformat) "WP:Opus"
  [VBR]: http://de.wikipedia.org/wiki/Bitrate#Variable_Bitrate "WP:VBR"
  [Voice-over-IP,]: http://de.wikipedia.org/wiki/Voice_over_IP "WP:VoIP"
  [opus-codec.org]: http://opus-codec.org "opus"
  [Fedora]: http://de.wikipedia.org/wiki/Fedora_(Linux-Distribution)
    "WP:Fedora"
