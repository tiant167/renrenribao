# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('raw_url', models.URLField(max_length=500)),
                ('image', models.ImageField(null=True, upload_to=b'upload/image/%Y/%m/%d', blank=True)),
                ('article', models.ForeignKey(to='article.Article')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
