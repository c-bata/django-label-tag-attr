from django import template
from django.template import Node

register = template.Library()


@register.tag(name="render_label")
def render_label(parser, token):
    try:
        bits = token.split_contents()
        tag_name = bits[0]
        label_field = bits[1]
        form_attrs = bits[2:]
    except ValueError:
        raise template.TemplateSyntaxError(
            '%r tag requires a form field followed by a list of attributes'
            ' and values in the form attr="value"' % tag_name)

    label_field = parser.compile_filter(label_field)
    return FieldAttributeNode(label_field, form_attrs)


class FieldAttributeNode(Node):
    def __init__(self, form_field, form_attrs):
        self.form_field = form_field
        self.form_attrs = form_attrs

    def render(self, context):
        bounded_field = self.form_field.resolve(context)
        return '<label for="%s" %s>%s</label>'\
               % ('auto_id',
                  ''.join(self.form_attrs),
                  bounded_field)
