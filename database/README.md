# NCAA Baseball Sabermetrics Database

The database will store and manage the statistical data for NCAA baseball players, teams, conferences, and division.

## Database Schema

The database schema has not yet been finalized and the database has not yet been created. However, it is the next step since library development has been moving along.

The schema will need to include the following main tables:
* `players`: Stores information about individual players
* `teams`: Stores details about each team
* `conferences`: Stores details about each conference
* `divisions`: Stores information about each division (1-3)

Here's a preliminary schema diagram:

```
players
-------
id (PRIMARY KEY)
name
grade
team_id (FOREIGN KEY referencing teams.id)

batting_stats
-------------
player_id (FOREIGN KEY referencing players.id)
g (Games Played)
pa (Plate Appearances)
hr (Home Runs)
r (Runs)
rbi (Runs Batted In)
sb (Stolen Bases)
bb_percentage (Walk Percentage)
k_percentage (Strikeout Percentage)
iso (Isolated Power)
babip (Batting Average on Balls in Play)
avg (Batting Average)
obp (On-Base Percentage)
slg (Slugging Percentage)
woba (Weighted On-Base Average)
wrc_plus (Weighted Runs Created Plus)

pitching_stats
--------------
player_id (FOREIGN KEY referencing players.id)
g (Games Played)
gs (Games Started)
ip (Innings Pitched)
k_per_9 (Strikeouts Per 9 Innings)
bb_per_9 (Walks Per 9 Innings)
hr_per_9 (Home Runs Per 9 Innings)
babip (Batting Average on Balls in Play Against)
era (Earned Run Average)
fip (Fielding Independent Pitching)

teams
-----
id (PRIMARY KEY)
name
conference_id (FOREIGN KEY referencing conferences.id)

conferences
-----------
id (PRIMARY KEY)
name
division_id (FOREIGN KEY referencing divisions.id)

divisions
---------
id (PRIMARY KEY)
```

## Example SQL Queries

### Example 1

Retrieve the batting statistics of all the players in the "Landmark" conference with a wRC+ over 150 and over 50 plate appearances, then order them by wRC+:

```
SELECT t.name, p.name, bs.*
FROM batting_stats bs
JOIN players p ON bs.player_id = p.id
JOIN teams t ON p.team_id = t.id
JOIN conferences c ON t.conference_id = c.id
WHERE c.name = 'Landmark' AND bs.wrc_plus > 150 AND bs.pa > 50
ORDER BY bs.wrc_plus DESC
```

### Example 2

Retrieve the pitching stats of the 10 pitchers in Division II that have the lowest FIP and pitched over 10 innings:

```
SELECT t.name, p.name, ps.*
FROM pitching_stats ps
JOIN players p ON ps.player_id = p.id
JOIN teams t ON p.team_id = t.id
JOIN conferences c ON t.conference_id = c.id
JOIN divisions d ON c.division_id = d.id
WHERE d.id = '2' AND ps.ip > 10
ORDER BY ps.fip ASC
LIMIT 10
```