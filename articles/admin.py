# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from articles.models import Tag, Category, Article, Links
# Register your models here.


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published', 'user')
    list_filter = ('date_published', 'user')


admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
