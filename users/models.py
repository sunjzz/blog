# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.png', max_length=200,
                               blank=True, null=True, verbose_name='用户头像')
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name=u'手机号')
    website = models.URLField()

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-id']
        verbose_name = u'用户'
        verbose_name_plural = verbose_name





