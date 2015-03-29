from django import template
from django.template import Node

register = template.Library()

LABEL_STR_FORMAT = '<label for="{field.auto_id}" {attr}>{field.label}</label>'


@register.tag(name="render_label")
def render_label(parser, token):
    try:
        bits = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            '%r tag requires a form field followed by a list of attributes '
            'and values in the form attr="value"' % token.split_contents()[0])

    tag_name, form_field, form_attr = bits[0], bits[1], bits[2:]
    form_field = parser.compile_filter(form_field)
    return FieldAttributeNode(form_field, form_attr)


class FieldAttributeNode(Node):
    def __init__(self, form_field, form_attr):
        self.form_field = form_field
        self.form_attr = form_attr

    def render(self, context):
        bounded_field = self.form_field.resolve(context)
        return LABEL_STR_FORMAT.format(field=bounded_field,
                                       attr=''.join(self.form_attr))
