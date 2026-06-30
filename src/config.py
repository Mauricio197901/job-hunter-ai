"""
Configuración general del proyecto
"""

from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

DATABASE = BASE_DIR / "data" / "jobhunter.db"

LOGS = BASE_DIR / "logs"

CV = BASE_DIR / "cv" / "MauricioMurilloCV.pdf"

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")

EMAIL = os.getenv("EMAIL", "")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "")

HEADLESS = True

SALARIO_MINIMO = 3000000