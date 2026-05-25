select

NAME as player_name,
TEAM as team,
G as games,
AB as at_bats,
BA as batting_average,
OBP as on_base_percentage,
SLG as slugging_percentage,
OPS as on_base_plus_slugging,
HR as home_runs,
RBI as runs_batted_in,
BB as base_on_balls,
SO as strikeouts,
SEASON as season,
INGESTED_AT as ingested_at

from {{ source('raw', 'RAW_BATTING') }}
where G >= 20
