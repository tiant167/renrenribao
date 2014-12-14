from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article
from .serializers import ArticleSerialize
# Create your views here.

class ArticleList(APIView):

    def get(self,request):
        queryset = Article.objects.get_article_list()
        result = ArticleSerialize(queryset,many=True)
        return Response(result.data)