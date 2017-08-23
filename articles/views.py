# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse, redirect
from django.views.generic import View
from django.db.models import Q

from pure_pagination import Paginator, PageNotAnInteger

from models import Article, Tag, Category
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

        previous_article = Article.objects.raw('SELECT * FROM articles_article WHERE id < %s OR ID=(SELECT MIN(ID) FROM articles_article) ORDER BY id DESC LIMIT 1' % int(article_id))[0]
        if previous_article.id == int(article_id):
            previous_article = article

        next_article = Article.objects.raw('SELECT * FROM articles_article WHERE id > %s OR ID=(SELECT MAX(ID) FROM articles_article) ORDER BY id ASC LIMIT 1' % int(article_id))[0]
        if next_article.id == int(article_id):
            next_article = article

        return render(request, 'detail.html', {
            'article': article,
            'previous_article': previous_article,
            'next_article': next_article
        })


class ArticleCreateView(View):
    def get(self, request):
        article_category = Category.objects.all()
        article_tag = Tag.objects.all()
        return render(request, 'create.html', {
            'article_category': article_category,
            'article_tag': article_tag,
        })

    def post(self, request):
        obj = ArticleForm(request.POST)
        if obj.is_valid():
            instance = obj.save()
            return HttpResponse('{"status": "success", "msg": "%s"}' % instance.id, content_type='application/json')
        else:
            return HttpResponse('{"status": "fail", "msg": "保存出错"}', content_type='application/json')




