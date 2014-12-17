#! /usr/bin/env python
# -*-coding:utf-8-*-
from django.db import models
from scrapy.contrib.djangoitem import DjangoItem

from picture.models import Picture

# Create your models here.
class ArticleManager(models.Manager):
    def get_article_list(self):
        article_list = self.all()
        for article in article_list:
            article.picture = Picture.objects.filter(article=article)
            if len(article.title) < 30:
                article.title = u'【%s】 %s' % (article.title, article.content)
                article.title = article.title[:150]
            elif len(article.title) > 150:
                article.title = article.title[:150]
        return article_list


class Article(models.Model):
    url = models.URLField(max_length=500,null=True,blank=True)
    raw_url = models.URLField(max_length=500)
    title = models.TextField()
    content = models.TextField(null=True,blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    objects = ArticleManager()

    class Meta:
        ordering = ['-created_time']

    def __unicode__(self):
        return self.title[:10]


class ArticleItem(DjangoItem):
    django_model = Article