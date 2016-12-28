def compute_away_streaks(v):
    is_away = v == 'away_team'
    season_away = is_away.cumsum()
    # Need to "reset" that count each time they go home
    home_games = v[~is_away].index
    # Subtract the `season_away` value for the prior away leg
    home_offset = pd.Series(season_away, index=home_games)
    offset = (home_offset
        .reindex(season_away.index)
        .fillna(method='ffill'))
    return season_away - offset
