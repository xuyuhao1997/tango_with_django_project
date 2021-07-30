from django.urls import path
from rango import views
from django.shortcuts import render
from django.http import HttpResponse

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]