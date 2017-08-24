# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
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


class UserRegisterView(View):
    def get(self, request):
        return render(request, 'register.html', {})

    def post(self, request):
        registe_form = forms.RegisterForm(request.POST)
        if registe_form.is_valid():
            user_name = request.POST.get("username", "")
            if models.UserProfile.objects.filter(Q(username=user_name), Q(email=user_name)):
                return render(request, 'register.html', {"msg": "用户名已存在！"})
            user_pwd1 = request.POST.get("password1", "")
            user_pwd2 = request.POST.get("password2", "")
            if user_pwd1 != user_pwd2:
                return render(request, 'register.html', {"msg": "密码不一致！"})
            user_profile = models.UserProfile()
            user_profile.username = user_name
            user_profile.password =user_pwd1
            user_profile.save()



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
                    return HttpResponseRedirect(reverse('article:article_list'))
                else:
                    return render(request, "login.html", {"msg": "用户名或密码错误！"})
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误！"})
        else:
            return render(request, "login.html", {"msg": "用户名或密码错误！", "login_form": login_form})

