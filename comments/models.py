# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from users.models import UserProfile
from articles.models import Article


# Create your models here.


class Comment(models.Model):
    content = models.TextField(verbose_name=u'评论内容')
    date_published = models.DateTimeField(auto_now_add=True, verbose_name=u'发布时间')
    user = models.ForeignKey(UserProfile, blank=True, null=True, verbose_name=u'用户')
    article = models.ForeignKey(Article, blank=True, null=True, verbose_name=u'文章')
    pid = models.ForeignKey('self', blank=True, null=True, verbose_name=u'父级评论')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = verbose_name
        ordering = ['-date_published']



