import pyarrow.parquet as pq
import pandas as pd
import json
from typing import List, Callable, Iterator, Union, Optional
from hoopR.config import MBB_BASE_URL, MBB_TEAM_BOX_URL, MBB_PLAYER_BOX_URL, MBB_TEAM_SCHEDULE_URL
from hoopR.errors import SeasonNotFoundError
from hoopR.dl_utils import download

def load_mbb_pbp(seasons: List[int]) -> pd.DataFrame:
    """Load men's college basketball play by play data going back to 2002

    Example:
        `mbb_df = hoopR.mbb.load_mbb_pbp(seasons=range(2002,2022))`

    Args:
        seasons (list): Used to define different seasons. 2002 is the earliest available season.

    Returns:
        pd.DataFrame: Pandas dataframe containing the
        play-by-plays available for the requested seasons.

    Raises:
        ValueError: If `season` is less than 2002.
    """
    data = pd.DataFrame()
    for i in seasons:
        if int(i) < 2002:
            raise SeasonNotFoundError("season cannot be less than 2002")
        i_data = pd.read_parquet(MBB_BASE_URL.format(season=i), engine='auto', columns=None)
        data = data.append(i_data)
    #Give each row a unique index
    data.reset_index(drop=True, inplace=True)
    return data

def load_mbb_team_boxscore(seasons: List[int]) -> pd.DataFrame:
    """Load men's college basketball team boxscore data

    Example:
        `mbb_df = hoopR.mbb.load_mbb_team_boxscore(seasons=range(2002,2022))`

    Args:
        seasons (list): Used to define different seasons. 2002 is the earliest available season.

    Returns:
        pd.DataFrame: Pandas dataframe containing the
        team boxscores available for the requested seasons.

    Raises:
        ValueError: If `season` is less than 2002.
    """
    data = pd.DataFrame()
    for i in seasons:
        if int(i) < 2002:
            raise SeasonNotFoundError("season cannot be less than 2002")
        i_data = pd.read_parquet(MBB_TEAM_BOX_URL.format(season = i), engine='auto', columns=None)
        data = data.append(i_data)
    #Give each row a unique index
    data.reset_index(drop=True, inplace=True)

    return data

def load_mbb_player_boxscore(seasons: List[int]) -> pd.DataFrame:
    """Load men's college basketball player boxscore data

    Example:
        `mbb_df = hoopR.mbb.load_mbb_player_boxscore(seasons=range(2002,2022))`

    Args:
        seasons (list): Used to define different seasons. 2002 is the earliest available season.

    Returns:
        pd.DataFrame: Pandas dataframe containing the
        player boxscores available for the requested seasons.

    Raises:
        ValueError: If `season` is less than 2002.
    """
    data = pd.DataFrame()
    for i in seasons:
        if int(i) < 2002:
            raise SeasonNotFoundError("season cannot be less than 2002")
        i_data = pd.read_parquet(MBB_PLAYER_BOX_URL.format(season = i), engine='auto', columns=None)
        data = data.append(i_data)
    #Give each row a unique index
    data.reset_index(drop=True, inplace=True)

    return data

def load_mbb_schedule(seasons: List[int]) -> pd.DataFrame:
    """Load men's college basketball schedule data

    Example:
        `mbb_df = hoopR.mbb.load_mbb_schedule(seasons=range(2002,2022))`

    Args:
        seasons (list): Used to define different seasons. 2002 is the earliest available season.

    Returns:
        pd.DataFrame: Pandas dataframe containing the
        schedule for  the requested seasons.

    Raises:
        ValueError: If `season` is less than 2002.
    """
    data = pd.DataFrame()
    for i in seasons:
        if int(i) < 2002:
            raise SeasonNotFoundError("season cannot be less than 2002")
        i_data = pd.read_parquet(MBB_TEAM_SCHEDULE_URL.format(season = i), engine='auto', columns=None)
        data = data.append(i_data)
    #Give each row a unique index
    data.reset_index(drop=True, inplace=True)

    return data


def mbb_calendar(season: int) -> pd.DataFrame:
    """mbb_calendar - look up the men's college basketball calendar for a given season

    Args:
        season (int): Used to define different seasons. 2002 is the earliest available season.

    Returns:
        pd.DataFrame: Pandas dataframe containing
        calendar dates for the requested season.

    Raises:
        ValueError: If `season` is less than 2002.
    """
    url = "http://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/scoreboard?dates={}".format(season)
    resp = download(url=url)
    txt = json.loads(resp)['leagues'][0]['calendar']
    reg = pd.DataFrame(txt[0]['entries'])
    post = pd.DataFrame(txt[1]['entries'])
    full_schedule = pd.concat([reg,post], ignore_index=True)
    full_schedule['season']=season
    return full_schedule


