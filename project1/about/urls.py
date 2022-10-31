from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('history/', views.history, ),
    path('', views.index, ),
    path('pam/', views.index_1, ),
    path('galery/', views.galery.as_view())
]