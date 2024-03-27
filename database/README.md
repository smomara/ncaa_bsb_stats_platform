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
position (pitcher/hitter)
team_id (FOREIGN KEY referencing teams.id)
[stat_columns]

teams
-----
id (PRIMARY KEY)
name
university
conference_id (FOREIGN KEY referencing conferences.id)

conferences
-----------
id (PRIMARY KEY)
name
division_id (FOREIGN KEY referencing divisions.id)

divisions
---------
id (PRIMARY KEY)
name
```