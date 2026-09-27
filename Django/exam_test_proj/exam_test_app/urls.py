from django.urls import path
from . import views

urlpatterns = [
    # Landing Page & Auth Routes
    path('', views.landing_page, name='landing_page'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    
    # Dashboard & Participant CRUD Routes
    path('dashboard', views.dashboard, name='dashboard'),
    path('create', views.create_participant, name='create_participant'),
    path('edit/<int:id>', views.edit_participant, name='edit_participant'),
    path('view/<int:id>', views.view_participant, name='view_participant'),
    path('delete/<int:id>', views.delete_participant, name='delete_participant'),
    
    # Active Subscription Report Route (Stretch Goal)
    path('view/current/report', views.current_report, name='current_report'),
]