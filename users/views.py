# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend

from utils.login_utils import LoginRequired

from users import models, forms
# Create your views here.


def custombackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = models.UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class UserLoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            user_pawd = request.POST.get("password", "")
            user = authenticate(username=user_name, password=user_pawd)
            if user is not None:
                if user.is_active:
                    login(request, user)
                else:
                    return HttpResponseRedirect(reverse('article:article_list'))
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误！"})
        else:
            return render(request, "login.html", {"msg": "用户名或密码错误！", "login_form": login_form})

