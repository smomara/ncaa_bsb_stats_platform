team_name <- function(team_id) {
  team_name <- load_teams() %>%
    filter(team_id == team_id) %>%
    select(school_name) %>%
    pull()
  team_name()
}