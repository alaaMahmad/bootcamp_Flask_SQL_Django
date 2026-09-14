from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dojos/create', views.create_dojo),
    path('ninjas/create', views.create_ninja),
    path('dojos/<int:dojo_id>/delete', views.delete_dojo),
]