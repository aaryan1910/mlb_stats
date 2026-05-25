select

LAST_NAME_FIRST_NAME as player_name,
PLAYER_ID as player_id,
PA as plate_appearances,
BA as batting_average,
EST_BA as estimated_batting_average,
EST_BA_MINUS_BA_DIFF as est_ba_minus_ba_diff,
SLG as slugging_percentage,
EST_SLG as estimated_slugging_percentage,
EST_SLG_MINUS_SLG_DIFF as est_slg_minus_slg_diff,
WOBA as weighted_on_base_average,
EST_WOBA as estimated_weighted_on_base_average,
EST_WOBA_MINUS_WOBA_DIFF as est_woba_minus_woba_diff,
SEASON as season,
INGESTED_AT as ingested_at

from {{ source('raw', 'RAW_BATTING_STATCAST') }}
where PA >= 50

