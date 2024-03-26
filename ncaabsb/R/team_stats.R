team_stats <- function(team_id, type) {
  if (!type %in% c("pitching", "batting")) {
    stop("Invalid type specified. Please use 'pitching' or 'batting'.")
  }
  
  guts <- load_guts()
  team_stats <- baseballr::ncaa_team_player_stats(team_id, 2024, type)
  
  if (type == "batting") {
    park_factor <- park_factor(team_id)
    team_stats_processed <- team_stats %>%
      select(-player_url) %>%
      mutate(across(everything(), ~replace_na(.x, 0))) %>%
      mutate(across(c(AB, H, `2B`, `3B`, HR, BB, HBP, SF, SH), as.numeric)) %>%
      mutate(`1B` = H - `2B` - `3B` - HR, PA = AB + BB + HBP + SF + SH) %>%
      filter(PA != 0) %>%
      left_join(guts, by = c("division")) %>%
      mutate(wOBA = (wBB * BB + wHBP * HBP + w1B * `1B` + w2B * `2B` + w3B * `3B` + wHR * HR) / PA,
             wRAA = (wOBA - lgwOBA) / wOBAScale * PA,
             pf = park_factor,
             wRC_plus = (((wRAA / PA + `R.PA`) + (`R.PA` - pf * `R.PA`)) / `R.PA`) * 100,
             wOBA = round(wOBA, 3),
             wRC_plus = round(wRC_plus, 0),
             `BB%` = round(BB / PA * 100, 1),
             `K%` = round(K / PA * 100, 1),
             ISO = round(SlgPct - BA, 3),
             BABIP = round((H - HR) / (AB - HR - K + SF), 3)) %>%
      select(c("player_name", "GP", "PA", "HR", "R", "RBI", "SB", "BB%", "K%", "ISO", "BABIP", "BA", "OBPct", "SlgPct", "wOBA", "wRC_plus")) %>%
      arrange(desc(PA))
    
    return(team_stats_processed)
    
  } else if (type == "pitching") {
    team_stats_processed <- team_stats %>%
      filter(!str_detect(player_name, "Totals")) %>%
      mutate(across(everything(), ~replace_na(.x, 0))) %>%
      mutate(across(c(IP, SFA, BF, H, `2B-A`, `3B-A`, `HR-A`, BB, HB, SO), as.numeric)) %>%
      filter(BF != 0) %>%
      left_join(guts, by = c("division")) %>%
      mutate(IPx = floor(IP) + (IP - floor(IP)) * (10/3),
             FIP = round(get_fip(.), 2),
             `K/9` = round((SO / IPx) * 9, 2),
             `BB/9` = round((BB / IPx) * 9, 2),
             `HR/9` = round((`HR-A` / IPx) * 9, 2),
             BABIP = round((H - `HR-A`) / (BF - SO - `HR-A` + SFA), 3)) %>%
      select(c("player_name", "GP", "GS", "IP", "K/9", "BB/9", "HR/9", "BABIP", "ERA", "FIP")) %>%
      arrange(desc(IP))
    
    return(team_stats_processed)
  }
}