"""Publish URL Configuration

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

from userauths.views import *
from articles.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	
    #Stories App
    url(r'^$',home,name='home'),
    url(r'^s/$',search_article,name='search_article'),
    url(r'^my$',my_articles,name='my_articles'),
    url(r'^article/(?P<slug>[\w-]+)/',single_article,name="single_article"),
    url(r'^edit/(?P<slug>[\w-]+)/',edit_article,name="edit_article"),
    #authusers app
	url(r'^logout/',logout_view,name='logout_view'),
    url(r'^login/',login_view,name='login_view'),
    url(r'^signup/',signup_view,name='signup_view'),
    url(r'^home/',user_home,name='user_home'),
]
