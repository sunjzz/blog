# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2017/7/27 18:26
from django import forms
from models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'desc', 'content']
