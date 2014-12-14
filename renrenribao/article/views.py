from django.shortcuts import render
from django.views.generic import View

from .models import Article
# Create your views here.

class ArticleList(View):
    
    def get(self,request):
        queryset = Article.objects.get_article_list()
        return render(request,'article/article_list.html',{'article_list':queryset})