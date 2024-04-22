from rest_framework import serializers
import math
from .models import Division, Conference, Team, Player, BattingStats, PitchingStats

class SafeFloatField(serializers.FloatField):
    def to_representation(self, value):
        if isinstance(value, float):
            if math.isinf(value):
                return 999.99
            if math.isnan(value):
                return None
        return super().to_representation(value)

class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = '__all__'

class ConferenceSerializer(serializers.ModelSerializer):
    division = DivisionSerializer(read_only=True)

    class Meta:
        model = Conference
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    conference = ConferenceSerializer(read_only=True)

    class Meta:
        model = Team
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    
    class Meta:
        model = Player
        fields = '__all__'

class BattingStatsSerializer(serializers.ModelSerializer):
    player = PlayerSerializer(read_only=True)
    qualified = serializers.SerializerMethodField()

    class Meta:
        model = BattingStats
        fields = '__all__'

    def get_qualified(self, obj):
        return obj.g >= obj.player.team.g * 0.75 and obj.pa >= 2 * obj.player.team.g if obj.player.team else False

class PitchingStatsSerializer(serializers.ModelSerializer):
    player = PlayerSerializer(read_only=True)
    g = SafeFloatField(allow_null=True)
    gs = SafeFloatField(allow_null=True)
    ip = SafeFloatField(allow_null=True)
    k_per_9 = SafeFloatField(allow_null=True)
    bb_per_9 = SafeFloatField(allow_null=True)
    hr_per_9 = SafeFloatField(allow_null=True)
    babip = SafeFloatField(allow_null=True)
    era = SafeFloatField(allow_null=True)
    fip = SafeFloatField(allow_null=True)
    qualified = serializers.SerializerMethodField()

    class Meta:
        model = PitchingStats
        fields = '__all__'

    def get_qualified(self, obj):
        return obj.ip >= obj.player.team.g if obj.player.team and obj.ip is not None else False