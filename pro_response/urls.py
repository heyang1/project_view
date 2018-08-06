# -*- coding:utf-8 -*-
from django.urls import path
from . import views

app_name = 'pro_response_app'

urlpatterns = [
    path('template/', views.template, name='template'),
    path('return_json/', views.return_json, name='return_json'),
    path('test_rs/', views.test_rs, name='test_rs'),
    path('rs/', views.rs, name='rs'),
    path('index/', views.index, name='index'),
]
