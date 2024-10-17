#!/usr/bin/env python3

import subprocess
import time
import os
from datetime import datetime
import argparse
from analytics import analyze_window_usage, print_analytics

# File to store the time logs
log_file = os.path.expanduser("~/.window_time_log")

def get_active_window():
    try:
        win_id = subprocess.check_output(["xdotool", "getactivewindow"]).decode("utf-8").strip()
        win_name = subprocess.check_output(["xdotool", "getwindowname", win_id]).decode("utf-8").strip()
        return win_id, win_name
    except subprocess.CalledProcessError:
        return None, None

def get_idle_time():
    try:
        idle_time = int(subprocess.check_output(["xprintidle"]).decode("utf-8").strip()) / 1000
        return idle_time
    except subprocess.CalledProcessError:
        return 0

def log_time(window_name, duration):
    with open(log_file, "a") as f:
        print(f"printing to: {log_file}")
        f.write(f"{datetime.now()},{window_name},{duration}\n")

def track_windows():
    active_window = None
    start_time = time.time()
    
    while True:
        new_window, new_window_name = get_active_window()
        idle_time = get_idle_time()

        if idle_time < 10:  # Consider it active if idle time is less than 10 seconds
            if new_window != active_window:
                if active_window:
                    print(f"Active window: {new_window_name}")
                    duration = time.time() - start_time
                    log_time(active_window_name, duration)
                active_window = new_window
                active_window_name = new_window_name
                start_time = time.time()
        
        time.sleep(1)

def main():
    parser = argparse.ArgumentParser(description="Window usage tracker and analyzer")
    parser.add_argument("--analyze", action="store_true", help="Analyze the logged data")
    args = parser.parse_args()

    if args.analyze:
        analytics_results = analyze_window_usage(log_file)
        print_analytics(analytics_results)
    else:
        track_windows()

if __name__ == "__main__":
    main()
