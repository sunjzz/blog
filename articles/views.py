# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
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


class ArticleDetailView(View):
    def get(self, request, article_id):
        article = Article.objects.get(id=int(article_id))
        article.click_count += 1
        article.save()

        if int(article_id)-1 < 1:
            previous_article = Article.objects.get(id=int(article_id))
        else:
            previous_article = Article.objects.get(id=int(article_id)-1)

        try:
            next_article = Article.objects.get(id=int(article_id)+1)
        except:
            next_article = Article.objects.get(id=int(article_id))

        return render(request, 'detail.html', {
            'article': article,
            'previous_article': previous_article,
            'next_article': next_article
        })


class ArticleCreateView(View):
        def post(self, request):
            article_create = ArticleForm
            if article_create.is_valid():
                article_create.save(commit=True)
                return HttpResponseRedirect(reverse('article:article_list'))
            else:
                return HttpResponse('{"status": "fail", "msg": "保存出错"}', content_type='application/json')


