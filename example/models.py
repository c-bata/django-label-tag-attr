from django.db import models


class SampleModel(models.Model):
    """sample model"""
    CHOICE_FIELD = (
        (1, 'choice 1'),
        (2, 'choice 2'),
        (3, 'choice 3'),
    )

    text = models.CharField('char field', max_length=255)
    choices = models.SmallIntegerField('select box', choices=CHOICE_FIELD)
