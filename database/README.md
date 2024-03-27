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
ba (Batting Average)
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