# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SampleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='char field')),
                ('choices', models.SmallIntegerField(choices=[(1, 'choice 1'), (2, 'choice 2'), (3, 'choice 3')], verbose_name='select box')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
