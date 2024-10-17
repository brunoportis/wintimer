#!/usr/bin/env python3

import subprocess
from typing import Tuple, Optional

def get_active_window() -> Tuple[Optional[str], Optional[str]]:
    """
    Get the active window ID and name.
    
    Returns:
        Tuple[Optional[str], Optional[str]]: Window ID and name, or (None, None) if an error occurs.
    """
    try:
        win_id = subprocess.check_output(["xdotool", "getactivewindow"]).decode("utf-8").strip()
        win_name = subprocess.check_output(["xdotool", "getwindowname", win_id]).decode("utf-8").strip()
        return win_id, win_name
    except subprocess.CalledProcessError:
        return None, None

