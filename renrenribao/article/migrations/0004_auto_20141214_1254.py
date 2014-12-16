# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20141214_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.TextField(default='as'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
