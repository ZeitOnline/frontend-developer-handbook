# Jinja Template Filter

Mit [Template Filtern](https://jinja.palletsprojects.com/en/2.11.x/templates/#filters) ist es uns möglich Python Code auszuführen und das Ergebnis im Template auszugeben.

Diese Template Filter definieren wir in der Datei `zeit/web/core/template.py`


## Wie definiere ich einen neuen Template Filter?

Ein Template Filter wird durch das Anlegen einer neuen Funktion in der Datei `zeit/web/core/template.py` definiert.
Diese benötigt den `@zeit.web.register_filter` Decorator.

Hier ein Beispiel:

```python
@zeit.web.register_filter
def multiply_by_two(number):
  return number * 2
```


## Wie kann ich meinen Template Filter testen?

Es ist gewünscht, dass jeder selbstgeschriebene Template Filter ebenfalls durch Tests überprüft wird.
Die Tests für unsere Template Filter befinden sich in `zeit/web/core/test/test_template.py`.

Hier ein Beispiel:

```python
def test_filter_multiply_by_two_should_not_throw_exception(application):
  assert zeit.web.core.template.multiply_by_two(2) == 4
  assert zeit.web.core.template.multiply_by_two('foo) == 'foofoo'
  assert zeit.web.core.template.multiply_by_two(1.5) == 3
```


## Wie verwende ich meinen Template Filter?

Der neu geschriebene Template Filter lässt sich nun im Template verwenden

Beispiel:

```html
{{ 2 | multiply_by_two }}
```

sollte als Ausgabe
```
4
```
erzeugen.

