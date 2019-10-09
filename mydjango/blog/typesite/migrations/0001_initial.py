# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('user_full_name', models.CharField(verbose_name='用户名', max_length=30, blank=True, null=True)),
                ('user_name', models.CharField(verbose_name='账号', max_length=30)),
                ('user_password', models.CharField(verbose_name='密码', max_length=30)),
                ('user_email', models.CharField(verbose_name='邮箱', max_length=45, blank=True, null=True)),
                ('user_sex', models.IntegerField(verbose_name='性别')),
                ('user_age', models.IntegerField(verbose_name='年龄')),
                ('user_phone_number', models.CharField(verbose_name='电话号码', max_length=20, blank=True, null=True)),
                ('user_card', models.CharField(verbose_name='身份证号码', max_length=30)),
                ('createby', models.CharField(verbose_name='创建者', max_length=32)),
                ('createtime', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('updateby', models.CharField(verbose_name='更新者', max_length=32, null=True)),
                ('updatetime', models.DateTimeField(verbose_name='更新时间', blank=True, null=True)),
                ('is_active', models.IntegerField(verbose_name='是否使用', blank=True, null=True, default=1)),
                ('img_url', models.ImageField(verbose_name='头像', blank=True, null=True, upload_to='img')),
            ],
            options={
                'db_table': 'sys_user',
            },
        ),
    ]
