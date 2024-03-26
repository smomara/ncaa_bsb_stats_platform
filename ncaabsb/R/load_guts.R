load_guts <- function() {
  url <- "https://raw.githubusercontent.com/smomara/ncaa_bsb_stats_platform/main/ncaabsb/data/guts.csv"
  guts <- read.csv(url) %>%
    rename(lgwOBA = wOBA) %>%
    filter(season == 2023) %>%
    select(-season)
  guts
}