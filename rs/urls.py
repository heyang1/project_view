# -*- coding:utf-8 -*-
from django.urls import path
from . import views

app_name = 'rs'
urlpatterns = [
    path(route="test_rs/<int:pk>/", view=views.test_rs, name='test_rs'),
    path(route="test01/", view=views.test01, name='test01'),
]