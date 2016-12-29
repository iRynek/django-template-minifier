django-template-minifier
========================

Django application, providing simple template loader. It reduces HTML output in templates by stripping out whitespace characters between HTML and django template tags.

Things to note:
* It **does not** make any fancy compression, to do that use [GZip Middleware](https://docs.djangoproject.com/en/dev/ref/middleware/#module-django.middleware.gzip).
* To compress CSS and JS use [django-compressor](https://github.com/jezdez/django_compressor).


Installation
===

```bash
pip install django-template-minifier
```

Basic usage
===

Modify Your Django project settings's module.

For production:
---

```python
TEMPLATE_LOADERS = (('django.template.loaders.cached.Loader', (
        'template_minifier.template.loaders.filesystem.Loader',
        'template_minifier.template.loaders.app_directories.Loader',
    )),
)
```

Note cached loader, we prepare template only once. Be sure You **clean up Your 
cache during deploy**.

For development:
---

```python
TEMPLATE_LOADERS = (
    'template_minifier.template.loaders.filesystem.Loader',
    'template_minifier.template.loaders.app_directories.Loader',
)
```

Each refresh recalculate template.

Be happy having less spaces and new lines in Your templates!


Advanced usage:
===

Using modified settings You can:

* turn off stripping spaces between HTML tags

```python
TEMPLATE_MINIFIER_HTML_TAGS = False # default = True
```

* turn off stripping spaces between Django template tags (\s{%, %}\s)

```python
TEMPLATE_MINIFIER_TEMPLATE_TAGS = False # default = True
```

* turn off all stripping

```python
TEMPLATE_MINIFIER = False # default = True
```

* run Your own strip_function, which preprocess templates

```python
TEMPLATE_MINIFER_STRIP_FUNCTION = 'template_minifier.utils.strip_spaces_in_template'
```

(There is a typo in variable name, see #2 for details)

* use only in production

```python
if DEBUG:
    TEMPLATE_MINIFIER = False
```

Known issues:
===

Templates in JS
---
We do not support verbatim tag. Details [here](https://github.com/iRynek/django-template-minifier/issues/3).
PR welcome :)

One line comments in JS
---

Don't use // one line comments in Your inline javascript &lt;script&gt; or .js templates. In some cases,
if You are using lot of {% if %} there, it can comment out }; or }, for example:

```js
// comment something - !!it's evil!!
{% if %}
function name(){
}
{% endif %}
```

**Use /* */ instead**

```js
/* comment something - it's nice and clean <3! */
{% if %}
function name(){
}
{% endif %}
```

Or just set TEMPLATE_MINIFIER_TEMPLATE_TAGS = False

Changelog:
===

Version 1.1.0
-----------
* Added support for [template loader changes in Django 1.9+](https://github.com/django/django/commit/fc2147152637e21bc73f991b50fa06254af02739)

Version 1.0.0
-----------
* Initial package, no tests :/

To do:
===
* Tests!
* {% new_line %} template_tag
* {% space %} template_tag
* support for {% verbatim %} tag
