select

NAME as player_name,
TEAM as team,
G as games,
GS as games_started,
IP as innings_pitched,
COALESCE(W, 0) as wins,
COALESCE(L, 0) as losses,
ERA as era,
WHIP as whip,
SO9 as strikeouts_per_nine,
SO_W as strikeout_to_walk_ratio,
BB as walks,
SO as strikeouts,
HR as home_runs,
BABIP as batting_average_on_balls_in_play,
SEASON as season,
INGESTED_AT as ingested_at

from {{ source('raw', 'RAW_PITCHING') }}
where IP >= 20