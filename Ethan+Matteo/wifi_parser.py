import pandas as pd

def clean_table(csv_path):

    # initialize data frame (turns the raw data into editable table: df)
    df = pd.read_csv(csv_path)

    # convert timestamps into datatime data type (to use time ranges later)
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # splits the data in the third column into two additional columns
    df["building"] = df["AP"].str.split("AP").str[0].str.replace("Bldg", "")
    df["ap_number"] = df["AP"].str.split("AP").str[1]

    return df

def get_windowed_counts(df, window_size="10min"):
  
    # Groups by AP and counts unique clients per time window.
    
    df_unique = df.set_index("timestamp").groupby("AP").resample(window_size)["client"].nunique()
    return df_unique

df = clean_table("2014_01.csv")
windowed = get_windowed_counts(df)

# shows repeating connection at regular interval
# print(windowed.loc["Bldg44AP10"].head(20))

# shows same mac address repeatedly reconnecting
# print(df[df["AP"] == "Bldg44AP10"].head(30))