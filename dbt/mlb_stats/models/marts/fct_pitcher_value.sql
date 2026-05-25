select
    player_name,
    team,
    games,
    games_started,
    innings_pitched,
    wins,
    era,
    whip,
    strikeouts_per_nine,
    strikeout_to_walk_ratio,
    walks,
    strikeouts,
    home_runs,
    batting_average_on_balls_in_play,
    round(
        ((1 / nullif(era, 0)) * 0.30) +
        ((1 / nullif(whip, 0)) * 0.25) +
        (strikeouts_per_nine * 0.25) +
        (strikeout_to_walk_ratio * 0.20),
    4) as pitcher_score

from {{ ref('stg_pitching') }}
where innings_pitched >= 20