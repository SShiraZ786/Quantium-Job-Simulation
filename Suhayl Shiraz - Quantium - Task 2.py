# Suhayl Shiraz
# March 2026
import pandas as pd

files = ["daily_sales_data_0.csv", "daily_sales_data_1.csv", "daily_sales_data_2.csv"]

df_list = []

for file in files:
    df = pd.read_csv(file)

    # Keep only pink morsel rows
    df = df[df["product"].str.lower() == "pink morsel"]

    # Remove $ from price column so it doesn't just repeat a string when multiplied
    df["price"] = df["price"].replace(r"[\$,]", "", regex=True).astype(float)

    # Create sales column
    df["Sales"] = df["quantity"] * df["price"]

    # Keep only required columns
    df = df[["date","Sales","region"]].rename(columns={
        "date": "Date",
        "region": "Region"
    })

    # Add all relevant rows to combined list
    df_list.append(df)

# Output combined list to new file
df_final = pd.concat(df_list, ignore_index=True)
df_final.to_csv("Pink_Morsel_Sales_Data.csv", index=False)