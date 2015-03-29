from django import forms
from django.template import Template, Context
from django.test import TestCase


LIBRARY_LOAD_STRING = '{% load label_tag_attr %}'


class MyForm(forms.Form):
    sample_field = forms.CharField(label='SampleText')


def render_form(text, form=None, **context_args):
    tpl = Template(LIBRARY_LOAD_STRING + text)
    context_args.update({'form': MyForm() if form is None else form})
    context = Context(context_args)
    return tpl.render(context)


class TestFieldAttributeNode(TestCase):
    def test_rendered_label_has_id(self):
        res = render_form('{% render_label form.sample_field %}',
                          form=MyForm())
        self.assertIn('for="id_sample_field"', res)
        self.assertIn('SampleText', res)
