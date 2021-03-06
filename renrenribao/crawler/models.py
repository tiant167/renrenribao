from django.db import models
from dynamic_scraper.models import Scraper, SchedulerRuntime

# Create your models here.

class CrawlerWebsite(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    scraper = models.ForeignKey(Scraper,blank=True,null=True,on_delete=models.SET_NULL)
    scraper_runtime = models.ForeignKey(SchedulerRuntime,blank=True,null=True,on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name