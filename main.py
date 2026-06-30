from datetime import datetime

from config import DATABASE
from database import engine
from logger import logger


def main():

    logger.info("Proyecto iniciado")

    print("=" * 60)
    print("JOB HUNTER AI")
    print("=" * 60)

    print("Inicio:", datetime.now())
    print("Base de datos:", DATABASE)
    print("Engine:", engine)

    print("Todo funcionando correctamente.")

    print("=" * 60)


if __name__ == "__main__":
    main()