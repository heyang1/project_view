# -*- coding:utf-8 -*-
from django.urls import path
from . import views
from django.views.generic.base import RedirectView
app_name = 'user'

urlpatterns = [
    path('template/<int:pk>/', views.template, name='template'),
    path('detail/<slug:slug_value>/', views.UserDetailView.as_view(), name='detail'),
    # path('detail/<int:abc>/', views.UserDetailView.as_view(), name='detail'),
    path('list/', views.UserListView.as_view(), name='list'),

    path('redirect/', views.UserRedirectView.as_view(), name='redirect'),

    path('go-to-django/',
         RedirectView.as_view(url='https://www.djangoproject.com'),
         name='go-to-django'),

    path('go-to-home/',
         RedirectView.as_view(url='../home/'),
         name='go-to-home'),

    path('home/', views.HomeView.as_view(), name='home'),
    path('login/',views.login,name='login'),

    path('index/',views.index,name='index'),
    path('logout/',views.logout,name='logout'),
    path('',views.UserView.as_view(),name=''),
]