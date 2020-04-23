from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.all_notes,name='home'),
    path('<str:slug>', views.selected,name='home'),


]