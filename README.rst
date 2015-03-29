=====================
django-label-tag-attr
=====================

.. image:: https://travis-ci.org/c-bata/django-label-tag-attr.svg
    :target: https://travis-ci.org/c-bata/django-label-tag-attr

Add css classes and html tag attributes to form's label in django templates.
This library can render a form label like `django-widget-tweaks <https://github.com/kmike/django-widget-tweaks>`_

The license is MIT.

Installation
============

::

    $ pip install django-widget-tweaks

Then add 'label_tag_attr' to INSTALLED_APPS.


Usage
=====

Previous
--------

.. code-block:: html

    {% load widget_tweaks %}

    <label id="{{ form.text.id_for_label }}" class="control-label">{{ form.text.label }}</label>
    {% render_label form.text class="form-control" %}  {# django-widget-tweaks use #}

Use django-label-tag-attr
-------------------------

``render_field`` template tag for customizing form's label by using an HTML-like syntax.

.. code-block:: html

    {% load label_tag_attr %}
    {% load widget_tweaks %}

    {% render_label form.text class="control-label" %}  {# this library use #}
    {% render_field form.text class="form-control" %}  {# django-widget-tweaks use #}

Resources
=========

* `Github <https://github.com/c-bata/django-label-tag-attr>`_
* `PyPI <https://pypi.python.org/pypi/django-label-tag-attr>`_
