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
    ap_df = df[df["AP"] == ap].copy()

    # Put every timestamp into a 10-minute time window
    ap_df["time_window"] = ap_df["timestamp"].dt.floor("10min")

    # Count how many different windows each client appeared in
    window_counts = ap_df.groupby("client")["time_window"].nunique()

    return window_counts.sort_values(ascending=False)

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
    flagged = window_counts[window_counts > threshold].index
    return set(flagged)

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
    return df[~df["client"].isin(flagged_clients)].copy()

if __name__ == "__main__":
    df = clean_table(CSV_PATH)

    # Find two busy APs
    busy_aps = df["AP"].value_counts().head(2).index.tolist()

    THRESHOLD = 100

    for ap in busy_aps:
        print("\n" + "=" * 60)
        print(f"AP: {ap}")
        print("=" * 60)

        # Get only rows belonging to this AP
        ap_df = df[df["AP"] == ap].copy()

        # BEFORE filtering:
        # Count distinct clients in each 10-minute window
        before_counts = (
            ap_df.set_index("timestamp")
            .resample("10min")["client"]
            .nunique()
        )

        print("\nDistinct devices per 10-minute window BEFORE filtering:")
        print(before_counts)

        # Determine how many windows each client appears in
        window_counts = count_windows_per_client(df, ap)

        # Flag likely infrastructure devices
        flagged_clients = flag_infrastructure_clients(
            window_counts,
            THRESHOLD
        )

        print(f"\nClients appearing in more than {THRESHOLD} windows:")
        print(flagged_clients if flagged_clients else "None")

        print(f"Number of clients flagged: {len(flagged_clients)}")

        # Remove flagged devices
        filtered_df = filter_infrastructure(
            df,
            flagged_clients
        )

        # Get this AP again after filtering
        filtered_ap_df = filtered_df[filtered_df["AP"] == ap].copy()

        # AFTER filtering
        after_counts = (
            filtered_ap_df.set_index("timestamp")
            .resample("10min")["client"]
            .nunique()
        )

        print("\nDistinct devices per 10-minute window AFTER filtering:")
        print(after_counts)

        # Compare before vs after
        comparison = pd.DataFrame({
            "before": before_counts,
            "after": after_counts
        }).fillna(0).astype(int)

        comparison["removed"] = (
            comparison["before"] - comparison["after"]
        )

    print("\nBefore/after comparison:")
    print(comparison)

