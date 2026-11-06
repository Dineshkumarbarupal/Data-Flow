from __future__ import annotations
import logging
from pathlib import Path
import eel
from core.logging_config import configure_logging
from db.database import initialize_database
from py.api.system_api import register_system_api

USER_DIR = Path(__file__).resolve().parent

def main() -> None:
    configure_logging(USER_DIR / "data" / "logs")
    logger = logging.getLogger("dataflow")
    try:
        initialize_database(USER_DIR / "data" / "dataflow.sqlite3")
        # Serve from User/ so web/index.html can load sibling css/ and js/ assets.
        eel.init(str(USER_DIR), allowed_extensions=[".js", ".html", ".css"])
        register_system_api()
        eel.start("web/index.html", mode="edge", size=(1440, 900), position=(80, 60), block=True)
    except Exception:
        logger.exception("Data-Flow failed to start")
        raise

if __name__ == "__main__":
    main()
