#! /usr/bin/env python
# -*-coding:utf-8-*-

from rest_framework import serializers
from .models import Article

from picture.serializers import PictureSerialize
class ArticleSerialize(serializers.ModelSerializer):
    picture = PictureSerialize(many=True)

    class Meta:
        model = Article
        fields = ('id','raw_url','title','content','created_time','picture')