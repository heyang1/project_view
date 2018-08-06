# -*- coding:utf-8 -*-
from django.urls import path
from . import views

app_name = 'post_app'

urlpatterns = [

    path('add/', views.add, name='add'),
    path('index/', views.index, name='index'),

]
