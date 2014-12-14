from rest_framework import serializers
from .models import Article

from picture.serializers import PictureSerialize
class ArticleSerialize(serializers.ModelSerializer):
    picture = PictureSerialize()

    class Meta:
        model = Article