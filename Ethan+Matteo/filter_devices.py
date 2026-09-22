import pandas as pd
from wifi_parser import clean_table

"""
Printers, routers, and other devices that can connect to wifi shouldn't be counted 
as people in our data. The goal of this file is to filter out any device that shouldn't
be counted.
"""

CSV_PATH = "2014_01.csv"

def count_windows_per_client(df: pd.DataFrame, ap: str) -> pd.Series:
    """
    TODO:
    For a single AP, count how many distinct time windows each client
    appears in. This is the core signal for spotting "always-on" devices:
    a real person should appear in relatively few windows across a day,
    while infrastructure will appear in almost all of them.
 
    Args:
        df: the full (non-windowed) WiFi DataFrame, with "timestamp",
            "client", "AP" columns (timestamp already converted to
            datetime -- reuse that from wifi_parser.py).
        ap: which AP to analyze, e.g. "Bldg44AP10"
 
    Returns:
        A Series indexed by client hash, with the count of distinct
        10-minute windows that client showed up in.
    """

def flag_infrastructure_clients(window_counts: pd.Series, threshold: int) -> set:
    """
    TODO:
    Given the output of count_windows_per_client(), return the set of
    client hashes that look like infrastructure -- i.e. appeared in more
    than `threshold` distinct windows.
 
    Args:
        window_counts: Series from count_windows_per_client()
        threshold: minimum number of windows before we consider a client
            suspicious. Pick a number and justify it in your write-up --
            e.g. if there are ~144 possible 10-min windows in a day,
            a device present in more than, say, 100 of them in one day
            is a reasonable starting cutoff. Tune this once you see results.
 
    Returns:
        A set of client hashes flagged as likely-infrastructure.
    """

def filter_infrastructure(df: pd.DataFrame, flagged_clients: set) -> pd.DataFrame:
    """
    TODO:
    Remove rows belonging to flagged infrastructure clients from the
    DataFrame.
 
    Args:
        df: the full WiFi DataFrame.
        flagged_clients: set of client hashes to exclude (from
            flag_infrastructure_clients()).
 
    Returns:
        A new, filtered DataFrame with those clients' rows removed.
    """

if __name__ == "__main__":
    df = clean_table(CSV_PATH)
    # TODO: for a couple of busy APs (e.g. "Bldg44AP10"):
    #   1. Print the raw distinct-device count per window (before filtering)
    #   2. Run count_windows_per_client -> flag_infrastructure_clients
    #      -> filter_infrastructure
    #   3. Print the distinct-device count per window again (after filtering)
    # The deliverable is that before/after comparison, printed clearly.
    pass
