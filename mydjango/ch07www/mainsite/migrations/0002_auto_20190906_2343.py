# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='描述', default='暂无说明'),
        ),
        migrations.AlterField(
            model_name='product',
            name='nikename',
            field=models.CharField(verbose_name='摘要', max_length=20, default='超值二手机'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pmodel',
            field=models.ForeignKey(verbose_name='型号', to='mainsite.Pmodel'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(verbose_name='价格', default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='year',
            field=models.PositiveIntegerField(verbose_name='年份', default=2018),
        ),
    ]
