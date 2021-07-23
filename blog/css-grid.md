# CSS-Grid 

Warum:
- einen Teaserlink für alles, danach übergroße Klickflächen

Motivation: 
- heute guter Browser-Support für css-grid
- veraltetes float-Pattern ablösen (ist ja eigentlich auch ein Hack). 
- Flexbox als Fallback für z.B. IE11 einsetzen.
- Vertical Spacing in Form von Padding aus den Teasern nehmen Stichwort übergoße Teaser-Klickflächen 

Vorgehen:
- Teaser-Spalten/-Aufteilung ermitteln -> Bild Screenshot (Stanard, Duo, Trio etc.)
- Responsive mobil einspaltig desktop mehrspaltig
- Grid-Mixin entwickeln, dass horizontal und vertical
- Verwaltungsaufwand minimieren, indem der Fallback Teil des Mixins wird (IE11, low Edge Unterstützung)
- verticale Abstände der Teaser erhalten, Schwierigkeit: unterschiedliche Abstände pro Teasergruppe/Teaserausprägung

Ergebnis/Vorteil:
- keine ausufernden Klickflächen
- einfacher zu wartende Abstände, weil an einem Ort verwaltet
  - Vertikale Abstände hingen vorher an den Teasern, was zur Folge hat, dass an den vertikalen Teaser-Kannten jeweils die Hälfte des gewünschten Gesamtabstandes drangeschrieben werden musste. Jetzt collapsen die Abstände richtig und können einfacher überblickt werden, da sie an dem Grid hängen.
  - horizontale Abstände wandern als Ganzes an die defnierte Stelle und müssen nicht mehr halbiert werden (cp-padding) 
- Float abgeschafft und modernes Feature eingeführt (das genau dafür da ist!)
- wir folgen stringenter der BEM-Methodologie, da Teaser Blöcke sind und keine Abstände direkt drangeschrieben haben sollten

Peace & Love
