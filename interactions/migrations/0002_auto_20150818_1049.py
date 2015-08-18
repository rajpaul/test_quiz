# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0007_remove_portfolio_comments'),
        ('interactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='parent_instrument',
            field=models.ForeignKey(blank=True, to='features.Instrument', null=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='parent_portfolio',
            field=models.ForeignKey(blank=True, to='features.Portfolio', null=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='parent_user',
            field=models.ForeignKey(blank=True, to='features.User', null=True),
        ),
    ]
