Title: Informationen über ein Youtube-Video auslesen
Date: 2013-04-07 00:13
Author: heiko
Category: Programmierung
Tags: API, json, PHP, Programmierung, Python, web, www, youtube
Slug: informationen-uber-ein-youtube-video-auslesen

Um Meta-Daten (z.B. Anzahl der Likes, Anzahl der Kommentare oder Titel)
über ein Youtube-Video zu bekommen nutzt man ganz einfach die Youtube
data API. Gibt man folgendes in den Browser ein, sendet die API
Informationen zum angegebenen Video im JSON-Format. (Das Video wird
mittels ID bestimmt. Die Video-ID steht in der URL eines Video-Aufrufs
nach dem watch?v= https://www.youtube.com/watch?v=\<ID\>)

Browser-Eingabe:
`http://gdata.youtube.com/feeds/api/videos/<ID>?v=2&alt=jsonc`

Für eine bessere Übersicht sorgt der URL-Anhang `&prettyprint=true`.

Eingabe:
`http://gdata.youtube.com/feeds/api/videos/<ID>?v=2&alt=jsonc&prettyprint=true`

Die Ausgabe, die von der API erzeugt wird, ist nichts weiter als ein
String (Zeichenkette) der dekodiert werden muss. In PHP könnte dies so
aussehen:

    // <ID> wird durch die Youtube-Video-ID ersetzt
    $j = json_decode(file_get_contents("http://gdata.youtube.com/feeds/api/videos/<ID>?v=2&alt=jsonc"));
    // Einzelne Angaben können nun mit diesem Muster ausgegeben werden
    echo "Video-Title: " . $j->data->title;

In Python könnte dies so aussehen:

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    import urllib2
    import simplejson

    # <ID> wird durch die Youtube-Video-ID ersetzt
    handle = urllib2.urlopen("http://gdata.youtube.com/feeds/api/videos/<ID>?v=2&alt=jsonc")
    content = handle.read()
    j = simplejson.loads(content)

    print "Titel: {0}".format(j["data"]["title"])
    print "Aufrufe: {0}".format(j["data"]["viewCount"])

