# Frontend Tech Stack bei ZEIT ONLINE

## Jinja
Unsere HTML Code schreiben wir als Template-Code mit der Template Engine [Jinja](https://palletsprojects.com/p/jinja/). Unseren Template Code halten wir, dort wo möglich, simpel und leicht verständlich durch die strukturelle Aufteilung der Templates in Komponenten.

## Sass
Wir verwenden [Sass](https://sass-lang.com/) als Präprozessor. Die Verwendung von Variablen, Mixins und Funktionen hat sich für uns als hilfreich herausgestellt.
Kürzlich haben wir von [node-sass](https://github.com/sass/node-sass) zu [Dart Sass](https://sass-lang.com/dart-sass) gewechselt, da wir so die neuesten Sass Features nutzen können.
Mehr zu der Art und Weise wie wir unseren Sass Code schreiben ist in unseren [Sass Guidelines](../sass/guidelines.md) notiert.

## Postcss
Der von Sass verarbeitete Code wird nochmal von Postcss an unseren Browsersupport angepasst.

## Javascript @ ZON
Unser Javascript Code wird durch einige Polyfills unterstützt.
Außerdem ermöglicht [Babel](https://babeljs.io/) uns das schreiben von Code der noch nicht in allen von uns unterstützten Browsern läuft.
Dadurch können wir unseren Code in schöner es5/6 Syntax schreiben und einen Großteil der neuesten Funktionen verwenden.

Als Module Bundler setzen wir [Webpack](https://webpack.js.org/) ein.

2020 haben wir es geschafft unsere Codebase in plain js umzuschreiben, sodass wir seitdem jQuery nur noch bei Bedarf externe Module laden.

## Browsersupport
Vor kurzem konnten wir unseren Browsersupport anpassen, sodass wir den Internet Explorer 10 nun nicht mehr offiziell unterstützen.

Der aktuelle Browsersupport ist:
```
"Chrome >= 35",
"Firefox >= 30",
"Edge >= 12",
"Explorer >= 11",
"iOS >= 7",
"Safari >= 8",
"Android >= 4",
"Opera >= 12"
```

Dennoch arbeiten wir nach dem Prinzip des Progressive-Enhancements, wodurch sich die Seite in so ziemlich jedem Browser ohne Probleme bedienen lassen sollte.
