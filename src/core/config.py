from dataclasses import dataclass


@dataclass
class Settings:

    MIN_SALARY = 3000000

    CITIES = [
        "Cali",
        "Palmira",
        "Cerrito",
        "Jamundí",
        "Remoto"
    ]

    SEARCH_INTERVAL = 120

    DATABASE = "data/jobhunter.db"

    LOG_FOLDER = "logs"

    CV = "cv/MauricioMurilloCV.pdf"


settings = Settings()