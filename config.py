"""
Sector Rotation Analyzer V2
Configuration File
"""

from pathlib import Path
from datetime import datetime

# ======================================================
# PROJECT PATHS
# ======================================================

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

OUTPUT_DIR = BASE_DIR / "output"
LOG_DIR = BASE_DIR / "logs"

# Create folders automatically
for folder in [
    DATA_DIR,
    RAW_DIR,
    PROCESSED_DIR,
    OUTPUT_DIR,
    LOG_DIR,
]:
    folder.mkdir(parents=True, exist_ok=True)

# ======================================================
# DOWNLOAD SETTINGS
# ======================================================

START_DATE = "2010-01-01"
END_DATE = datetime.today().strftime("%Y-%m-%d")

INTERVAL = "1mo"
AUTO_ADJUST = False
MAX_RETRIES = 3
RETRY_DELAY = 3

# ======================================================
# OUTPUT FILES
# ======================================================

MASTER_CSV = PROCESSED_DIR / "master_returns.csv"

EXCEL_REPORT = OUTPUT_DIR / "Sector_Rotation_Report.xlsx"

PDF_REPORT = OUTPUT_DIR / "Sector_Rotation_Report.pdf"

# ======================================================
# LOG FILE
# ======================================================

LOG_FILE = LOG_DIR / "sector_rotation.log"

# ======================================================
# NIFTY SECTOR INDICES
# (Verified / Extendable)
# ======================================================

SECTORS = {

    "Nifty 50": "^NSEI",

    "Nifty Bank": "^NSEBANK",

    "Nifty Auto": "^CNXAUTO",

    "Nifty IT": "^CNXIT",

    "Nifty FMCG": "^CNXFMCG",

    "Nifty Metal": "^CNXMETAL",

    "Nifty Realty": "^CNXREALTY",

    "Nifty Pharma": "^CNXPHARMA",

    "Nifty Energy": "^CNXENERGY",

    "Nifty PSU Bank": "^CNXPSUBANK",

    "Nifty Media": "^CNXMEDIA",

    "Nifty Infrastructure": "^CNXINFRA",

    "Nifty Services": "^CNXSERVICE",
}
