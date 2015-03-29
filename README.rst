=====================
django-label-tag-attr
=====================

[![Build Status](https://travis-ci.org/c-bata/django-label-tag-attr.svg?branch=master)](https://travis-ci.org/c-bata/django-label-tag-attr)

Django library to alter css classes and html attributes.

The license is MIT.

About
=====



How to use
==========

Prev
----

.. code-block:: html

    <label id="{{ form.text.id_for_label }}" class="control-label">{{ form.text.label }}</label>
    {% render_label form.text class="form-control" %}

Next
----

.. code-block:: html

    {% render_label form.text class="control-label" %}
    {% render_field form.text class="form-control" %}


Resources
=========

* `Github <https://github.com/c-bata/django-label-tag-attr>`_