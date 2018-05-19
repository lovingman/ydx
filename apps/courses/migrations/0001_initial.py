# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-11 11:00
from __future__ import unicode_literals

import DjangoUeditor.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='类别名', max_length=30, verbose_name='类别名')),
                ('code', models.CharField(default='', help_text='类别code', max_length=30, verbose_name='类别code')),
                ('desc', models.TextField(default='', help_text='类别描述', verbose_name='类别描述')),
                ('category_type', models.IntegerField(choices=[(1, '方向'), (2, '分类'), (3, '类型')], verbose_name='类目级别')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('parent_category', models.ForeignKey(blank=True, help_text='父目录', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_cat', to='courses.Category', verbose_name='父类目级别')),
            ],
            options={
                'verbose_name': '课程类别',
                'verbose_name_plural': '课程类别',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_type', models.IntegerField(blank=True, choices=[(1, '基础'), (2, '案例'), (3, '架构'), (4, '工具')], null=True, verbose_name='类型')),
                ('name', models.CharField(max_length=52, verbose_name='课程名字')),
                ('desc', models.TextField(blank=True, max_length=200, null=True, verbose_name='课程描述')),
                ('detail', DjangoUeditor.models.UEditorField(blank=True, default='', null=True, verbose_name='课程详情')),
                ('is_easy', models.CharField(choices=[('cj', '初级'), ('zj', '中级'), ('gj', '高级')], max_length=2, verbose_name='难度')),
                ('learn_times', models.IntegerField(default=0, verbose_name='学习时长(分钟数)')),
                ('students', models.IntegerField(default=0, verbose_name='学习人数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏人数')),
                ('image', models.ImageField(blank=True, null=True, upload_to='courses/%Y/%m', verbose_name='封面图')),
                ('fight_image', models.ImageField(blank=True, null=True, upload_to='fights/%Y/%m', verbose_name='实战封面图')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击数')),
                ('is_banner', models.BooleanField(default=False, verbose_name='是否是轮播图')),
                ('is_fight', models.BooleanField(default=False, verbose_name='是否实战')),
                ('abstract', models.CharField(blank=True, max_length=50, null=True, verbose_name='简述')),
                ('price', models.IntegerField(default=0, verbose_name='价格')),
                ('category', models.CharField(blank=True, default='后端', max_length=20, null=True, verbose_name='课程类别')),
                ('tag', models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='课程标签')),
                ('youneed_konw', DjangoUeditor.models.UEditorField(blank=True, default='', null=True, verbose_name='课程须知')),
                ('teacher_tell', DjangoUeditor.models.UEditorField(blank=True, default='', null=True, verbose_name='老师能告诉你')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('course_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Category', verbose_name='课程分类')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.Teacher', verbose_name='讲师')),
            ],
            options={
                'verbose_name': '课程',
                'verbose_name_plural': '课程',
            },
        ),
        migrations.CreateModel(
            name='LastLearn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '上次学习',
                'verbose_name_plural': '上次学习',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='章节名')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='课程')),
            ],
            options={
                'verbose_name': '章节',
                'verbose_name_plural': '章节',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='视频名')),
                ('url', models.URLField(default='www.baidu.com', verbose_name='访问地址')),
                ('learn_times', models.IntegerField(default=0, verbose_name='视频时长(分钟数)')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Lesson', verbose_name='章节')),
            ],
            options={
                'verbose_name': '视频',
                'verbose_name_plural': '视频',
            },
        ),
        migrations.AddField(
            model_name='lastlearn',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Video', verbose_name='视频'),
        ),
    ]
