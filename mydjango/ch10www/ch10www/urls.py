"""ch10www URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from logininfo import views as lv

urlpatterns = [
    url(r'^$', lv.index),
    url(r'^contact/$', lv.contact),
    url(r'^list/$', lv.listing),
    # url(r'^login/$', lv.login),
    url(r'^logout/$', lv.logout),
    url(r'^userinfo/$', lv.userinfo),
    url(r'^post/$', lv.posting),
    url(r'^post2db/$', lv.post2db),
    url(r'^(\d+)/(\w+)$', lv.index),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
