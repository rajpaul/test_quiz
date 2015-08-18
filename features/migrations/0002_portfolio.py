# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('today_prc', models.DecimalField(null=True, max_digits=4, decimal_places=3, blank=True)),
                ('object_type', models.ForeignKey(blank=True, to='features.ObjectType', null=True)),
            ],
        ),
    ]
