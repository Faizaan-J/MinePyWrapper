import ConfigHandler
import HandleState

import os
from ColorMap import color_map

def set_title(title: str):
    os.system(f"title {title}")

def set_color(color_name: str):
    color_code = color_map.get(color_name, color_map["darkgray"])
    os.system(f"color {color_code}")

def on_state_change(new_state: HandleState.State):
    state_styles = ConfigHandler.config["state_styles"]
    set_title(state_styles[new_state.value]["title"])
    set_color(state_styles[new_state.value]["color"])

HandleState.add_listener(on_state_change)