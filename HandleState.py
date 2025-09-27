import re
from enum import Enum

import Logger

# I used chatgpt for these regex statements: 
# "[HH:MM:SS] [Thread/Level]:"
LOG_PREFIX = re.compile(r"^\[\d{2}:\d{2}:\d{2}\] \[[^\]]+\]: ")
# "Playername joined the game"
PLAYER_JOINED_REGEX = r"^[^\s]+ joined the game"

class State(Enum):
    STARTING = "starting"
    RUNNING = "running"
    STOPPING = "stopping"
    STOPPED = "stopped"
    IDLE = "idle"

def strip_prefix(line: str) -> str:
    return LOG_PREFIX.sub("", line, count=1)

state: State = State.STARTING
_listeners = []

def add_listener(func: callable):
    _listeners.append(func)
    invoke_listeners()

def remove_listener(func: callable):
    if func in _listeners:
        _listeners.remove(func)

def update_state_from_line(line: str):
    msg = strip_prefix(line)

    state_table = {
        msg.startswith("Done ("): State.RUNNING,
        msg.startswith("Stopping the server"): State.STOPPING,
        msg.startswith("Server empty for 60 seconds, pausing"): State.IDLE,
        re.match(PLAYER_JOINED_REGEX, msg): State.RUNNING
    }

    new_state = None
    for condition in state_table:
        new_state_value = state_table[condition]
        if condition:
            new_state = new_state_value
            break

    set_state(new_state)

def invoke_listeners():
    for listener in _listeners:
        try:
            listener(state)
        except Exception as e:
            Logger.Log(Logger.LogLevel.ERROR, f"Listener error: {e}")

def set_state(new_state: State | None):
    global state
    if new_state != state and new_state is not None:
        state = new_state
        invoke_listeners()