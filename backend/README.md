# College Baseball API

This API provides endpoints to retrieve college baseball data, including batting stats, pitching stats, divisions, conferences, and teams.

## API Endpoints

### Batting Stats

#### List All Batting Stats
- Endpoint: `/api/batting-stats/`
- HTTP Method: GET
- Returns: A list of all batting stats with associated player information.

#### List Batting Stats by Conference
- Endpoint: `/api/batting-stats/conference/<conference_id>/`
- HTTP Method: GET
- URL Parameter: `<conference_id>` (integer) - The ID of the conference.
- Returns: A list of batting stats for players in the specified conference.

#### List Batting Stats by Team
- Endpoint: `/api/batting-stats/team/<team_id>/`
- HTTP Method: GET
- URL Parameter: `<team_id>` (integer) - The ID of the team.
- Returns: A list of batting stats for players in the specified team.

### Pitching Stats

#### List All Pitching Stats
- Endpoint: `/api/pitching-stats/`
- HTTP Method: GET
- Returns: A list of all pitching stats with associated player information.

#### List Pitching Stats by Conference
- Endpoint: `/api/pitching-stats/conference/<conference_id>/`
- HTTP Method: GET
- URL Parameter: `<conference_id>` (integer) - The ID of the conference.
- Returns: A list of pitching stats for players in the specified conference.

#### List Pitching Stats by Team
- Endpoint: `/api/pitching-stats/team/<team_id>/`
- HTTP Method: GET
- URL Parameter: `<team_id>` (integer) - The ID of the team.
- Returns: A list of pitching stats for players in the specified team.

### Divisions

#### List All Divisions
- Endpoint: `/api/divisions/`
- HTTP Method: GET
- Returns: A list of all divisions.

### Conferences

#### List All Conferences
- Endpoint: `/api/conferences/`
- HTTP Method: GET
- Returns: A list of all conferences with associated division information.

#### List Conferences by Division
- Endpoint: `/api/conferences/division/<division_id>/`
- HTTP Method: GET
- URL Parameter: `<division_id>` (integer) - The ID of the division.
- Returns: A list of conferences in the specified division.

### Teams

#### List All Teams
- Endpoint: `/api/teams/`
- HTTP Method: GET
- Returns: A list of all teams with associated conference information.

#### List Teams by Division
- Endpoint: `/api/teams/division/<division_id>/`
- HTTP Method: GET
- URL Parameter: `<division_id>` (integer) - The ID of the division.
- Returns: A list of teams in the specified division.

#### List Teams by Conference
- Endpoint: `/api/teams/conference/<conference_id>/`
- HTTP Method: GET
- URL Parameter: `<conference_id>` (integer) - The ID of the conference.
- Returns: A list of teams in the specified conference.

## Data Format

The API endpoints return data in JSON format. The returned data is serialized using the corresponding serializer classes defined in the `serializers.py` file. The serializers handle the conversion of model instances to JSON format and include related information based on the defined relationships between models.