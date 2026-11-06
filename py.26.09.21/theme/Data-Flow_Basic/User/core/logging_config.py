import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def configure_logging(directory: Path) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    root = logging.getLogger()
    if root.handlers:
        return
    root.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
    handler = RotatingFileHandler(directory / "dataflow.log", maxBytes=2_000_000, backupCount=4, encoding="utf-8")
    handler.setFormatter(formatter)
    root.addHandler(handler)
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    root.addHandler(console)
