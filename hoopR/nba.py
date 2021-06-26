import pyarrow.parquet as pq
import pandas as pd
from typing import Callable, Iterator, Union, Optional, List
from hoopR.config import NBA_BASE_URL, NBA_TEAM_BOX_URL, NBA_PLAYER_BOX_URL, NBA_TEAM_SCHEDULE_URL
from hoopR.errors import SeasonNotFoundError

def load_nba_pbp(years: List[int]) -> pd.DataFrame:
    """
    Load NBA play by play data going back to 2003
    """
    data = pd.DataFrame()
    for i in years:
        i_data = pd.read_parquet(NBA_BASE_URL.format(year=i), engine='auto', columns=None, 
        use_nullable_dtypes=False)
        data = data.append(i_data)
    #Give each row a unique index
    data.reset_index(drop=True, inplace=True)
    return data

def load_nba_team_boxscore(years: List[int]) -> pd.DataFrame:
    """
    Load NBA team boxscore data
    """
    data = pd.DataFrame()
    for i in years:
        i_data = pd.read_parquet(NBA_TEAM_BOX_URL.format(year = i), engine='auto', columns=None, 
        use_nullable_dtypes=False)
        data = data.append(i_data)
    #Give each row a unique index
    data.reset_index(drop=True, inplace=True)

    return data

def load_nba_player_boxscore(years: List[int]) -> pd.DataFrame:
    """
    Load NBA player boxscore data
    """
    data = pd.DataFrame()
    for i in years:
        i_data = pd.read_parquet(NBA_PLAYER_BOX_URL.format(year = i), engine='auto', columns=None, 
        use_nullable_dtypes=False)
        data = data.append(i_data)
    #Give each row a unique index
    data.reset_index(drop=True, inplace=True)

    return data

def load_nba_schedule(years: List[int]) -> pd.DataFrame:
    """
    Load NBA schedule data
    """
    data = pd.DataFrame()
    for i in years:
        i_data = pd.read_parquet(NBA_TEAM_SCHEDULE_URL.format(year = i), engine='auto', columns=None, 
        use_nullable_dtypes=False)
        data = data.append(i_data)
    #Give each row a unique index
    data.reset_index(drop=True, inplace=True)

    return data





