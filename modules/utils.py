from datetime import datetime

import psutil

from modules.const import DATETIME_FORMAT


def get_current_cpu() -> float:
    return psutil.cpu_percent()


def get_current_ram() -> float:
    return psutil.virtual_memory().percent


def get_current_time() -> str:
    return datetime.now().strftime(DATETIME_FORMAT)
