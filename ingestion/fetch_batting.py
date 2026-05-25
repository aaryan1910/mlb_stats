import pandas as pd
from pybaseball import batting_stats_bref
from datetime import datetime

def fetch_batting_stats(season=2026):
    print(f"Fetching MLB batting stats for {season} season...")
    
    df = batting_stats_bref(season)
    
    # Keep only columns we need
    columns = [
        "Name", "Tm", "G", "AB", "BA", "OBP", 
        "SLG", "OPS", "HR", "RBI", "BB", "SO"
    ]
    
    df = df[columns]
    
    # Add metadata
    df["season"] = season
    df["ingested_at"] = datetime.utcnow().isoformat()
    
    print(f"Fetched {len(df)} players")
    return df

if __name__ == "__main__":
    df = fetch_batting_stats()
    print(df.head())
    print(f"Shape: {df.shape}")