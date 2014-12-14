from django.conf.urls import patterns, url

from .views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'renrenribao.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'list/$',ArticleList.as_view())
    # url(r'^$',a),
)
