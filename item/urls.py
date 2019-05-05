from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url(r'^new/', views.check),
    url(r'^$', views.post_new),
    url(r'^list/', views.item_list)
]