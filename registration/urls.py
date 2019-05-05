from django.conf.urls import url, include
from django.contrib import admin
#from .views import home, register
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^register/', views.register),
    url(r'^user_type/', views.choose_type),
]