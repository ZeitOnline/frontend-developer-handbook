# ZEIT ONLINE Jinja Coding Guidelines

## Indentation

Use 4 spaces to indent HTML tags and template blocks.


## Whitespaces

Use [whitespace control](http://jinja.pocoo.org/docs/templates/#whitespace-control)
to strip whitespaces around or within control structures where needed.

Always pad [control statements](http://jinja.pocoo.org/docs/templates/#list-of-control-structures)
and variables with 1 space before and after their braces::

    HTML+Django
    {% for item in container %}
        <span>{{ item.text }}</span>
    {% endfor %}

Also add a 1 space padding to [filter](http://jinja.pocoo.org/docs/templates/#filters) pipes::

    {{ container | join(', ') }}


## Blank lines

There is *no* blank line at the top and exactly *one* at the end of a file.

Use one blank line to separate semantic HTML sections and jinja blocks (i.e. macros).

Import and extend statements should be grouped at the top of a document, with
one trailing blank line.


## Line length

A strict maximum line length is not enforced, but try to avoid unnecessarily
long lines with multiple tags.


## Assignments

Avoid assignments for cached properties and static attributes, like
`{% set val = view.val %}`. [Assigning](http://jinja.pocoo.org/docs/templates/#assignments)
return values of computationally heavy methods, however, is encouraged::

    {% set web = crawl_web() %}


## Comments

Use [jinja style comments](http://jinja.pocoo.org/docs/templates/#comments)
instead of HTML comments to prevent them from rendering::

    {# TODO: This section needs to be reworked. #}


## Embedded code

Avoid substancial computation within control structures and try to move such
code to view properties.

Still, code inside jinja control structures is *mostly* Python and should
conform to [PEP8](https://www.python.org/dev/peps/pep-0008).
