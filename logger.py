# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Osvaldo Cipriano (github.com/nunchuckcoder)
"""
Configuração de logging com rotação de ficheiros.

Níveis configuráveis via .env:
    LOG_LEVEL_FILE     (default INFO)
    LOG_LEVEL_CONSOLE  (default INFO)
"""
import logging
import os
from logging.handlers import RotatingFileHandler

LOG_LEVEL_FILE = os.getenv("LOG_LEVEL_FILE", "INFO").upper()
LOG_LEVEL_CONSOLE = os.getenv("LOG_LEVEL_CONSOLE", "INFO").upper()

logger = logging.getLogger("BotLogger")
logger.setLevel(logging.DEBUG)
logger.propagate = False

if not logger.handlers:
    fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    # Ficheiro com rotação: 5 ficheiros de 1 MB cada
    file_handler = RotatingFileHandler(
        "bot.log",
        maxBytes=1_000_000,
        backupCount=5,
        encoding="utf-8",
    )
    file_handler.setLevel(LOG_LEVEL_FILE)
    file_handler.setFormatter(fmt)
    logger.addHandler(file_handler)

    # Consola
    console_handler = logging.StreamHandler()
    console_handler.setLevel(LOG_LEVEL_CONSOLE)
    console_handler.setFormatter(fmt)
    logger.addHandler(console_handler)
