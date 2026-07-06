"""
Sector Rotation Analyzer V2
Downloader Module
Part 1
"""

from pathlib import Path
from datetime import datetime
import logging
import time

import pandas as pd
import yfinance as yf
from tqdm import tqdm

# ===========================
# PATHS
# ===========================

BASE_DIR = Path(__file__).resolve().parent

RAW_DIR = BASE_DIR / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "downloader.log"

# ===========================
# LOGGING
# ===========================

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)

# ===========================
# SETTINGS
# ===========================

START_DATE = "2010-01-01"

END_DATE = datetime.today().strftime("%Y-%m-%d")

INTERVAL = "1mo"

MAX_RETRY = 3

# ===========================
# SECTORS
# ===========================

SECTORS = {

    "Nifty 50": "^NSEI",

    "Nifty Bank": "^NSEBANK",

    "Nifty Auto": "^CNXAUTO",

    "Nifty IT": "^CNXIT",

}
