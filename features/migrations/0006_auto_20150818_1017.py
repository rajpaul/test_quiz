# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0005_portfolio_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='comments',
            field=models.ManyToManyField(related_name='portfolios', null=True, to='interactions.Comments', blank=True),
        ),
    ]
