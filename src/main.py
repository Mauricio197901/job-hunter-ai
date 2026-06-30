from src.core.config import settings
from src.core.logger import logger


def main():
    logger.info("========================================")
    logger.info("JOB HUNTER AI")
    logger.info("========================================")
    logger.info(f"Ciudades objetivo: {settings.CITIES}")
    logger.info(f"Salario mínimo: ${settings.MIN_SALARY:,}")
    logger.info("Sistema iniciado correctamente.")


if __name__ == "__main__":
    main()