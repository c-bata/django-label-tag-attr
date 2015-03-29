=====================
django-label-tag-attr
=====================

[![Build Status](https://travis-ci.org/c-bata/django-label-tag-attr.svg?branch=master)](https://travis-ci.org/c-bata/django-label-tag-attr)

More easy to alter css classes and html attributes.
This library can render a form label like `django-widget-tweaks <https://github.com/kmike/django-widget-tweaks>`_

The license is MIT.

Installation
============

::

    $ pip install django-widget-tweaks

Then add 'label_tag_attr' to INSTALLED_APPS.


Usage
=====

Prev
----

.. code-block:: html

    {% load widget_tweaks %}

    <label id="{{ form.text.id_for_label }}" class="control-label">{{ form.text.label }}</label>
    {% render_label form.text class="form-control" %}

Use django-label-tag-attr
-------------------------

``render_field`` template tag for customizing form fields by using an HTML-like syntax.

.. code-block:: html

    {% load label_tag_attr %}
    {% load widget_tweaks %}

    {% render_label form.text class="control-label" %}
    {% render_field form.text class="form-control" %}

Resources
=========

* `Github <https://github.com/c-bata/django-label-tag-attr>`_