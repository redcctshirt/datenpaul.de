Title: Tutorial: LibreOffice Writer - Erste Schritte mit regulären Ausdrücken
Date: 2013-06-28 03:28
Author: admin
Category: LibreOffice
Tags: Daten, Datenjournalismus, LibreOffice, Linux, RegEx, Regulärer Ausdruck, Writer
Slug: tutorial-libreoffice-writer-erste-schritte-mit-regularen-ausdrucken

Reguläre Ausdrücke  (regular expressions, RegExp, RegEx, Grep, …)

Viele Aufgaben eines/r Datenjournalist/in kann man mit "Suchen und
Ersetzen" lösen, z.B. in LibreOffice Writer. Für komplexere "Suchen und
Ersetzen" gibt es die sogenannten "regulären Ausdrücke". Diese werden
von vielen einfachen Texteditoren unterstützt. Wie man mit "Suchen und
Ersetzen" einen Text bereinigen kann, werde ich nun an einem Beispiel
demonstrieren. Dafür habe ich eine Liste gewählt, in der alle
Leerzeichen fehlen. Dieses Phänomen tritt in der Arbeit öfters auf, z.B.
weil der Text mit einer OCR-Software (Bild-zu-Text-Erkennung) erstellt
oder aus einem PDF-Dokument kopiert wurde. Hier ein Beispiel: die Liste
der ehemaligen Bundespräsidenten der BRD kopiert von der [entsprechenden
Wikipedia Seite][].

TheodorHeuss(1884–1963)  
HeinrichLübke(1894–1972)  
GustavHeinemann(1899–1976)  
WalterScheel(\*1919)  
KarlCarstens(1914–1992)  
RichardvonWeizsäcker(\*1920)  
RomanHerzog(\*1934)  
JohannesRau(1931–2006)  
HorstKöhler(\*1943)  
ChristianWulff(\*1959)  
JoachimGauck(\*1940)

Als erstes kann man alle "(" ersetzen durch ein Tab, dass von
LibreOffice Calc als Spaltenwechsel interpretiert wird.

In Writer: ersetze "\\(" durch "\\t" (Unter Bearbeiten - Suchen und
Ersetzen - Suchen nach "\\(" - Ersetzen durch "\\t" - Unter Mehr
Optionen - Regulärer Ausdruck anklicken)

TheodorHeuss 1884–1963)  
HeinrichLübke 1894–1972)  
GustavHeinemann 1899–1976)  
WalterScheel \*1919)  
KarlCarstens 1914–1992)  
RichardvonWeizsäcker \*1920)  
RomanHerzog \*1934)  
JohannesRau 1931–2006)  
HorstKöhler \*1943)  
ChristianWulff \*1959)  
JoachimGauck \*1940

Nun die schließenden Klammern entfernen.

In Writer: ersetze ")" durch "" (Unter Bearbeiten - Suchen und Ersetzen
- Suchen nach "\\)" - Ersetzen durch "" - Unter Mehr Optionen -
Regulärer Ausdruck anklicken)

TheodorHeuss 1884–1963  
HeinrichLübke 1894–1972  
GustavHeinemann 1899–1976  
WalterScheel \*1919  
KarlCarstens 1914–1992  
RichardvonWeizsäcker \*1920  
RomanHerzog \*1934  
JohannesRau 1931–2006  
HorstKöhler \*1943  
ChristianWulff \*1959  
JoachimGauck \*1940

Nun die Minuszeichen durch einen Tab ersetzen.

In Writer: ersetze "–" durch "\\t" (Unter Bearbeiten - Suchen und
Ersetzen - Suchen nach "–" - Ersetzen durch "\\t" - Unter Mehr Optionen
- Regulärer Ausdruck anklicken)

TheodorHeuss 1884 1963  
HeinrichLübke 1894 1972  
GustavHeinemann 1899 1976  
WalterScheel \*1919  
KarlCarstens 1914 1992  
RichardvonWeizsäcker \*1920  
RomanHerzog \*1934  
JohannesRau 1931 2006  
HorstKöhler \*1943  
ChristianWulff \*1959  
JoachimGauck \*1940

Nun die Mal-Zeichen entfernen.

In Writer: ersetze "\*" durch "" (Unter Bearbeiten - Suchen und Ersetzen
- Suchen nach "\\\*" - Ersetzen durch "" - Unter Mehr Optionen -
Regulärer Ausdruck anklicken)

TheodorHeuss 1884 1963  
HeinrichLübke 1894 1972  
GustavHeinemann 1899 1976  
WalterScheel 1919  
KarlCarstens 1914 1992  
RichardvonWeizsäcker 1920  
RomanHerzog 1934  
JohannesRau 1931 2006  
HorstKöhler 1943  
ChristianWulff 1959  
JoachimGauck 1940

Die Daten sind nun schon sehr gut strukturiert, aber die Namen sind noch
nicht korrekt. Vor- und Nachnamen kleben noch aneinander. Man müsste
nach jeden Kleinbuchstaben, auf den ein Großbuchstabe folgt, ein
Leerzeichen setzen. Solch eine Aufgabe lässt sich nicht mehr mit einem
einfachen "Suchen und Ersetzen" lösen. Theoretisch müsste man jede
Kombination von Klein- und Großbuchstaben suchen.

Als regulärer Ausdruck: ersetze "([a-z])([A-Z])" durch "\\1 \\2" (Unter
Bearbeiten - Suchen und Ersetzen - Suchen nach "([a-z])([A-Z])" -
Ersetzen durch "\$1 \$2" - Unter Mehr Optionen - Regulärer Ausdruck
anklicken, Groß-/Kleinschreibung anklicken)

Theodor Heuss 1884 1963  
Heinrich Lübke 1894 1972  
Gustav Heinemann 1899 1976  
Walter Scheel 1919  
Karl Carstens 1914 1992  
Richardvon Weizsäcker 1920  
Roman Herzog 1934  
Johannes Rau 1931 2006  
Horst Köhler 1943  
Christian Wulff 1959  
Joachim Gauck 1940

Durch den oben verwendeten regulären Ausdruck werden beliebige
Kombinationen aus Klein- und Großbuchstaben gefunden: ([a-z])([A-Z]) -
ein beliebiger Kleinbuchstabe (1. Teil in Klammern), ein beliebiger
Großbuchstabe (2. Teil in Klammern)

Wenn etwas gefunden wird, wird es ersetzt durch: \\1 \\2 (In Writer
durch \$1 \$2)  
Was im 1. Teil in Klammern gefunden wurde. Leerzeichen. Was im 2. Teil
in Klammern gefunden wurde.

Reguläre Ausdrücke sind scheinbar kompliziert, aber auch hier ist alles
eine Frage der Übung! Wenn man einmal damit anfängt, hat man schnell die
ersten Erfolgserlebnisse und lernt dann kontinuierlich weitere Tricks
dazu. Aber den ersten Schritt muss man erst einmal machen, und zwar
einfach mal nach "Regulären Ausdrücken" googeln und sich die vielen
Einführungskurse anschauen.

([Quelltext][] ist von Michael Kreil und steht unter einer Creative
Commons-Lizenz (CC BY 3.0 Michael Kreil))

  [entsprechenden Wikipedia Seite]: http://de.wikipedia.org/wiki/Bundespr%C3%A4sident_(Deutschland)#Die_bisherigen_Bundespr.C3.A4sidenten_der_Bundesrepublik_Deutschland
    "WP:Bundespräsidenten"
  [Quelltext]: http://www.opendatacity.de/tutorial-erste-schritte-mit-regularen-ausdrucken/
    "Tutorial: Erste Schritte mit regulären Ausdrücken"
