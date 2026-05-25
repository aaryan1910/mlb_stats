import pandas as pd
from pybaseball import pitching_stats_bref
from datetime import datetime

def fetch_pitching_stats(season=2026):
    print(f"Fetching MLB pitching stats for {season} season...")
    
    df = pitching_stats_bref(season)
    
    # Keep only columns we need
    columns = [
        "Name", "Tm", "G", "GS", "IP", "W", "L", 
        "ERA", "WHIP", "SO9", "SO/W", "BB", "SO", "HR", "BAbip"
    ]
    
    df = df[columns]
    
    # Add metadata
    df["season"] = season
    df["ingested_at"] = datetime.utcnow().isoformat()
    
    print(f"Fetched {len(df)} players")
    return df

if __name__ == "__main__":
    df = fetch_pitching_stats()
    print(df.head())
    print(f"Shape: {df.shape}")