Title: Wordpress widget 6 Zufallszahlen von 1 bis 49
Date: 2010-06-23 16:16
Author: heiko
Category: Programmierung
Tags: 6von49, PHP, Programmierung, Widget, Wordpress
Slug: wordpress-widget-6-zufallszahlen-von-1-bis-49

Wordpress widget 6 Zufallszahlen von 1 bis 49  
License: GPLv3  
Version: 0.1 (23.06.2010)  
[Download][]

Prinzip:  

`$numberlist = range(1,49); // Liste erstellen mit Zahlen von 1 bis 49 shuffle($numberlist); // Liste mischen for ($i=0; $i<=5; $i++) { $rand_nr[$i] = $numberlist[$i]; } // ersten 6 Zahlen in eine neue Liste schreiben sort($rand_nr); // die 6 Zufallszahlen sortieren foreach ($rand_nr as $value) { echo "$value "; } // die 6 geordneten Zufallszahlen ausgeben`

  [Download]: http://www.datenpaul.de/archive/six_random_numbers.zip
