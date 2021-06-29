# hoopR package

## Submodules

## hoopR.config module

## hoopR.dl_utils module


### hoopR.dl_utils.download(url, num_retries=5)
## hoopR.errors module

Custom exceptions for hoopR module


### exception hoopR.errors.SeasonNotFoundError()
Bases: `Exception`

## hoopR.mbb module


### hoopR.mbb.load_mbb_pbp(seasons: List[int])
Load men’s college basketball play by play data going back to 2002
Args:

> seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    pbp_df (pandas dataframe): Pandas dataframe containing
    play-by-plays available for the requested seasons.

Raises:

    ValueError: If season is less than 2002.


### hoopR.mbb.load_mbb_player_boxscore(seasons: List[int])
Load men’s college basketball player boxscore data
Args:

> seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    player_boxscore_df (pandas dataframe): Pandas dataframe containing the
    player boxscores available for the requested seasons.

Raises:

    ValueError: If season is less than 2002.


### hoopR.mbb.load_mbb_schedule(seasons: List[int])
Load men’s college basketball schedule data
Args:

> seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    schedule_df (pandas dataframe): Pandas dataframe containing the
    schedule for  the requested seasons.

Raises:

    ValueError: If season is less than 2002.


### hoopR.mbb.load_mbb_team_boxscore(seasons: List[int])
Load men’s college basketball team boxscore data
Args:

> seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    team_boxscore_df (pandas dataframe): Pandas dataframe containing the
    team boxscores available for the requested seasons.

Raises:

    ValueError: If season is less than 2002.

## hoopR.nba module


### hoopR.nba.load_nba_pbp(seasons: List[int])
Load NBA play by play data going back to 2002
Args:

> seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    pbp_df (pandas dataframe): Pandas dataframe containing
    play-by-plays available for the requested seasons.

Raises:

    ValueError: If season is less than 2002.


### hoopR.nba.load_nba_player_boxscore(seasons: List[int])
Load NBA player boxscore data
Args:

> seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    player_boxscore_df (pandas dataframe): Pandas dataframe containing the
    player boxscores available for the requested seasons.

Raises:

    ValueError: If season is less than 2002.


### hoopR.nba.load_nba_schedule(seasons: List[int])
Load NBA schedule data
Args:

> seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    schedule_df (pandas dataframe): Pandas dataframe containing the
    schedule for  the requested seasons.

Raises:

    ValueError: If season is less than 2002.


### hoopR.nba.load_nba_team_boxscore(seasons: List[int])
Load NBA team boxscore data
Args:

> seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    team_boxscore_df (pandas dataframe): Pandas dataframe containing the
    team boxscores available for the requested seasons.

Raises:

    ValueError: If season is less than 2002.

## hoopR.schedule module


### hoopR.schedule.mbb_calendar(season: int)

### hoopR.schedule.nba_calendar(season: int)
## Module contents
