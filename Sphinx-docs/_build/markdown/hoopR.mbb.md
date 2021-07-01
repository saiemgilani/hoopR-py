# hoopR.mbb package

## Module contents


### hoopR.mbb.load_mbb_pbp(seasons: List[int])
Load men’s college basketball play by play data going back to 2002

Example:

    mbb_df = hoopR.mbb.load_mbb_pbp(seasons=[range(2002,2022)])

Args:

    seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    pd.DataFrame: Pandas dataframe containing the
    play-by-plays available for the requested seasons.

Raises:

    ValueError: If season is less than 2002.


### hoopR.mbb.load_mbb_player_boxscore(seasons: List[int])
Load men’s college basketball player boxscore data

Example:

    mbb_df = hoopR.mbb.load_mbb_player_boxscore(seasons=[range(2002,2022)])

Args:

    seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    pd.DataFrame: Pandas dataframe containing the
    player boxscores available for the requested seasons.

Raises:

    ValueError: If season is less than 2002.


### hoopR.mbb.load_mbb_schedule(seasons: List[int])
Load men’s college basketball schedule data

Example:

    mbb_df = hoopR.mbb.load_mbb_schedule(seasons=[range(2002,2022)])

Args:

    seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    pd.DataFrame: Pandas dataframe containing the
    schedule for  the requested seasons.

Raises:

    ValueError: If season is less than 2002.


### hoopR.mbb.load_mbb_team_boxscore(seasons: List[int])
Load men’s college basketball team boxscore data

Example:

    mbb_df = hoopR.mbb.load_mbb_team_boxscore(seasons=[range(2002,2022)])

Args:

    seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    pd.DataFrame: Pandas dataframe containing the
    team boxscores available for the requested seasons.

Raises:

    ValueError: If season is less than 2002.


### hoopR.mbb.mbb_calendar(season: int)
mbb_calendar - look up the men’s college basketball calendar for a given season

Args:

    season (int): Used to define different seasons. 2002 is the earliest available season.

Returns:

    pd.DataFrame: Pandas dataframe containing
    calendar dates for the requested season.

Raises:

    ValueError: If season is less than 2002.
