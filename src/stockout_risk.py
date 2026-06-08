import pandas as pd

df = pd.read_csv(r"G:\walmart-demand-forecasting\data\\merged_data.csv")

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

print(at_risk.head(10))