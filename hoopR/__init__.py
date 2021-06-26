import pyarrow.parquet as pq
import pandas as pd
from typing import Callable, Iterator, Union, Optional, List
from hoopR.config import MBB_BASE_URL, MBB_ROSTER_URL, MBB_TEAM_LOGO_URL, MBB_TEAM_SCHEDULE_URL, MBB_TEAM_INFO_URL
from hoopR.errors import SeasonNotFoundError

