# hoopR.nba package

## Module contents


### hoopR.nba.load_nba_pbp(seasons: List[int])
Load NBA play by play data going back to 2002

Example:

    nba_df = hoopR.nba.load_nba_pbp(seasons=[range(2002,2022)])

Args:

    seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    pd.DataFrame: Pandas dataframe containing the
    play-by-plays available for the requested seasons.

Raises:

    ValueError: If season is less than 2002.


### hoopR.nba.load_nba_player_boxscore(seasons: List[int])
Load NBA player boxscore data

Example:

    nba_df = hoopR.nba.load_nba_player_boxscore(seasons=[range(2002,2022)])

Args:

    seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    pd.DataFrame: Pandas dataframe containing the
    player boxscores available for the requested seasons.

Raises:

    ValueError: If season is less than 2002.


### hoopR.nba.load_nba_schedule(seasons: List[int])
Load NBA schedule data

Example:

    nba_df = hoopR.nba.load_nba_schedule(seasons=[range(2002,2022)])

Args:

    seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    pd.DataFrame: Pandas dataframe containing the
    schedule for  the requested seasons.

Raises:

    ValueError: If season is less than 2002.


### hoopR.nba.load_nba_team_boxscore(seasons: List[int])
Load NBA team boxscore data

Example:

    nba_df = hoopR.nba.load_nba_team_boxscore(seasons=[range(2002,2022)])

Args:

    seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    pd.DataFrame: Pandas dataframe containing the
    team boxscores available for the requested seasons.

Raises:

    ValueError: If season is less than 2002.


### hoopR.nba.nba_calendar(season: int)
nba_calendar - look up the NBA calendar for a given season

Args:

    season (int): Used to define different seasons. 2002 is the earliest available season.

Returns:

    pd.DataFrame: Pandas dataframe containing
    calendar dates for the requested season.

Raises:

    ValueError: If season is less than 2002.
