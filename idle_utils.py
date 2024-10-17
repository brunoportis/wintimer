#!/usr/bin/env python3

import subprocess

def get_idle_time() -> float:
    """
    Get the current idle time in seconds.
    
    Returns:
        float: Idle time in seconds, or 0 if an error occurs.
    """
    try:
        idle_time = int(subprocess.check_output(["xprintidle"]).decode("utf-8").strip()) / 1000
        return idle_time
    except subprocess.CalledProcessError:
        return 0

