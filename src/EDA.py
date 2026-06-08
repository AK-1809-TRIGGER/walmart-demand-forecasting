import pandas as pd
import numpy as np

train = pd.read_csv("G:\\walmart-demand-forecasting\\data\\train.csv")
features = pd.read_csv("G:\\walmart-demand-forecasting\\data\features.csv")
stores = pd.read_csv("G:\\walmart-demand-forecasting\\data\\store.csv")
df = pd.read_csv(r"G:\walmart-demand-forecasting\data\\merged_data.csv")
df = train.merge(features, on=["Store", "Date", "IsHoliday"])
df = df.merge(stores, on="Store")

df["Date"] = pd.to_datetime(df["Date"])

df.fillna(0, inplace=True)

weekly_sales = df.groupby("Date")["Weekly_Sales"].sum().reset_index()

holiday_sales = df.groupby("IsHoliday")["Weekly_Sales"].mean().reset_index()

top_stores = (
    df.groupby("Store")["Weekly_Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

dept_summary = (
    df.groupby("Dept")["Weekly_Sales"]
    .agg(["mean", "max", "std"])
    .reset_index()
)

dept_summary.columns = [
    "Dept",
    "avg_sales",
    "peak_sales",
    "std_sales"
]

dept_summary["volatility"] = (
    dept_summary["std_sales"] /
    dept_summary["avg_sales"]
)

dept_summary["risk_flag"] = (
    dept_summary["volatility"] > 0.5
)

at_risk = dept_summary[
    dept_summary["risk_flag"] == True
].sort_values("volatility", ascending=False)

print(df.shape)
print(top_stores.head())
print(at_risk.head())