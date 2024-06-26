% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/team_stats.R
\name{team_stats}
\alias{team_stats}
\title{Retrieve and Process NCAA Baseball Team Statistics}
\usage{
team_stats(team_id)
}
\arguments{
\item{team_id}{Numeric or character. The unique identifier for the team whose statistics are being retrieved.}
}
\value{
A list of three dataframes:
- \code{player_info} contains common player information such as player ID, name, team, and division.
- \code{batting_stats} includes batting metrics like games played, plate appearances, home runs,
runs, RBIs, stolen bases, walk and strikeout percentages, ISO, BABIP, batting average,
on-base percentage, slugging percentage, wOBA, and wRC+.
- \code{pitching_stats} covers pitching metrics including games played, games started, innings pitched,
strikeouts per 9 innings, walks per 9 innings, home runs per 9 innings, BABIP, ERA, and FIP.
Each of the statistics dataframes also contains the player ID to link back to the \code{player_info} dataframe.
}
\description{
This function fetches and processes team statistics for an NCAA baseball team for the year 2024,
based on the team ID. It returns three dataframes: one with player information (\code{player_info}),
one with batting statistics (\code{batting_stats}), and one with pitching statistics (\code{pitching_stats}).
The function integrates park factor adjustments for batting statistics and offers detailed metrics
such as wOBA, wRC+, and others for batting, as well as FIP, K/9, and BABIP for pitching.
}
\examples{
stats <- team_stats(124)
player_info <- stats[[1]]
batting_stats <- stats[[2]]
pitching_stats <- stats[[3]]

}
