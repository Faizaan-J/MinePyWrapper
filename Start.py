import subprocess
import os
from dotenv import load_dotenv
import ConfigHandler
import threading

from ColorMap import color_map

import Logger
from Events import Event

import HandleState
import HandleSneakyBans
import HandleStateStyles

load_dotenv()  # load .env file # copilot i dont need these fucking comments

script_dir = os.path.dirname(os.path.abspath(__file__))
jar_path = os.path.join(script_dir, "..", f"{ConfigHandler.config['jar_info']['jar_name']}.jar")

# i used chatgpt for these parameters i only understand that its between 2gb and 8gb of ram idk what anything else does
java_args = [
    "java",
    f"-Xms{ConfigHandler.config['jar_info']['min_ram']}",
    f"-Xmx{ConfigHandler.config['jar_info']['max_ram']}",
]

if "other_args" in ConfigHandler.config['jar_info']:
    java_args.extend(ConfigHandler.config['jar_info']['other_args'])

java_args.extend([
    "-jar", jar_path, "nogui"
])

server_process = subprocess.Popen(
    java_args,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
    bufsize=1,
    encoding="utf-8",
    errors="replace"
)

def on_state_change(new_state: HandleState.State):
    if new_state == HandleState.State.RUNNING:
        threading.Thread(target=HandleSneakyBans.handle_sneaky_ban, daemon=True).start()
        HandleState.OnStateChange.unsubscribe(on_state_change)
HandleState.OnStateChange.subscribe(on_state_change)

# how the fuck does this for loop keep running even for all lines that get added after that
# i think it's because it keeps waiting for more lines to some sort of "output stream"
# until the process ends in which in the stdout stream stops right
for line in server_process.stdout:
    print(line, end='')
    HandleState.update_state_from_line(line)

server_process.wait()
HandleState.set_state(HandleState.State.STOPPED)

Logger.Log(Logger.LogLevel.INFO, "Server process stopped!")
# It pauses in bat file