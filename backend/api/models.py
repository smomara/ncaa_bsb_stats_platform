from django.db import models

class Division(models.Model):
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'divisions'

class Conference(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    division_id = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='conferences', db_column='division_id')
    
    class Meta:
        managed = False
        db_table = 'conferences'

class Team(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name='teams', db_column='conference_id')
    g = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teams'

class Player(models.Model):
    id = models.IntegerField(primary_key=True, blank=True, null=False)
    name = models.TextField(blank=True, null=True)
    grade = models.TextField(blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, db_column='team_id')
    
    class Meta:
        managed = False
        db_table = 'players'

class BattingStats(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE, primary_key=True, db_column='player_id')
    g = models.FloatField(blank=True, null=True)
    pa = models.FloatField(blank=True, null=True)
    hr = models.FloatField(blank=True, null=True)
    r = models.FloatField(blank=True, null=True)
    rbi = models.FloatField(blank=True, null=True)
    sb = models.FloatField(blank=True, null=True)
    bb_percentage = models.FloatField(blank=True, null=True)
    k_percentage = models.FloatField(blank=True, null=True)
    iso = models.FloatField(blank=True, null=True)
    babip = models.FloatField(blank=True, null=True)
    avg = models.FloatField(blank=True, null=True)
    obp = models.FloatField(blank=True, null=True)
    slg = models.FloatField(blank=True, null=True)
    woba = models.FloatField(blank=True, null=True)
    wrc_plus = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'batting_stats'

class PitchingStats(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE, primary_key=True, db_column='player_id')
    g = models.FloatField(blank=True, null=True)
    gs = models.FloatField(blank=True, null=True)
    ip = models.FloatField(blank=True, null=True)
    k_per_9 = models.FloatField(blank=True, null=True)
    bb_per_9 = models.FloatField(blank=True, null=True)
    hr_per_9 = models.FloatField(blank=True, null=True)
    babip = models.FloatField(blank=True, null=True)
    era = models.FloatField(blank=True, null=True)
    fip = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pitching_stats'
