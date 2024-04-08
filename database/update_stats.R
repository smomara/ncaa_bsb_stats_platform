# NCAA Baseball Statistics Database Updater
#
# This script updates an SQLite database named "stats.db" with the latest NCAA baseball statistics.
# It adds five tables to the database: `players`, `batting_stats`, `pitching_stats`, `teams`, 
# `conferences`, and `divisions`.
#
# Tables:
# - `players`: Contains information about each player, including player ID, name, team, conference,
#   and division, with foreign keys referencing the respective tables.
# - `batting_stats`: Stores batting statistics for each player, linked by player ID. Includes metrics
#   such as games played, plate appearances, home runs, batting average, and more.
# - `pitching_stats`: Stores pitching statistics for each player, linked by player ID. Contains metrics
#   such as innings pitched, strikeouts per 9 innings, earned run average (ERA), and more.
# - `teams`: Contains team information, including team ID and name, with a foreign key referencing
#   the conferences table.
# - `conferences`: Contains conference information, including conference ID and name.
# - `divisions`: Contains division information, including division ID and name.
#
# The script iterates through all teams loaded from the `ncaabsb` package, fetching and processing
# team stats for player information, batting, and pitching. It updates the database daily with new
# statistics, ensuring that the `stats.db` file reflects the most current data available.
#
# Dependencies: DBI, RSQLite, tidyverse, ncaabsb, svMisc

library(DBI)
library(RSQLite)
library(tidyverse)
library(ncaabsb)
library(svMisc)

teams <- ncaabsb::load_teams()

teams <- as.data.frame(teams) %>% filter(conference == "Landmark")

con <- dbConnect(RSQLite::SQLite(), "stats.db")
dbBegin(con)

dbWriteTable(con, "teams", unique(teams[, c("team_id", "team_name", "conference_id")]) %>%
               rename(id = team_id, name = team_name), overwrite = TRUE)
dbWriteTable(con, "conferences", unique(teams[, c("conference_id", "conference")]) %>%
               rename(id = conference_id, name = conference), overwrite = TRUE)
dbWriteTable(con, "divisions", data.frame(division = unique(teams$division), stringsAsFactors = FALSE) %>%
               rename(id = division), overwrite = TRUE)

prog <- txtProgressBar(min = 0, max = nrow(teams), style = 3)
for(i in 1:nrow(teams)) {
  tryCatch({
    stats <- ncaabsb::team_stats(teams$team_id[i])
    player_info <- as.data.frame(stats[[1]])
    batting_stats <- as.data.frame(stats[[2]])
    pitching_stats <- as.data.frame(stats[[3]])
    
    schedule <- baseballr::ncaa_schedule_info(teams$team_id[i], 2024)
    team_g = sum(!is.na(schedule$contest_id))
    teams$g[i] = team_g
    
    if (i == 1) {
      dbWriteTable(con, "players", player_info[, c("id", "name", "grade", "team_id")], overwrite = TRUE)
      dbWriteTable(con, "batting_stats", batting_stats[, c("player_id", "g", "pa", "hr", "r", "rbi", "sb", "bb_percentage", "k_percentage", "iso", "babip", "avg", "obp", "slg", "woba", "wrc_plus")], overwrite = TRUE)
      dbWriteTable(con, "pitching_stats", pitching_stats[, c("player_id", "g", "gs", "ip", "k_per_9", "bb_per_9", "hr_per_9", "babip", "era", "fip")], overwrite = TRUE)
    } else {
      dbWriteTable(con, "players", player_info[, c("id", "name", "grade", "team_id")] %>%
                     rename(team_id = team_id), append = TRUE)
      dbWriteTable(con, "batting_stats", batting_stats[, c("player_id", "g", "pa", "hr", "r", "rbi", "sb", "bb_percentage", "k_percentage", "iso", "babip", "avg", "obp", "slg", "woba", "wrc_plus")], append = TRUE)
      dbWriteTable(con, "pitching_stats", pitching_stats[, c("player_id", "g", "gs", "ip", "k_per_9", "bb_per_9", "hr_per_9", "babip", "era", "fip")], append = TRUE)
    }
    
  }, error = function(e) {
    cat("Error in processing team", i, ": ", e$message, "\n")
  })
  setTxtProgressBar(prog, i)
}

dbExecute(con, "ALTER TABLE teams ADD COLUMN g INTEGER")
for(i in 1:nrow(teams)) {
  team_g <- teams$g[i]
  team_id <- teams$team_id[i]
  dbExecute(con, "UPDATE teams SET g = ? WHERE id = ?", list(team_g, team_id))
}

dbCommit(con)
close(prog)
dbDisconnect(con)