from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect



urlpatterns = [
    url(r'^new/', view.post_new),
]