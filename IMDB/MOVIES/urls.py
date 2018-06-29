from django.conf.urls import include,url
from views import getmovies,getdirector


urlpatterns = [
        url(r'^movies/',getmovies),
        url(r'^director/(?P<_director>[\w\-]+)/$',getdirector),
]
#r'^studentname/(?P<_studentname>[\w\-]+)/$'
