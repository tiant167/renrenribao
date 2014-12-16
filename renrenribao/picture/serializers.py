#! /usr/bin/env python
# -*-coding:utf-8-*-

from rest_framework import serializers
from .models import Picture

class PictureSerialize(serializers.ModelSerializer):

    class Meta:
        model = Picture