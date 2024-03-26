base_pf <- function(team_id, type = "division") {
  pf <- baseballr::ncaa_park_factor(team_id, c(2019:2023), type)
  bpf <- pf$base_pf
  bpf
}