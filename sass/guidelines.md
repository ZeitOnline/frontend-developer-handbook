# ZEIT ONLINE SASS Coding Guidelines

## Definition
```sass
.block
    margin: 0
```

- The above mentioned code example covers one **sass rule** or **ruleset**.
- `.block` in this case is the **selector**.
- `margin: 0` is a **declaration**,
- where `margin` is the property
- and `0` is the value.

## Notation
All classes and ids in the html should be written lowercased. Therefor all selectors should be written lowercased. Also all declarations have to be written in lowercase.

## Indentation
We use tabs for indentation.

## Whitespace
Remove trailing whitespace (i.e. tell your text editor to do so automatically). Never mix spaces and tabs for *indentation*.

## Format
- Use one selector per line in multi-selector rulesets.
- Include a single space before the opening brace of a ruleset.
- Include one declaration per line in a declaration block.
- Use one level of indentation for each declaration.
- Include a single space after the colon of a declaration.
- Use lowercase and shorthand hex values, e.g., `#aaa`.
- Use single or double quotes consistently. Preference is for double quotes, e.g., `content: ""`.
- Quote attribute values in selectors, e.g., `input[type="checkbox"]`.
- *Where allowed*, avoid specifying units for zero-values, e.g., `margin: 0`.
- Include a space after each comma in comma-separated property or function values.
- Place the closing brace of a ruleset in the same column as the first character of the ruleset.
- Separate each ruleset by a blank line.

## Special Characters
When using unicode character codes, please declare the character itself and a description in a comment on the same line:
```sass
content: "\203A" // › = single right-pointing angle quotation mark
```

## Declaration order
Declarations should be alphabetically ordered.

## Exceptions
Long, comma-separated property values - such as collections of gradients or shadows - can be arranged across multiple lines in an effort to improve readability and produce more useful diffs. There are various formats that could be used; one example is shown below.
```sass
.selector
    background-image:
        linear-gradient(#fff, #ccc),
        linear-gradient(#f3c, #4ec)
    box-shadow:
        1px 1px 1px #000,
        2px 2px 1px 1px #ccc inset
```

## Naming convention
The overall used naming convention used on ZON webpages should be following the [BEM][1] naming scheme. BEM in this case stands for `block, element, modifier`, which refers to the the three levels of differentiation this convention uses. If you are not familiar with this naming convention, [read this article][2] now.

### Naming Pattern
The naming convention follows this pattern:
```sass
.block
.block__element
.block--modifier
```

- `.block` represents the higher level of an abstraction or component.
- `.block__element` represents a descendent of .block that helps form .block as a whole.
- `.block--modifier` represents a different state or version of .block.

The double underscores and hyphens are used because block, element or modifier themselves can contain single hyphens or underscores.

### HTML Example
A typical HTML construct following this convention looks like this:
```html
<form class="site-search  site-search--full">
    <input type="text" class="site-search__field">
    <input type="submit" value ="Search" class="site-search__button">
</form>
```

While `.block` and `.block__element` can be assigned to elements seperately, `.block--modifier` is always used together with the element it modifies. In this case `site-search  site-search--full`. The modifier css rule may only contain *additional* declarations.

### No IDs
You must not use any `#id` as a selector.

[1]: http://bem.info/ "BEM – Technology for creating web applications"
[2]: http://csswizardry.com/2013/01/mindbemding-getting-your-head-round-bem-syntax/ "MindBEMding – getting your head ’round BEM syntax"

## Preprocessor
We assume here that Sass is used as prepocessor. As long they are applicable, all rules that apply to css also apply to the code for css preprocessors.

### Declaration order
- First list `@extend` declaration
- afterwards list `@mixin/@include` statements
- then list regular styles
- at least add nested elements.

We put `@mixins` above regular styles, so we can override specific propertiers defined by a mixin.

You might want to make the call on separating user-authored @includes and vendor-provided @includes.

### Maximum Nesting
To keep up code readability and to avoid *specificity war*, do not nest Sass/SCSS code more than three levels deep.


### Rules
`border-width` should have pixel values always. Use `2px solid black` instead of `0.125rem solid black`. We do not want subpixel border width.


### Additional preprocessor specific rules
- Do not write vendor-prefixes directly into the code, use `@mixin`.
- Do not put styles into the global and section-specific sass files. Just list imported sass files and partials there.
    + list vendor/global dependencies first, then author dependencies, then patterns, then parts
    + as these files act like a table of content, comment them appropriate
    + do not put styles in there
- Partials are named with a leading underscore, like `_partial.sass`
- Variablize all common numbers, and numbers with meaning
- Variablize all colors, avoid using literal colors, encourage semantic color mappings 
- As the amount of font variables rose, we omitted all font-variables.
- Use hyphenated-variable-names (no camelCase or snake_case)
- For naming, use the [general-to-specific](http://webdesign.tutsplus.com/tutorials/quick-tip-name-your-sass-variables-modularly--webdesign-13364) approach when appropriate
- Name your media-queries

```sass
/**
 * Examples
 */

// literal colors
$black: black !default
$grey: #808080 !default
$red: #e02020 !default

// semantic color mappings
$primary-color: $black
$accent-color: $grey
$alert-color: $red
$link-color: $red

// usage
$comments-color-text: $primary-color
$comments-color-link: $link-color
$comments-bg: $accent-color
```
