from django.urls import path
from . import views

app_name = 'cookie_app'

urlpatterns = [
    path('js_cookie/',views.js_cookie,name='js_cookie'),
    path('delete_cookie/', views.delete_cookie, name='delete_cookie'),
    path('read_signed_cookie/', views.read_signed_cookie,
         name='read_signed_cookie'),
    path('read_cookie/', views.read_cookie, name='read_cookie'),
    path('set_cookie/', views.set_cookie, name='set_cookie'),
]