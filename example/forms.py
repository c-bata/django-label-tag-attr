from django import forms
from example.models import SampleModel


class ContactForm(forms.ModelForm):
    """sample model's form"""
    class Meta:
        model = SampleModel
        fields = ('text', 'choices',)
