# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from django.views.generic import View
from django.db.models import Q

from pure_pagination import Paginator, PageNotAnInteger

from models import Article
from forms import ArticleForm

# Create your views here.


class ArticleListView(View):
    def get(self, request):

        sort = request.GET.get("sort", "")

        if sort == 'date':
            order_filed = "-date_published"
        else:
            order_filed = "title"

        search_keywords = request.GET.get("keywords", "")

        all_articles = Article.objects.all()

        if search_keywords:
            all_articles = all_articles.filter(Q(title__contains=search_keywords)|Q(desc__contains=search_keywords))

        choose_sort = all_articles.order_by(order_filed)

        try:
            page = request.GET.get("page", 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(choose_sort, 10, request=request)

        article = p.page(page)

        return render(request, "index.html", {
            "all_article": article,
            "sort": sort
        })


class ArticleAddView(View):
        def post(self, request):
            article_create = ArticleForm
            if article_create.is_valid():
                article_create.save(commit=True)
                return HttpResponse('{"status": "success"}', content_type='application/json')
            else:
                return HttpResponse('{"status": "fail", "msg": "保存出错"}', content_type='application/json')


