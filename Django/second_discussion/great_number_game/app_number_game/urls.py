from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('guess', views.guess),
    path('submit_score', views.submit_score),
    path('leaderboard', views.show_leaderboard),
    path('reset', views.reset),
]