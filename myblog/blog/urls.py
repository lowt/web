#coding: utf-8
from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',

url(r'^$', views.PostsListView.as_view(), name='post_list'), # то есть по URL http://имя_сайта/blog/ 
                                               # будет выводиться список постов
url(r'^(?P<pk>\d+)/$', views.PostDetailView.as_view()), # а по URL http://имя_сайта/blog/число/ 
                                              # будет выводиться пост с определенным номером
url(r'^new$', views.PostCreate.as_view(), name='post_new'),

url(r'^edit/(?P<pk>\d+)$', views.PostUpdate.as_view(), name='post_edit'),

url(r'^delete/(?P<pk>\d+)$', views.PostDelete.as_view(), name='post_delete'),

)

