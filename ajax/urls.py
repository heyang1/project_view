# -*- coding:utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path('update_json_params/', views.update_json_params, name='update_json_params'),
    path('update/', views.update, name='update'),
    path('get_salegrade/', views.get_salegrade, name='get_salegrade'),
    path('test2/', views.test2, name='test2'),
    path('test1/', views.test1, name='test1'),
    path('', views.index, name='index'),
]