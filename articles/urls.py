# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2017/7/28 14:43
from django.conf.urls import url
from views import ArticleListView, ArticleDetailView, ArticleCreateView

urlpatterns = [
    url(r'^list/$', ArticleListView.as_view(), name='article_list'),
    url(r'^detail/(?P<article_id>\d+)/$', ArticleDetailView.as_view(), name='article_detail'),
    url(r'^create/$', ArticleCreateView.as_view(), name='article_create')
]
