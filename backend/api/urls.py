from django.urls import path
from .views import (
    BattingStatsView, PitchingStatsView, BattingStatsByDivision, PitchingStatsByDivision,
    BattingStatsByConferenceView, PitchingStatsByConferenceView, BattingStatsByTeam,
    PitchingStatsByTeam, TeamListView, TeamByDivisionListView, TeamByConferenceListView,
    ConferenceListView, ConferenceByDivisionListView, DivisionListView,
    ConferenceDetailView, TeamDetailView
)

urlpatterns = [
    # stats/
    path('batting-stats/', BattingStatsView.as_view(), name='batting-stats'),
    path('pitching-stats/', PitchingStatsView.as_view(), name='pitching_stats'),

    # stats/division/<id>/
    path('batting-stats/division/<int:division_id>/', BattingStatsByDivision.as_view(), name='batting-stats-by-division'),
    path('pitching-stats/division/<int:division_id>/', PitchingStatsByDivision.as_view(), name='pitching-stats-by-division'),

    # stats/conference/<id>/
    path('batting-stats/conference/<int:conference_id>/', BattingStatsByConferenceView.as_view(), name='batting-stats-by-conference'),
    path('pitching-stats/conference/<int:conference_id>/', PitchingStatsByConferenceView.as_view(), name='pitching-stats-by-conference'),

    # stats/team/<id>/
    path('batting-stats/team/<int:team_id>/', BattingStatsByTeam.as_view(), name='batting-stats-by-team'),
    path('pitching-stats/team/<int:team_id>/', PitchingStatsByTeam.as_view(), name='pitching-stats-by-team'),

    # divisions/
    path('divisions/', DivisionListView.as_view(), name='list-divisions'),

    # conferences/
    path('conferences/', ConferenceListView.as_view(), name='list-conferences'),
    path('conferences/<int:id>/', ConferenceDetailView.as_view(), name='conference-detail'),
    path('conferences/division/<int:division_id>/', ConferenceByDivisionListView.as_view(), name='list-conferences-by-division'),
    
    # teams/
    path('teams/', TeamListView.as_view(), name='list-teams'),
    path('teams/<int:id>/', TeamDetailView.as_view(), name='team-detail'),
    path('teams/division/<int:division_id>/', TeamByDivisionListView.as_view(), name='list-teams-by-division'),
    path('teams/conference/<int:conference_id>/', TeamByConferenceListView.as_view(), name='list-teams-by-conference'),
]
