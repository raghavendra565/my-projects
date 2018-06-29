from django.conf.urls import include, url
from .views import studentdata,getstudent,facultydata,getfaculty,getstudentname,getstudentid


urlpatterns = [
    url(r'^VIKAS/', getstudent),
    url(r'^student/',studentdata),
    url(r'^subject/',facultydata),
    url(r'^studentname/(?P<_id>\d+)',getstudentname),
    url(r'^studentname/(?P<_subject>[\w\-]+)/$', getstudentid),
]
