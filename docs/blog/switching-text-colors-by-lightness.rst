Switching text colors in subject to its background color lightness
==================================================================

Sometimes you build a feature with the feeling, there is something that can go wrong afterwards. In this case we built a CMS feature where the editor could decide more or less about the background color of a part of the website. This poses in our thinking a threat to the accessibility of the foreground text, falling behind in contrast in the best case, being completely unreadable in the worst case. No user would certainly choose a black background with black text on it, but what about some of the so loved shades of gray? So… we looked for a solution to change text colors automatically.

What we found was `Switch font color for different backgrounds with CSS`_ over at CSS-Tricks, which uses css variables (and a css math coding trick from hell to achieve conditional statements) to change text colors in subject to its background. But the article also led to the `Techniques For Accessibility Evaluation And Repair Tools Working Draft`_ of the W3C, which includes an equation to estimate `perceived lightness`_ of colors.

::

    L = (red * 0.299 + green * 0.587 + blue * 0.114) / 255


If you put the red, green and blue parts of a color value into the equation you will get a value between 0 and 1, where 0 is perceived as an absolute dark color (black). I would not question the math behind this. All what's left to do is to set a threshold value, from which one we think of a color as so dark, that we need to change the foreground color.

This can be certainly achieved with css variables (and the conditional css trick mentioned before) but as we have a broad variety of browsers we need to support that certainly not `support`_ css custom properties yet, we decided to put the equation into a template function of our pythonic template engine `jinja2`_.

::

    import colorsys

    def color_is_dark(hexcolor):
        # takes a hex background color (no shorthands) and computes
        # if the color is dark in accessiblity context
        # i.e. a light color needs to be used for contrast
        # like in light font on dark background
        threshold = 0.6
        try:
            red, green, blue = tuple(int(hexcolor[i:i+2], 16) for i in (0, 2, 4))
            # percieved lightness by W3C working draft
            # https://www.w3.org/TR/AERT/#color-contrast
            l = (red * 0.299 + green * 0.587 + blue * 0.114) / 255
            return l < threshold
        except:
            return True

If the color is defined as dark (lower than 0.6) we add a modifier class to the teaser to change colors of the content:

::

    {% block teaser_modifier -%}
        {% if teaser.serie.color -%}
            {{ 'teaser--light-text' if teaser.serie.color | color_is_dark }}
        {%- endif %}
    {%- endblock %}


In the CSS we change now text colors based on the background color, from dark gray on light backgrounds to white on dark backgrounds. For testing purposes we put two versions of the feature on a test page one with light and one with dark background and do a11y tests on them with `axe`_ and `Selenium`_ (we use `pytest`_ for these things).

::

    from axe_selenium_python import Axe

    def test_podcast_leader_dark_is_accessable(selenium_driver):
        driver = selenium_driver
        driver.get('/zeit-online/index-with-podcast-lead-variations')
        axe = Axe(driver)
        axe.inject()
        result = axe.run('.teaser-podcast-leader', {
            'runOnly': ['wcag2a', 'wcag2aa', 'wcag2aaa'],
            'resultTypes': ['violations'],
            'rules': {
                'color-contrast': {'enabled': 'true'}
            }
        })

        assert len(result.get('violations')) == 0


Based on the CSS-Tricks method there is `a codepen`_ to demonstrate the outcome.


Resources
---------

Articles
________

- `Switch font color for different backgrounds with CSS`_


Webstandards
____________

- `Techniques For Accessibility Evaluation And Repair Tools Working Draft`_



Tools
______

- `axe-selenium-python`_
- `pytest`_


*Written 2019-03-07, Nico Brünjes*


.. _Switch font color for different backgrounds with CSS: https://css-tricks.com/switch-font-color-for-different-backgrounds-with-css/
.. _Techniques For Accessibility Evaluation And Repair Tools Working Draft: https://www.w3.org/TR/AERT/#color-contrast
.. _perceived lightness: https:google.cmo
.. _support: https://caniuse.com/#feat=css-variables
.. _jinja2: http://jinja.pocoo.org/
.. _axe: https://github.com/mozilla-services/axe-selenium-python
.. _selenium: https://selenium-python.readthedocs.io/
.. _pytest: https://docs.pytest.org/en/latest/
.. _a codepen: https://codepen.io/codecandies/pen/QYQLZb/
.. _Switch font color for different backgrounds with CSS: https://css-tricks.com/switch-font-color-for-different-backgrounds-with-css/
.. _Techniques For Accessibility Evaluation And Repair Tools Working Draft : https://www.w3.org/TR/AERT/#color-contrast
.. _axe-selenium-python: https://github.com/mozilla-services/axe-selenium-python
