# -*- coding:utf-8 -*-
from django.urls import path
from . import views

app_name = 'get_app'

urlpatterns = [

    path('handler_multi/', views.handler_multi, name='handler_multi'),
    path('handler_one/', views.handler_one, name='handler_one'),
    path('index/', views.index, name='index'),
    path('print_request/', views.print_request, name='print_request'),
]