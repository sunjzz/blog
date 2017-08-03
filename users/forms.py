# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2017/7/27 10:27

from django import forms

from captcha.fields import CaptchaField
from models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)


class RegisterForm(forms.Form):
    username = forms.CharField(required=True)
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(required=True)


class ModifyForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']


class UpdateUserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nick_name', 'birthday', 'gender', 'address']


class UpdateUserEmailForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email']