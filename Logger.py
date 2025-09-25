import datetime
from enum import Enum

prefix = "MinePyWrapper"

class LogLevel(Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"

def Log(level: LogLevel, *args):
    now = datetime.datetime.now()
    timestamp = now.strftime("%H:%M:%S").zfill(8)
    print(f"[{timestamp}] [{prefix}/{level.value}] {' '.join(str(arg) for arg in args)}")

# test
Log(LogLevel.INFO, "Logger initialized", "Combined message test", 6, 7)