import logging

from app.db.session import SessionLocal
from tenacity import (after_log, before_log, retry, stop_after_attempt,
                      wait_fixed)
from sqlalchemy import text


logging.basicConfig(
    format='%(asctime)s [%(levelname)s] -- %(filename)s[%(lineno)d] --  %(message)s',
    filename="backend.log",
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S %Z'
)
logger = logging.getLogger()

max_tries = 60 * 5  # 5 minutes
wait_seconds = 1


@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
def init() -> None:
    try:
        db = SessionLocal()
        # Try to create session to check if DB is awake
        cursor = db.execute(text("CREATE EXTENSION IF NOT EXISTS pg_trgm;"))
        db.commit()
        cursor.close()

        cursor = db.execute(text("CREATE EXTENSION IF NOT EXISTS unaccent;"))
        db.commit()
        cursor.close()

    except Exception as e:
        logger.error(e)
        raise e


def main() -> None:
    logger.info("Initializing service")
    init()
    logger.info("Service finished initializing")


if __name__ == "__main__":
    main()
