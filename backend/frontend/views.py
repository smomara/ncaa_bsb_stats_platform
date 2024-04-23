import requests
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def all_teams(request):
    response = requests.get('http://ncaa-bsb-stats-40f08cc936de.herokuapp.com/api/conferences/')
    conferences = response.json()

    teams = requests.get('http://ncaa-bsb-stats-40f08cc936de.herokuapp.com/api/teams/').json()
    conference_teams_map = {conference['id']: [] for conference in conferences}
    for team in teams:
        conference_id = team['conference']['id']
        if conference_id in conference_teams_map:
            conference_teams_map[conference_id].append(team)
    for conference in conferences:
        conference['teams'] = conference_teams_map[conference['id']]

    divisions = {}
    for conference in conferences:
        division_id = conference.get('division_id')
        if division_id in divisions:
            divisions[division_id].append(conference)
        else:
            divisions[division_id] = [conference]
    sorted_divisions = sorted((int(k), v) for k, v in divisions.items())
    
    division_list = [{'id': div_id, 'conferences': confs} for div_id, confs in sorted_divisions]

    return render(request, 'teams.html', {'divisions': division_list})

def division_stats(request, division_id):
    batting_stats = requests.get(f'http://ncaa-bsb-stats-40f08cc936de.herokuapp.com/api/batting-stats/division/{division_id}/').json()
    pitching_stats = requests.get(f'http://ncaa-bsb-stats-40f08cc936de.herokuapp.com/api/pitching-stats/division/{division_id}/').json()

     # Sort batting stats by 'wrc_plus', descending (higher is better)
    batting_stats_sorted = sorted(batting_stats, key=lambda x: float(x.get('wrc_plus')) if x.get('wrc_plus') is not None else 0, reverse=True)

    # Sort pitching stats by 'fip', ascending (lower is better)
    pitching_stats_sorted = sorted(pitching_stats, key=lambda x: float(x.get('fip')) if x.get('fip') is not None else float(99.99))

    return render(request, 'division_stats.html', {
        'division': division_id,
        'batting_stats': batting_stats_sorted,
        'pitching_stats': pitching_stats_sorted
    })

def conference_stats(request, conference_id):
    conference = requests.get(f'http://ncaa-bsb-stats-40f08cc936de.herokuapp.com/api/conferences/{conference_id}/').json()
    batting_stats = requests.get(f'http://ncaa-bsb-stats-40f08cc936de.herokuapp.com/api/batting-stats/conference/{conference_id}/').json()
    pitching_stats = requests.get(f'http://ncaa-bsb-stats-40f08cc936de.herokuapp.com/api/pitching-stats/conference/{conference_id}/').json()

    # Sort batting stats by 'wrc_plus', descending (higher is better)
    batting_stats_sorted = sorted(batting_stats, key=lambda x: float(x.get('wrc_plus')) if x.get('wrc_plus') is not None else 0, reverse=True)

    # Sort pitching stats by 'fip', ascending (lower is better)
    pitching_stats_sorted = sorted(pitching_stats, key=lambda x: float(x.get('fip')) if x.get('fip') is not None else float(99.99))

    return render(request, 'conference_stats.html', {
        'conference_name': conference.get("name"),
        'batting_stats': batting_stats_sorted,
        'pitching_stats': pitching_stats_sorted
    })

def team_stats(request, team_id):
    team = requests.get(f'http://ncaa-bsb-stats-40f08cc936de.herokuapp.com/api/teams/{team_id}/').json()
    batting_stats = requests.get(f'http://ncaa-bsb-stats-40f08cc936de.herokuapp.com/api/batting-stats/team/{team_id}/').json()
    pitching_stats = requests.get(f'http://ncaa-bsb-stats-40f08cc936de.herokuapp.com/api/pitching-stats/team/{team_id}/').json()

     # Sort batting stats by 'wrc_plus', descending (higher is better)
    batting_stats_sorted = sorted(batting_stats, key=lambda x: float(x.get('wrc_plus')) if x.get('wrc_plus') is not None else 0, reverse=True)

    # Sort pitching stats by 'fip', ascending (lower is better)
    pitching_stats_sorted = sorted(pitching_stats, key=lambda x: float(x.get('fip')) if x.get('fip') is not None else float(99.99))

    return render(request, 'team_stats.html', {
        'team_name': team.get("name"),
        'batting_stats': batting_stats_sorted,
        'pitching_stats': pitching_stats_sorted
    })