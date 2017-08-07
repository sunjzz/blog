# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2017/7/27 18:26
from django import forms
from ckeditor.fields import RichTextFormField
from models import Article


# class ArticleForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(ArticleForm, self).__init__(*args, **kwargs)
#         self.fields['tag'].widget = forms.CheckboxSelectMultiple()
#
#     class Meta:
#         model = Article
#         fields = ['title', 'desc', 'content', 'category', 'tag']


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    desc = forms.CharField(max_length=50, required=True)
    content = RichTextFormField()
