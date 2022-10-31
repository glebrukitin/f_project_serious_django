from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('dost/', views.places_list, ),
    path('pam/', views.pam_places_list, ),
    path('<int:id>/', views.place_detail, )
]