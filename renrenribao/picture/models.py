from django.db import models

# Create your models here.
class Picture(models.Model):
    raw_url = models.URLField(max_length=500)
    image = models.ImageField(upload_to="upload/image/%Y/%m/%d",null=True,blank=True)
    article = models.ForeignKey('article.Article')

    def __unicode__(self):
        return self.article.content[:10]