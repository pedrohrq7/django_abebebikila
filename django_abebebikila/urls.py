"""
URL configuration for django_abebebikila project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import include, path
from django.conf import settings  
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('discografia/', include('discografia.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('cadastro/', include('cadastro.urls')),
]

