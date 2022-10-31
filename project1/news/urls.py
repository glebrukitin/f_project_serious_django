from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list.as_view(), ),
    path('<int:id>/', views.post_detail, )
]