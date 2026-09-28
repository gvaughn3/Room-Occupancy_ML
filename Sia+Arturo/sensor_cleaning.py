import pandas as pd

"""
The goal of this file is to load the Occupancy_Estimation sensor CSV, produce a clean DataFrame
with a real datetime column

This dataset has columns like Date, Time, S1_Temp, S1_Light,
S1_Sound, S5_CO2, S6_PIR, S7_PIR, and a labeled target column
Room_Occupancy_Count. Unlike the WiFi dataset, this one has real ground
truth. Room_Occupancy_Count is what we're eventually trying to predict.
"""

def load_sensor_data() -> pd.DataFrame:
    df = pd.read_csv("Occupancy_Estimation.csv")
    return df


def add_datetime_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    TODO:
    Combine the separate Date and Time columns into a single real datetime
    column (Combine the columns and then pass them through pd.to_datetime)
    This will make it easier to perform functions related to time later.

    Args:
        df: raw DataFrame with separate "Date" and "Time" columns.

    Returns:
        A new DataFrame with an added "datetime" column.
    """
    df = df.copy()
    df["datetime"] = pd.to_datetime(df["Date"] + " " + df["Time"])
    return df



if __name__ == "__main__":
    # TODO: call load_sensor_data(), then add_datetime_column()
    df = load_sensor_data()
    df = add_datetime_column(df)
    print(df[["Date", "Time", "datetime"]].head())
    print(df.dtypes["datetime"])