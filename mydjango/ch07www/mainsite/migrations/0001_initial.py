# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pmodel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('url', models.URLField()),
                ('maker', models.ForeignKey(to='mainsite.Maker')),
            ],
        ),
        migrations.CreateModel(
            name='PPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('description', models.CharField(max_length=20, default='产品照片')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nikename', models.CharField(max_length=20, default='超值二手机')),
                ('description', models.TextField(default='暂无说明')),
                ('price', models.PositiveIntegerField(default=0)),
                ('year', models.PositiveIntegerField(default=2018)),
                ('pmodel', models.ForeignKey(to='mainsite.Pmodel')),
            ],
        ),
        migrations.AddField(
            model_name='pphoto',
            name='product',
            field=models.ForeignKey(to='mainsite.Product'),
        ),
    ]
