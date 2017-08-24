# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.jpg', max_length=200,
                               blank=True, null=True, verbose_name='用户头像')
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name=u'手机号')
    website = models.URLField()

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-id']
        verbose_name = u'用户'
        verbose_name_plural = verbose_name


choice_send_type = (
    ("register", "注册"),
    ("forget", "找回密码"),
    ("update", "修改邮箱"),
)


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(choices=choice_send_type, max_length=10, verbose_name=u"验证码类型")
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u"发送时间") #实例化时间
#   send_time = models.DateField(default=datetime.now()) 注意这种写法时间是models编译时间

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)





