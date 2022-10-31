from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, ),
    path('login/', views.new_login, ),
    path('logout/', views.logout, ),
    path('change/', views.change, ),
    path('account/', views.account, ),
]