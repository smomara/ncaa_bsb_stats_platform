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
ID (PRIMARY KEY)
Name
Team_ID (FOREIGN KEY referencing teams.id)
Conference_ID (FOREIGN KEY referencing conferences.id)
Division_ID (References a division category, not a FOREIGN KEY in this schema)

batting_stats
-------------
ID (FOREIGN KEY referencing players.ID)
GP (Games Played)
PA (Plate Appearances)
HR (Home Runs)
R (Runs)
RBI (Runs Batted In)
SB (Stolen Bases)
BB% (Walk Percentage)
K% (Strikeout Percentage)
ISO (Isolated Power)
BABIP (Batting Average on Balls in Play)
BA (Batting Average)
OBP (On-Base Percentage)
SLG (Slugging Percentage)
wOBA (Weighted On-Base Average)
wRC+ (Weighted Runs Created Plus)

pitching_stats
--------------
ID (FOREIGN KEY referencing players.ID)
GP (Games Played)
GS (Games Started)
IP (Innings Pitched)
K/9 (Strikeouts Per 9 Innings)
BB/9 (Walks Per 9 Innings)
HR/9 (Home Runs Per 9 Innings)
BABIP (Batting Average on Balls in Play Against)
ERA (Earned Run Average)
FIP (Fielding Independent Pitching)

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