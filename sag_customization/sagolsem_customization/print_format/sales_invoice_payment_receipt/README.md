# Variables

| name               | description                                                            |
| ------------------ | ---------------------------------------------------------------------- |
| **page_height**    | sets `min-height` of the page                                          |
| **page_font_size** | sets `font-size` of the text. others are `em` sizes based off of this. |
| **title**          | sets title text to be rendered on the printed page                     |

## A5

```
{% set page_height = "7.4in" %}
{% set page_font_size = "10pt" %}
```

## A6

```
{% set page_height = "5.3in" %}
{% set page_font_size = "9pt" %}
```
