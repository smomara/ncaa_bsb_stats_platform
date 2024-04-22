from django.contrib import admin
from .models import Division, Conference, Team, Player, BattingStats, PitchingStats

admin.site.register(Division)
admin.site.register(Conference)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(BattingStats)
admin.site.register(PitchingStats)