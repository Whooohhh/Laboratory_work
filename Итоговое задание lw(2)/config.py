from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
REPORTS_DIR = BASE_DIR / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"
CHARTS_DIR = BASE_DIR / "charts"
DATA_PATTERN = "trips_*.csv"
OTD_TARGET = 90
HIST_BINS = 35
