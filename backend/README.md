# NCAA Baseball Stats Backend API

This is the backend API for the NCAA Baseball Stats platform, providing enpoints to retrieve baseball statistics and data from the database.. The API is built using FastAPI and integrated wit ha SQLite databse using SQLAlchemy.

## Current Status

Please note that this project is still a work in progress. The current implementation includes a basic structure and a few initial endpoints. More endpoints and features will be added in the future as the project evolves.

## API Endpoints
The following endpoints are currently available:
* `/teams/{team_id}/batting-stats`: Retrieve batting statistics for a specific team
* `/teams/{team_id}/pitching-stats`: Retrieve pitching statistics for a specific team
* `/conferences/{conference_id}/batting-stats`: Retrieve batting statistics for a specific conference
* `/conferences/{conference_id}/pitching-stats`: Retrieve pitching statistics for a specific conference
* `/divisions/{division_id}/conferences`: Retrieve conferences for a specific division
* `/conferences/{conference_id}/teams`: Retrieve teams for a specific conference
