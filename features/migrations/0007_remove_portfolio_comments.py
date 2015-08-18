# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0006_auto_20150818_1017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='comments',
        ),
    ]
