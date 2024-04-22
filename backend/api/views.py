from django.db.models import Q
from rest_framework import generics
from .models import Player, Team, Conference, Division, BattingStats, PitchingStats
from .serializers import BattingStatsSerializer, PitchingStatsSerializer, ConferenceSerializer, TeamSerializer, DivisionSerializer

# List all batting stats
class BattingStatsView(generics.ListAPIView):
    queryset = BattingStats.objects.select_related('player')
    serializer_class = BattingStatsSerializer

# List all pitching stats
class PitchingStatsView(generics.ListAPIView):
    queryset = PitchingStats.objects.select_related('player')
    serializer_class = PitchingStatsSerializer

# List batting stats by division
class BattingStatsByDivision(generics.ListAPIView):
    serializer_class = BattingStatsSerializer

    def get_queryset(self):
        division_id = self.kwargs.get('division_id', '')
        return BattingStats.objects.filter(player__team__division__id=division_id).select_related('player', 'player__team')

# List pitching stats by division
class PitchingStatsByDivision(generics.ListAPIView):
    serializer_class = PitchingStatsSerializer

    def get_queryset(self):
        division_id = self.kwargs.get('division_id', '')
        return PitchingStats.objects.filter(player__team__division__id=division_id).select_related('player', 'player__team')

# List batting stats by conference
class BattingStatsByConferenceView(generics.ListAPIView):
    serializer_class = BattingStatsSerializer

    def get_queryset(self):
        conference_id = self.kwargs.get('conference_id', '')
        return BattingStats.objects.filter(player__team__conference__id=conference_id).select_related('player', 'player__team')

# List pitching stats by conference
class PitchingStatsByConferenceView(generics.ListAPIView):
    serializer_class = PitchingStatsSerializer

    def get_queryset(self):
        conference_id = self.kwargs.get('conference_id', '')
        return PitchingStats.objects.filter(player__team__conference__id=conference_id).select_related('player', 'player__team')

# List batting stats by team
class BattingStatsByTeam(generics.ListAPIView):
    serializer_class = BattingStatsSerializer

    def get_queryset(self):
        team_id = self.kwargs.get('team_id', '')
        return BattingStats.objects.filter(player__team__id=team_id).select_related('player', 'player__team')

# List pitching stats by team
class PitchingStatsByTeam(generics.ListAPIView):
    serializer_class = PitchingStatsSerializer

    def get_queryset(self):
        team_id = self.kwargs.get('team_id', '')
        return PitchingStats.objects.filter(player__team__id=team_id).select_related('player', 'player__team')

class DivisionListView(generics.ListAPIView):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer

class ConferenceListView(generics.ListAPIView):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer

class ConferenceByDivisionListView(generics.ListAPIView):
    serializer_class = ConferenceSerializer

    def get_queryset(self):
        division_id = self.kwargs.get('division_id', '')
        return Conference.objects.filter(division_id=division_id)

class TeamListView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamByDivisionListView(generics.ListAPIView):
    serializer_class = TeamSerializer

    def get_queryset(self):
        division_id = self.kwargs.get('division_id', '')
        return Team.objects.filter(conference__division_id=division_id)

class TeamByConferenceListView(generics.ListAPIView):
    serializer_class = TeamSerializer
    
    def get_queryset(self):
        conference_id = self.kwargs.get('conference_id', '')
        return Team.objects.filter(conference__id=conference_id)

