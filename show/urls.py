from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.all_notes,name='home'),
    # path('search_notes/', views.search_notes),
    path('contact/', views.contact),
    path('select_dept/',views.select_dept),

    path('<str:slug>/', views.download),
]