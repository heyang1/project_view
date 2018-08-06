from django.urls import path
from . import views

app_name = 'csrf'
urlpatterns = [
    path('form/', views.form, name='form'),
    path('home_ajax/', views.home_ajax, name='home_ajax'),

    path('home/', views.home, name='home'),
    path('index/', views.index, name='index'),

]