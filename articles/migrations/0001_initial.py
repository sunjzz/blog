# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 21:37
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='\u6587\u7ae0\u6807\u9898')),
                ('desc', models.CharField(max_length=50, verbose_name='\u6587\u7ae0\u63cf\u8ff0')),
                ('image', models.ImageField(blank=True, default='image/default.png', max_length=200, null=True, upload_to='image/%Y/%m', verbose_name='\u6587\u7ae0\u7f29\u7565\u56fe')),
                ('content', ckeditor.fields.RichTextField(verbose_name='\u6587\u7ae0\u5185\u5bb9')),
                ('click_count', models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u91cf')),
                ('is_recommend', models.BooleanField(default=False, verbose_name='\u662f\u5426\u63a8\u8350')),
                ('date_published', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
            ],
            options={
                'ordering': ['-date_published'],
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='\u5206\u7c7b\u540d\u79f0')),
                ('index', models.IntegerField(default=999, verbose_name='\u5206\u7c7b\u6392\u5e8f')),
            ],
            options={
                'verbose_name': '\u5206\u7c7b',
                'verbose_name_plural': '\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='\u94fe\u63a5\u6807\u9898')),
                ('desc', models.CharField(max_length=200, verbose_name='\u94fe\u63a5\u63cf\u8ff0')),
                ('callback_url', models.URLField(verbose_name='url\u5730\u5740')),
                ('date_published', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('index', models.IntegerField(default=999, verbose_name='\u6392\u5e8f')),
            ],
            options={
                'ordering': ['index', 'id'],
                'verbose_name': '\u94fe\u63a5',
                'verbose_name_plural': '\u94fe\u63a5',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='\u6807\u7b7e\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u6807\u7b7e',
                'verbose_name_plural': '\u6807\u7b7e',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.Category', verbose_name='\u5206\u7c7b'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, to='articles.Tag', verbose_name='\u6807\u7b7e'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237'),
        ),
    ]
