from django.urls import path
from . import views
from django.views.generic.base import RedirectView


app_name = 'uploader'
urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('index/', views.index, name='index'),

]
