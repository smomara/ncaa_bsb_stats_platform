from rest_framework import serializers
import math
from .models import Division, Conference, Team, Player, BattingStats, PitchingStats

class FormattedFloatField(serializers.FloatField):
    """ Custom FloatField that formats floating point numbers and handles inf and NaN. """

    def __init__(self, format_spec='0.3f', **kwargs):
        super().__init__(**kwargs)
        self.format_spec = format_spec

    def to_representation(self, value):
        if isinstance(value, float):
            if math.isinf(value):
                return 99.99
            elif math.isnan(value):
                return None
            return format(value, self.format_spec)
        return value

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
    g = serializers.IntegerField()
    pa = serializers.IntegerField()
    hr = serializers.IntegerField()
    r = serializers.IntegerField()
    rbi = serializers.IntegerField()
    sb = serializers.IntegerField()
    bb_percentage = serializers.FloatField()
    k_percentage = serializers.FloatField()
    iso = FormattedFloatField()
    babip = FormattedFloatField()
    avg = FormattedFloatField()
    obp = FormattedFloatField()
    slg = FormattedFloatField()
    woba = FormattedFloatField()
    wrc_plus = serializers.FloatField()
    qualified = serializers.SerializerMethodField()

    class Meta:
        model = BattingStats
        fields = '__all__'

    def get_qualified(self, obj):
        return obj.g >= obj.player.team.g * 0.75 and obj.pa >= 2 * obj.player.team.g if obj.player.team else False

class PitchingStatsSerializer(serializers.ModelSerializer):
    player = PlayerSerializer(read_only=True)
    g = serializers.IntegerField()
    gs = serializers.IntegerField()
    ip = serializers.FloatField()
    k_per_9 = serializers.FloatField()
    bb_per_9 = serializers.FloatField()
    hr_per_9 = serializers.FloatField()
    babip = FormattedFloatField()
    era = serializers.FloatField()
    fip = serializers.FloatField()
    qualified = serializers.SerializerMethodField()

    class Meta:
        model = PitchingStats
        fields = '__all__'

    def get_qualified(self, obj):
        return obj.ip >= obj.player.team.g if obj.player.team and obj.ip is not None else False