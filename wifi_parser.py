import pandas as pd

# initialize data frame (turns the raw data into editable table: df)
df = pd.read_csv("2014_01.csv")

# convert timestamps into datatime data type (to use time ranges later)
df["timestamp"] = pd.to_datetime(df["timestamp"])

# splits the data in the third column into two additional columns
df["building"] = df["AP"].str.split("AP").str[0].str.replace("Bldg", "")
df["ap_number"] = df["AP"].str.split("AP").str[1]

# new table that counts unique clients at each AP, in 10 minute windows
df_unique = df.set_index("timestamp").groupby("AP").resample("10min")["client"].nunique()

# shows repeating connection at regular interval
# print(df_unique.loc["Bldg44AP10"].head(20))

# shows same mac address repeatedly reconnecting
# print(df[df["AP"] == "Bldg44AP10"].head(30))