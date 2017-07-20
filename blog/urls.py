# coding: utf-8

from django.conf.urls import url
from . import views


app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>\w+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^date/(?P<year>\w{4})/(?P<month>\w{1,2})/$', views.DateView.as_view(), name='date'),
    url(r'^caregory/(?P<pk>\w+)/$', views.CateGoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>\w+)/$', views.TagView.as_view(), name='tag')
]