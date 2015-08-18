# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0003_instrument'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('object_type', models.CharField(blank=True, max_length=31, null=True, verbose_name=b'ObjectType', choices=[(b'PORTFOLIO', b'PORTFOLIO'), (b'USER', b'USER'), (b'INSTRUMENT', b'INSTRUMENT')])),
            ],
        ),
        migrations.AlterField(
            model_name='instrument',
            name='object_type',
            field=models.CharField(blank=True, max_length=31, null=True, verbose_name=b'ObjectType', choices=[(b'PORTFOLIO', b'PORTFOLIO'), (b'USER', b'USER'), (b'INSTRUMENT', b'INSTRUMENT')]),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='object_type',
            field=models.CharField(blank=True, max_length=31, null=True, verbose_name=b'ObjectType', choices=[(b'PORTFOLIO', b'PORTFOLIO'), (b'USER', b'USER'), (b'INSTRUMENT', b'INSTRUMENT')]),
        ),
    ]
