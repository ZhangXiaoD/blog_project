# coding: utf-8
from django.conf.urls import url
from . import views


app_name = 'comments'
urlpatterns = [
    url(r'^post/comment/(?P<post_pk>\w+)/$', views.post_comment, name='post_comment')
]