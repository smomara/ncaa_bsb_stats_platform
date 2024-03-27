# NCAA Baseball Statistics Database Updater
# 
# This script updates an SQLite database named "stats.db" with the latest NCAA baseball statistics.
# It adds three tables to the database: `players`, `batting_stats`, and `pitching_stats`.
# 
# Tables:
# - `players`: Contains information about each player, including player ID, name, team, conference,
#   and division, with unique IDs for each entity (team, conference, division).
# - `batting_stats`: Stores batting statistics for each player, linked by player ID. Includes metrics
#   such as games played, plate appearances, home runs, batting average, and more.
# - `pitching_stats`: Stores pitching statistics for each player, linked by player ID. Contains metrics
#   such as innings pitched, strikeouts per 9 innings, earned run average (ERA), and more.
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

con <- dbConnect(RSQLite::SQLite(), "stats.db")

dbBegin(con)

prog <- txtProgressBar(min = 0, max = nrow(teams), style = 3)

for(i in 1:nrow(teams)) {
  tryCatch({
    stats <- ncaabsb::team_stats(teams$team_id[i])
    
    player_info <- as.data.frame(stats[[1]])
    batting_stats <- as.data.frame(stats[[2]])
    pitching_stats <- as.data.frame(stats[[3]])
    
    if (i == 1) {
      dbWriteTable(con, "players", player_info, overwrite = TRUE)
      dbWriteTable(con, "batting_stats", batting_stats, overwrite = TRUE)
      dbWriteTable(con, "pitching_stats", pitching_stats, overwrite = TRUE)
    } else {
      dbWriteTable(con, "players", player_info, append = TRUE)
      dbWriteTable(con, "batting_stats", batting_stats, append = TRUE)
      dbWriteTable(con, "pitching_stats", pitching_stats, append = TRUE)
    }
  }, error = function(e) {
    cat("Error in processing team", i, ": ", e$message, "\n")
  })
  
  setTxtProgressBar(prog, i)
}

dbCommit(con)

close(prog)

dbDisconnect(con)