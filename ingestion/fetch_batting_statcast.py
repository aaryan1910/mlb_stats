import pandas as pd
from pybaseball import statcast_batter_expected_stats
from datetime import datetime

def fetch_batting_statcast(season=2026):
    print(f"Fetching Statcast batting stats for {season} season...")
    
    df = statcast_batter_expected_stats(season)
    
    columns = [
        "last_name, first_name", "player_id", "pa", "ba", "est_ba",
        "est_ba_minus_ba_diff", "slg", "est_slg",
        "est_slg_minus_slg_diff", "woba", "est_woba",
        "est_woba_minus_woba_diff"
    ]
    
    df = df[columns]
    
    df["season"] = season
    df["ingested_at"] = datetime.utcnow().isoformat()
    
    print(f"Fetched {len(df)} players")
    return df

if __name__ == "__main__":
    df = fetch_batting_statcast()
    print(df.head())
    print(f"Shape: {df.shape}")