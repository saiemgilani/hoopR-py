---
title: Load MBB Team Boxscore
sidebar_label: Load MBB Team Boxscore
---

### hoopR.mbb.load_mbb_team_boxscore(seasons: List[int])
Load men’s college basketball team boxscore data

Example:

    mbb_df = hoopR.mbb.load_mbb_team_boxscore(seasons=range(2002,2022))

Args:

    seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    pd.DataFrame: Pandas dataframe containing the
    team boxscores available for the requested seasons.

Raises:

    ValueError: If season is less than 2002.

