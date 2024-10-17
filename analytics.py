import pandas as pd
from datetime import datetime, timedelta
from rich.console import Console
from rich.table import Table
from rich import box

def analyze_window_usage(log_file):
    """
    Analyze window usage data from the log file.
    
    :param log_file: Path to the log file
    :return: Dictionary containing analytics results
    """
    df = pd.read_csv(log_file, names=['timestamp', 'window_name', 'duration'])
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Calculate total time spent
    total_time = df['duration'].sum()
    
    # Calculate time spent per window
    time_per_window = df.groupby('window_name')['duration'].sum().sort_values()
    
    # Calculate percentage of time spent per window
    percentage_per_window = (time_per_window / total_time * 100).round(2)
    
    # Get most used windows
    most_used_windows = percentage_per_window.head(5)
    
    # Calculate daily usage
    df['date'] = df['timestamp'].dt.date
    daily_usage = df.groupby('date')['duration'].sum()
    
    return {
        'total_time': str(timedelta(seconds=int(total_time))),
        'time_per_window': time_per_window.to_dict(),
        'percentage_per_window': percentage_per_window.to_dict(),
        'most_used_windows': most_used_windows.to_dict(),
        'daily_usage': daily_usage.to_dict()
    }

def print_analytics(analytics_results):
    """
    Print the analytics results in a readable format using rich.
    
    :param analytics_results: Dictionary containing analytics results
    """
    console = Console()

    console.print("[bold blue]Window Usage Analytics:[/bold blue]")
    console.print(f"Total time tracked: [green]{analytics_results['total_time']}[/green]")
    
    # Top 5 Most Used Windows
    console.print("\n[bold blue]Top 5 Most Used Windows:[/bold blue]")
    top_windows_table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
    top_windows_table.add_column("Window", style="dim", width=40)
    top_windows_table.add_column("Usage", justify="right")
    
    for window, percentage in analytics_results['most_used_windows'].items():
        top_windows_table.add_row(window, f"{percentage:.2f}%")
    
    console.print(top_windows_table)
    
    # Daily Usage
    console.print("\n[bold blue]Daily Usage:[/bold blue]")
    daily_usage_table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
    daily_usage_table.add_column("Date", style="dim")
    daily_usage_table.add_column("Duration", justify="right")
    
    for date, duration in analytics_results['daily_usage'].items():
        daily_usage_table.add_row(str(date), str(timedelta(seconds=int(duration))))
    
    console.print(daily_usage_table)
