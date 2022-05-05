import re
import socket
from configparser import ConfigParser
from os import environ, path

ENV_APP_MODE = "APP_MODE"

CONFIG_NAMES = ("database", "secrets")
PATHS = SETTINGS = {}

parser = ConfigParser()

PATHS["APP_DIR"] = path.realpath(path.join(path.dirname(__file__), "../")) + "/"
PATHS["DATA_DIR"] = path.realpath(path.join(PATHS["APP_DIR"], "../../data")) + "/"
PATHS["CONFIG_DIR"] = path.realpath(path.join(PATHS["APP_DIR"], "../../conf")) + "/"
PATHS["STATIC_DIR"] = path.relpath(path.join(PATHS["APP_DIR"], "../../static")) + "/"

for config in CONFIG_NAMES:
    filepath = path.join(PATHS["CONFIG_DIR"], config)

    if not path.exists(filepath):
        continue

    with open(filepath, "r") as file:
        parser.read_string(f"[config]\n{file.read()}")

        for key, value in parser.items("config"):
            SETTINGS[key.upper()] = value
