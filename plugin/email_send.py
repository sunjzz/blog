# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2017/8/24 11:21

import os
from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from blog.settings import EMAIL_FROM

os.environ['DJANGO_SETTINGS_MODULE'] = 'online.settings'