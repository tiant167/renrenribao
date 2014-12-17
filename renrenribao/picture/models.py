#! /usr/bin/env python
# -*-coding:utf-8-*-
import requests

from django.db import models

# Create your models here.
class Picture(models.Model):
    raw_url = models.URLField(max_length=500)
    image = models.ImageField(upload_to="static/image/%Y/%m/%d",null=True,blank=True)
    article = models.ForeignKey('article.Article')

    def __unicode__(self):
        return self.article.title[:10]

    def fetch_picture(self):
        from PIL import Image
        from cStringIO import StringIO
        from django.core.files.uploadedfile import SimpleUploadedFile
        from random import randint
        import time
        import os

        pic = requests.get(self.raw_url,stream=True)
        DJANGO_TYPE = pic.headers['content-type']
        if DJANGO_TYPE == 'image/jpeg':
            PIL_TYPE = 'jpeg'
            FILE_EXTENSION = 'jpg'
        elif DJANGO_TYPE == 'image/png':
            PIL_TYPE = 'png'
            FILE_EXTENSION = 'png'
        elif DJANGO_TYPE == 'image/gif':
            PIL_TYPE = 'gif'
            FILE_EXTENSION = 'gif'

        image = Image.open(StringIO(pic.content))
        temp_handle = StringIO()
        image.save(temp_handle, PIL_TYPE)
        temp_handle.seek(0)
        suf = SimpleUploadedFile('%s_%s' % (time.strftime('%Y%m%d%H%M%S'),randint(1,100)),
            temp_handle.read(), content_type=DJANGO_TYPE)
        self.image.save('%s.%s' % (os.path.splitext(suf.name)[0],FILE_EXTENSION),suf,save=False)

    def save(self):
        self.fetch_picture()

        super(Picture,self).save()