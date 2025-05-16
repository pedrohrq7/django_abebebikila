from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastro, name='cadastro'),  # Rota para login
    path('logout/', views.logout_view, name='logout'),
]