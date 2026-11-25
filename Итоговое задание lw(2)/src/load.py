from pathlib import Path
import pandas as pd


def load_trips(raw_dir, pattern="trips_*.csv"):
    files = sorted(Path(raw_dir).glob(pattern))
    if not files:
        raise FileNotFoundError(f"В папке {raw_dir} нет файлов по шаблону {pattern}")
    frames = [pd.read_csv(p, parse_dates=["date"]).assign(source_file=p.name) for p in files]
    return pd.concat(frames, ignore_index=True)
