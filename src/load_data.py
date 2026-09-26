from pathlib import Path
import pandas as pd

# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Raw data directory
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"


def load_games():
    """Load the historical NBA games dataset."""
    path = RAW_DATA_DIR / "Games.csv"
    return pd.read_csv(path)


def load_betting():
    """Load the historical NBA betting dataset."""
    path = RAW_DATA_DIR / "BettingLines.csv"
    return pd.read_csv(path)


def load_team_histories():
    """Load the NBA team histories dataset."""
    path = RAW_DATA_DIR / "TeamHistories.csv"
    return pd.read_csv(path)


if __name__ == "__main__":
    games = load_games()
    betting = load_betting()
    teams = load_team_histories()

    print("Games:", games.shape)
    print("Betting:", betting.shape)
    print("Team Histories:", teams.shape)

