import os

CONFIG_DIR = os.getenv("CONFIG_DIR") or "/config/"

KEEP_TEMP_FILES = os.getenv("KEEP_TEMP_FILES") or False
if not KEEP_TEMP_FILES and isinstance(os.getenv("MODE"), str):
    KEEP_TEMP_FILES = os.getenv("MODE").lower() == "development"
