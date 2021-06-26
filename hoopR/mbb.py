import pyarrow.parquet as pq
import pandas as pd
from typing import Callable, Iterator, Union, Optional, List
from hoopR.config import MBB_BASE_URL, MBB_TEAM_BOX_URL, MBB_PLAYER_BOX_URL, MBB_TEAM_SCHEDULE_URL
from hoopR.errors import SeasonNotFoundError

def load_mbb_pbp(years: List[int]) -> pd.DataFrame:
    """
    Load men's college basketball play by play data going back to 2003
    """
    data = pd.DataFrame()
    for i in years:
        i_data = pd.read_parquet(MBB_BASE_URL.format(year=i), engine='auto', columns=None, 
        use_nullable_dtypes=False)
        data = data.append(i_data)
    #Give each row a unique index
    data.reset_index(drop=True, inplace=True)
    return data

def load_mbb_team_boxscore(years: List[int]) -> pd.DataFrame:
    """
    Load men's college basketball team boxscore data
    """
    data = pd.DataFrame()
    for i in years:
        i_data = pd.read_parquet(MBB_TEAM_BOX_URL.format(year = i), engine='auto', columns=None, 
        use_nullable_dtypes=False)
        data = data.append(i_data)
    #Give each row a unique index
    data.reset_index(drop=True, inplace=True)

    return data

def load_mbb_player_boxscore(years: List[int]) -> pd.DataFrame:
    """
    Load men's college basketball player boxscore data
    """
    data = pd.DataFrame()
    for i in years:
        i_data = pd.read_parquet(MBB_PLAYER_BOX_URL.format(year = i), engine='auto', columns=None, 
        use_nullable_dtypes=False)
        data = data.append(i_data)
    #Give each row a unique index
    data.reset_index(drop=True, inplace=True)

    return data

def load_mbb_schedule(years: List[int]) -> pd.DataFrame:
    """
    Load men's college basketball schedule data
    """
    data = pd.DataFrame()
    for i in years:
        i_data = pd.read_parquet(MBB_TEAM_SCHEDULE_URL.format(year = i), engine='auto', columns=None, 
        use_nullable_dtypes=False)
        data = data.append(i_data)
    #Give each row a unique index
    data.reset_index(drop=True, inplace=True)

    return data





