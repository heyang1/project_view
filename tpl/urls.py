from django.urls import path
from . import views

app_name = 'tpl'

urlpatterns = [

    path('filter/', views.filter, name='filter'),
    path('<int:year>/path/<int:month>/<int:day>/', views.path, name='path'),
    path('user_list/', views.user_list, name='user_list'),
    path('show_user/<int:pk>/', views.show_user, name='show_user'),
    path('find/', views.find, name='find'),
    path('index/', views.index, name='index'),

]