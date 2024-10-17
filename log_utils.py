#!/usr/bin/env python3

import os
from datetime import datetime

# File to store the time logs
LOG_FILE = os.path.expanduser("~/.window_time_log")

def log_time(window_name: str, duration: float) -> None:
    """
    Log the window name and duration to the log file.
    
    Args:
        window_name (str): Name of the active window.
        duration (float): Duration of activity in seconds.
    """
    with open(LOG_FILE, "a") as f:
        print(f"printing to: {LOG_FILE}")
        f.write(f"{datetime.now()},{window_name},{duration}\n")

