JS Coding Guidelines
================================

Notation
--------

All functions and variables should be named in CamelCase (eg. "doCounting").
A function name should include an action and a noun (eg. "countNumber"), if the return value is in boolean the action should be "has" (eg. "hasNumber").

Indentation
-----------

We use soft tabs (1 tab = 4 spaces) for indentation.

Whitespace
----------

General use:
- no trailing whitespace
- no whitespace in empty lines

Use maximal whitespacing (`jQuery Style`_), this means:
- use one whitespace behind: comma ``( , )``, colon ``( : )``, opening round brackets ``( ( )`` and before closing brackets ``( ) )``
- use one whitespace before and behind equals sign ``( = )`` and mathematical operators ``( +, *, -, / )`` and comparisons ``( ==, ===, !=, !==, &&, ||, >, < )``

.. code-block:: javascript

    if ( bla == foo ) {
        foo( 'bar', 'baz', { zoo: 1 } );
    }

Whitespace Exceptions
---------------------

There are some exceptions to the whitespacing policy:

.. code-block:: javascript

    // Function with a callback, object, or array as the sole argument:
    // No space on either side of the argument
    foo({
        a: 'alpha',
        b: 'beta'
    });

    // Function with a callback, object, or array as the first argument:
    // No space before the first argument
    foo(function() {
        // Do stuff
    }, options );

    // Function with a callback, object, or array as the last argument:
    // No space after the last argument
    foo( data, function() {
        // Do stuff
    });

    // Usage of jQuery object
    $( '<div class="myclass"></div>' );


Format
------

- use curly brackets to form blocks of code

.. code-block:: javascript

    // wrong!
    if ( true ) foo( 'help!' );

    // correct!
    if ( true ) {
        foo( '911' );
    }

- whenever possible, define all variables of a function at one place (always use var)

.. code-block:: javascript

    var title = 'My title',
        subtitle = 'My subtitle',
        story = 'My story';


- global variabels should always be referenzed by using the window object (eg. window.myGlobalVar)
- whenever we can, we should use single ticks

.. code-block:: javascript

    var title = 'My title';
    $( '<div class="myclass"></div>' );


Comparisons
-----------
For comparisons use:

- String: ``typeof object === 'string'``
- Number: ``typeof object === 'number'``
- Boolean: ``typeof object === 'boolean'``
- Object: ``typeof object === 'object'``
- Plain Object: ``jQuery.isPlainObject(object)``
- Function: ``jQuery.isFunction(object)``
- Array: ``jQuery.isArray(object)``
- Element: ``object.nodeType``
- null: ``object === null``
- null or undefined: ``object == null``
- Global Variables: ``typeof variable === 'undefined'``
- Local Variables: ``variable === undefined``
- Properties: ``object.prop === undefined``

Documentation
-------------
Use `JsDoc Style`_ to describe functions.

.. code-block:: javascript

    /**
    * writes a book.
    * @param {string} title - The title of the book.
    * @param {string} author - The author of the book.
    */
    function writeBook( title, author ) {
    }


.. _jQuery Style: http://contribute.jquery.org/style-guide/js/#spacing
.. _JsDoc Style: http://usejsdoc.org/
