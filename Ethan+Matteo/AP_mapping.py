import pandas as pd
from wifi_parser import clean_table

"""
There are several buildings in the data that have little to no activity on certain days. The
goal of this file is to find buildings that are busy, that would be good candidates for training
and testing on. 
"""

# You can change the file out for any of the ones on the website
CSV_PATH = "2014_01.csv"

def summarize_building_activity(df: pd.DataFrame) -> pd.DataFrame:
    """
    TODO:
    For each building, compute basic activity stats: total connection
    events, and number of distinct client devices seen. We are trying to get 
    a ranked table showing which buildings are worth focusing on, so we
    don't train on empty/low traffic buildings
 
    Args:
        df: DataFrame with "building" and "client" columns.
 
    Returns:
        A DataFrame indexed by building, with columns like
        "event_count" and "distinct_clients", sorted so the most
        active building is first.
    """

    activity = df.groupby("building").agg(event_count=("client", "count"), distinct_clients=("client", "nunique"))

    activity = activity.sort_values("event_count", ascending=False)

    return activity

def pick_focus_buildings(activity_summary: pd.DataFrame, n: int = 2) -> list:
        """
        TODO:
        Given the output of summarize_building_activity(), return the top N
        busiest building numbers -- these become our case-study focus for the
        rest of the pipeline (windowing, filtering, features).
    
        Args:
            activity_summary: output of summarize_building_activity()
            n: how many buildings to select (default 2)
    
        Returns:
            A list of building numbers (strings), e.g. ["44", "48"]
        """

        return activity_summary.head(n).index.tolist()
        
if __name__ == "__main__":
    df = clean_table(CSV_PATH)
    activity = summarize_building_activity(df)
    print(activity)
    focus = pick_focus_buildings(activity)
    print("Focusing on buildings:", focus)

