# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 14, 8, 40, 24, 800832, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
