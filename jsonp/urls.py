from django.urls import path
from . import views


urlpatterns = [

    path('callback/', views.callback, name='index'),
    path('index/', views.index, name='index'),

]