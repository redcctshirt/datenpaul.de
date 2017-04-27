Title: Informationen über ein vimeo-Video ermitteln
Date: 2013-04-13 00:04
Author: heiko
Category: Programmierung
Tags: API, json, Meta, PHP, Programmierung, Python, video, vimeo, xml
Slug: informationen-uber-ein-vimeo-video-ermitteln

Um Meta-Daten (wie z.B. Titel, Dauer usw.) über ein bestimmtes Video vom
vimeo-Video-Portal zu beziehen wird die vimeo data API angeboten. Die
Funktionsweise ist die gleiche wie beim [Auslesen von Informationen über
ein Youtube-Video][]. Eine sehr sorgfältige und leicht verständliche
Dokumentation mit Beispielen entdeckt man auf der Website
<http://developer.vimeo.com/apis/simple> Tippt man folgendes in den
Browser ein, werden die Metadaten vom jeweiligen Video geliefert. (Das
Video wird mittels ID bestimmt. Die Video-ID steht in der URL eines
Video-Aufrufs nach dem / https://vimeo.com/\<ID\>)

Browser-Eingabe: `http://vimeo.com/api/v2/video/<ID>.<Format>`

Mögliche Formate: `json, php, xml`

Beispiel: `http://vimeo.com/api/v2/video/52387087.json`

Mittels Skript können gewünschte Daten nun mühelos ermittelt werden. In
PHP könnte dies so aussehen:

    $id = "52387087";
    $url = "http://vimeo.com/api/v2/video/". $id .".json";
    $j = json_decode(file_get_contents($url));

    foreach($j[0] as $key => $value) {
       echo $key . ": " . $value . "n<br />";
    }

In Python könnte ein Skript so aussehen:

    import urllib2
    import simplejson

    videoid = "52387087"
    url = "http://vimeo.com/api/v2/video/" + videoid + ".json"
    handle = urllib2.urlopen(url)
    content = handle.read()
    j = simplejson.loads(content)

    for key in j[0]:
        print "{0}: {1}".format(key,j[0][key])

  [Auslesen von Informationen über ein Youtube-Video]: http://www.cc-juno.de/archives/364
    "Informationen über ein Youtube-Video auslesen"
