#!/usr/bin/python3
# -*- coding:utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from .views import index

urlpatterns = [
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]