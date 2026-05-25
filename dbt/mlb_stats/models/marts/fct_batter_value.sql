select
    b.player_name,
    b.team,
    b.games,
    b.batting_average,
    b.on_base_percentage,
    b.slugging_percentage,
    b.on_base_plus_slugging,
    b.home_runs,
    b.runs_batted_in,
    b.strikeouts,
    s.plate_appearances,
    s.weighted_on_base_average,
    s.estimated_weighted_on_base_average,
    s.est_woba_minus_woba_diff,
    round(
        (b.on_base_plus_slugging * 0.30) +
        (s.weighted_on_base_average * 0.35) +
        (s.estimated_weighted_on_base_average * 0.35),
    4) as batter_score

from {{ ref('stg_batting') }} as b
join {{ ref('stg_batting_statcast') }} as s
    on b.player_name = 
       trim(split_part(s.player_name, ',', 2)) || ' ' || trim(split_part(s.player_name, ',', 1))