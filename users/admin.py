# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import UserProfile

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    # fields = ('username', )
    list_display = ('username', 'last_login', 'mobile')


admin.site.register(UserProfile, UserProfileAdmin)
