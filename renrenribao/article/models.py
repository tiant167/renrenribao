from django.db import models
from picture.models import Picture

# Create your models here.
class ArticleManager(models.Manager):
    def get_article_list(self):
        article_list = self.all()
        for article in article_list:
            article.picture = Picture.objects.filter(article=article)
        return article_list

class Article(models.Model):
    raw_url = models.URLField(max_length=500)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    objects = ArticleManager()
    
    class Meta:
        ordering = ['-created_time']

    def __unicode__(self):
        return self.content[:10]