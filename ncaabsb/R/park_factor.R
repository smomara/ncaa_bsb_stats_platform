park_factor <- function(team_id) {
  schedule <- baseballr::ncaa_schedule_info(team_id, 2024)
  valid_games <- schedule[!is.na(schedule$contest_id), ]

  if (nrow(valid_games) == 0) {
    1
  }

  total_games <- nrow(valid_games)
  home_games <- sum(valid_games$home_team_id == team_id, na.rm = TRUE)

  base_park_factor_value <- base_park_factor(team_id)

  adjustment_factor <- abs(base_park_factor_value - 1) * (home_games / total_games)
  home_game_adj <- base_pf_value + adjustment_factor * ifelse(base_pf_value > 1, -1, 1)
  pf <- 1 - (1 - home_game_adj) * 0.6

  pf
}