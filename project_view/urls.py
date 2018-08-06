"""project_view URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('tpl/', include('tpl.urls')),
    path('uploader/', include('uploader.urls')),
    path('csrf/', include('csrf.urls')),
    path('jsonp/', include('jsonp.urls')),
    path('user/',include('user.urls')),
    path('cookie/',include('cookie.urls')),
    path('pro_response/',include('pro_response.urls')),
    path('ajax/',include('ajax.urls')),
    path('post_app/',include('post_app.urls')),
    path('get_app/',include('get_app.urls')),
    # path('http/',include(m_http.urls)),
    path('employee/', include('employee.urls')),
    # path('blog/', include('blog.urls')),
    # path('', include('articles.urls')),
    path('rs/', include('rs.urls')),
    path('admin/', admin.site.urls),
]
