# video/urls.py
from django.conf.urls import url, include
from . import views
from django.urls import path

app_name = "video"

urlpatterns = [
    url(r'^$', views.video_list, name='list'),
    url(r'^new$', views.video_new, name='new'),
    url(r'^(?P<video_id>\d+)/$', views.video_detail, name='detail'),
#    path('$', views.video_list, name='list')
]
