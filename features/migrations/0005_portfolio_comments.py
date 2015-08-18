# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interactions', '0001_initial'),
        ('features', '0004_auto_20150818_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='comments',
            field=models.ManyToManyField(related_name='portfolios', to='interactions.Comments'),
        ),
    ]
