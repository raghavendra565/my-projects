from django.conf.urls import include, url
from django.http import HttpResponse
from views import getsquare,getnum,post


urlpatterns =[
    url(r'^getsqr/(?P<_num>\d+)', getsquare),
    url(r'^post/(?P<_values>[0-99,-]+)',post),
    url(r'^numsqr/(?P<_num>\d+)',getnum)
]
