# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from users.models import UserProfile
from ckeditor.fields import RichTextField

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'标签名称')

    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'分类名称')
    index = models.IntegerField(default=999, verbose_name=u'分类排序')

    class Meta:
        verbose_name = u'分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name=u'文章标题')
    desc = models.CharField(max_length=50, verbose_name=u'文章描述')
    image = models.ImageField(upload_to='image/%Y/%m', default='image/default.png', max_length=200,
                               blank=True, null=True, verbose_name='文章缩略图')
    # content = models.TextField(verbose_name=u'文章内容')
    content = RichTextField(verbose_name=u'文章内容')
    click_count = models.IntegerField(default=0, verbose_name=u'点击量')
    is_recommend = models.BooleanField(default=False, verbose_name=u'是否推荐')
    date_published = models.DateTimeField(auto_now_add=True, verbose_name=u'发布时间')
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    category = models.ForeignKey(Category, blank=True, null=True, verbose_name=u'分类')
    tag = models.ManyToManyField(Tag, verbose_name=u'标签')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_published']


class Links(models.Model):
    title = models.CharField(max_length=50, verbose_name=u'链接标题')
    desc = models.CharField(max_length=200, verbose_name=u'链接描述')
    callback_url = models.URLField(verbose_name=u'url地址')
    date_published = models.DateTimeField(auto_now_add=True, verbose_name=u'发布时间')
    index = models.IntegerField(default=999, verbose_name=u'排序')

    class Meta:
        verbose_name = u'链接'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.title

