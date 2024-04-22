from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('division/<int:division_id>/', views.division_stats, name='division_stats'),
    path('conferences/<int:conference_id>/', views.conference_stats, name='conference_stats'),
    path('teams/<int:team_id>/', views.team_stats, name='team_stats'),
    path('teams/', views.all_teams, name='all_teams'),
]