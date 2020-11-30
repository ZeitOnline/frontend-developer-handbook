# Jinja Template Filter und Checks

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


## Context Filter

Sogenannte Context Filter sind eine spezielle Form der Filter, bei denen der aktuelle "Context" zur Verfügung steht.

Bei der Benutzung in Jinja wird, wie in normalen Filtern nur ein Wert (hier die URL) hineingereicht:

```
{{ teaser_url | append_campaign_params }}
```

Der Filter selbst nimmt zwei Parameter entgegen (`context` und `url`): Das funktioniert, weil bei Context Filtern der Context automatisch als erstes Argument in den Filter gegeben wird. Man muss das nicht selbst aus dem Template heraus machen.

```python
@zeit.web.register_ctxfilter
def append_campaign_params(context, url):
  ...
```

Was ist der Context?

Die Klassendefinition habe ich leider nicht gefunden. Lapidar gesagt: es ist ein Objekt, das Informationen über die aktuelle Umgebung bereitstellt. Im Falle eines Teasers beinhaltet es Dinge wie die `module_loop`, `area_loop` und die aktuelle `view`, aber auch den `request`, `toggles` und `settings`, sowie Hilfsfunktionen wie `get_image` und `get_svg_from_file`.


## Jinja Template Tests

Template Tests (oder "Template Checks") in Jinja funktionieren im Prinzip wie Filter. Der Unterschied: Tests geben nur den Boolean Wert True/false zurück, un werden entsprechend genutzt. 

```python
@zeit.web.register_test
def topicpage(context):
    return getattr(context, 'type', None) in ['autotopic', 'manualtopic']
```

Im Template kann die Abfrage dann in recht natürlicher Sprache erfolgen:

```
{% if view.context is topicpage %}
```
