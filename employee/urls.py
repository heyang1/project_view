# -*- coding:utf-8 -*-
from django.urls import path
from . import views
from .models import Dept, Emp

app_name = 'employee'
urlpatterns = [
    # path('depts/', views.list_dept, name='depts'),
    # path('emps/', views.list_emp, name='emps'),

    path('salegrade/<int:pk>/', views.find_salegrade, name='find_salegrade'),
    path('depts/', views.lst, {'model': Dept}, name='depts'),
    path('emps/', views.lst, {'model': Emp}, name='emps'),
]