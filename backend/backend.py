from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, Session

app = FastAPI()

# Cnfigure the database connection
SQLALCHEMY_DATABSE_URL = "sqlite:///../database/stats.db"
engine = create_engine(SQLALCHEMY_DATABSE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define database models
class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    grade = Column(String)
    team_id = Column(Integer, ForeignKey("teams.id"))
    
    team = relationship("Team", back_populates="players")
    batting_stats = relationship("BattingStat", back_populates="player")
    pitching_stats = relationship("PitchingStat", back_populates="player")

class BattingStat(Base):
    __tablename__ = "batting_stats"

    player_id = Column(Integer, ForeignKey("players.id"), primary_key=True)
    g = Column(Integer)
    pa = Column(Integer)
    hr = Column(Integer)
    r = Column(Integer)
    rbi = Column(Integer)
    sb = Column(Integer)
    bb_percentage = Column(String)
    k_percentage = Column(String)
    iso = Column(String)
    babip = Column(String)
    avg = Column(String)
    obp = Column(String)
    slg = Column(String)
    woba = Column(String)
    wrc_plus = Column(Integer)

    player = relationship("Player", back_populates="batting_stats")

class PitchingStat(Base):
   __tablename__ = "pitching_stats"

   player_id = Column(Integer, ForeignKey("players.id"), primary_key=True)
   g = Column(Integer)
   gs = Column(Integer)
   ip = Column(String)
   k_per_9 = Column(String)
   bb_per_9 = Column(String)
   hr_per_9 = Column(String)
   babip = Column(String)
   era = Column(String)
   fip = Column(String)

   player = relationship("Player", back_populates="pitching_stats")

class Team(Base):
   __tablename__ = "teams"

   id = Column(Integer, primary_key=True, index=True)
   name = Column(String, index=True)
   conference_id = Column(Integer, ForeignKey("conferences.id"))

   conference = relationship("Conference", back_populates="teams")
   players = relationship("Player", back_populates="team")

class Conference(Base):
   __tablename__ = "conferences"

   id = Column(Integer, primary_key=True, index=True)
   name = Column(String, index=True)
   division_id = Column(Integer, ForeignKey("divisions.id"))

   division = relationship("Division", back_populates="conferences")
   teams = relationship("Team", back_populates="conference")


class Division(Base):
   __tablename__ = "divisions"

   id = Column(Integer, primary_key=True, index=True)
   name = Column(String, index=True)

   conferences = relationship("Conference", back_populates="division")

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API endpoints
@app.get("/teams/{team_id}/batting-stats")
def read_team_batting_stats(team_id: int, db: Session = Depends(get_db)):
    batting_stats = db.query(
        Player.name.label("player_name"),
        Player.grade,
        BattingStat.player_id,
        BattingStat.g,
        BattingStat.pa,
        BattingStat.hr,
        BattingStat.r,
        BattingStat.rbi,
        BattingStat.sb,
        BattingStat.bb_percentage,
        BattingStat.k_percentage,
        BattingStat.iso,
        BattingStat.babip,
        BattingStat.avg,
        BattingStat.obp,
        BattingStat.slg,
        BattingStat.woba,
        BattingStat.wrc_plus
    ).join(Player, BattingStat.player_id == Player.id)\
    .filter(Player.team_id == team_id).all()

    return [
        {
            "player_name": stat.player_name,
            "grade": stat.grade,
            "player_id": stat.player_id,
            "g": stat.g,
            "pa": stat.pa,
            "hr": stat.hr,
            "r": stat.r,
            "rbi": stat.rbi,
            "sb": stat.sb,
            "bb_percentage": stat.bb_percentage,
            "k_percentage": stat.k_percentage,
            "iso": stat.iso,
            "babip": stat.babip,
            "avg": stat.avg,
            "obp": stat.obp,
            "slg": stat.slg,
            "woba": stat.woba,
            "wrc_plus": stat.wrc_plus
        }
        for stat in batting_stats
    ]

@app.get("/teams/{team_id}/pitching-stats")
def read_team_pitching_stats(team_id: int, db: Session = Depends(get_db)):
    pitching_stats = db.query(
        Player.name.label("player_name"),
        Player.grade,
        PitchingStat.g,
        PitchingStat.gs,
        PitchingStat.ip,
        PitchingStat.k_per_9,
        PitchingStat.bb_per_9,
        PitchingStat.hr_per_9,
        PitchingStat.babip,
        PitchingStat.era,
        PitchingStat.fip
    ).join(Player, PitchingStat.player_id == Player.id)\
    .filter(Player.team_id == team_id).all()

    return [
        {
            "player_name": stat.player_name,
            "grade": stat.grade,
            "g": stat.g,
            "gs": stat.gs,
            "ip": stat.ip,
            "k_per_9": stat.k_per_9,
            "bb_per_9": stat.bb_per_9,
            "hr_per_9": stat.hr_per_9,
            "babip": stat.babip,
            "era": str(stat.era),
            "fip": str(stat.fip)
        }
        for stat in pitching_stats
    ]

@app.get("/conferences/{conference_id}/batting-stats")
def read_conference_batting_stats(conference_id: int, db: Session = Depends(get_db)):
    batting_stats = db.query(
        Team.name.label("team_name"),
        Player.name.label("player_name"),
        Player.grade,
        BattingStat.player_id,
        BattingStat.g,
        BattingStat.pa,
        BattingStat.hr,
        BattingStat.r,
        BattingStat.rbi,
        BattingStat.sb,
        BattingStat.bb_percentage,
        BattingStat.k_percentage,
        BattingStat.iso,
        BattingStat.babip,
        BattingStat.avg,
        BattingStat.obp,
        BattingStat.slg,
        BattingStat.woba,
        BattingStat.wrc_plus
    ).select_from(BattingStat)\
    .join(Player, BattingStat.player_id == Player.id)\
    .join(Team, Player.team_id == Team.id)\
    .join(Conference, Team.conference_id == Conference.id)\
    .filter(Conference.id == conference_id).all()
    
    batting_stats_dict = [
        {
            "team_name": stat.team_name,
            "player_name": stat.player_name,
            "grade": stat.grade,
            "player_id": stat.player_id,
            "g": stat.g,
            "pa": stat.pa,
            "hr": stat.hr,
            "r": stat.r,
            "rbi": stat.rbi,
            "sb": stat.sb,
            "bb_percentage": stat.bb_percentage,
            "k_percentage": stat.k_percentage,
            "iso": stat.iso,
            "babip": stat.babip,
            "avg": stat.avg,
            "obp": stat.obp,
            "slg": stat.slg,
            "woba": stat.woba,
            "wrc_plus": stat.wrc_plus
        }
        for stat in batting_stats
    ]
    
    return batting_stats_dict

@app.get("/conferences/{conference_id}/pitching-stats")
def read_conference_pitching_stats(conference_id: int, db: Session = Depends(get_db)):
    pitching_stats = db.query(
        Team.name.label("team_name"),
        Player.name.label("player_name"),
        Player.grade,
        PitchingStat.g,
        PitchingStat.gs,
        PitchingStat.ip,
        PitchingStat.k_per_9,
        PitchingStat.bb_per_9,
        PitchingStat.hr_per_9,
        PitchingStat.babip,
        PitchingStat.era,
        PitchingStat.fip
    ).select_from(PitchingStat)\
    .join(Player, PitchingStat.player_id == Player.id)\
    .join(Team, Player.team_id == Team.id)\
    .join(Conference, Team.conference_id == Conference.id)\
    .filter(Conference.id == conference_id).all()

    return [
        {
            "team_name": stat.team_name,
            "player_name": stat.player_name,
            "grade": stat.grade,
            "g": stat.g,
            "gs": stat.gs,
            "ip": stat.ip,
            "k_per_9": stat.k_per_9,
            "bb_per_9": stat.bb_per_9,
            "hr_per_9": stat.hr_per_9,
            "babip": stat.babip,
            "era": str(stat.era),
            "fip": str(stat.fip)
        }
        for stat in pitching_stats
    ]

@app.get("/divisions/{division_id}/conferences")
def read_division_conferences(division_id: int, db: Session = Depends(get_db)):
    conferences = db.query(Conference).filter(Conference.division_id == division_id).all()
    return conferences

@app.get("/conferences/{conference_id}/teams")
def read_conference_teams(conference_id: int, db: Session = Depends(get_db)):
    teams = db.query(Team).filter(Team.conference_id == conference_id).all()
    return teams