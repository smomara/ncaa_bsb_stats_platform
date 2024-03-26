load_teams <- function() {
  teams <- baseballr::load_ncaa_baseball_teams() %>% 
    dplyr::filter(year == 2024)
  teams
}