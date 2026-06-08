import pandas as pd
from prophet import Prophet
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
import numpy as np

df = pd.read_csv(r"G:\walmart-demand-forecasting\data\\merged_data.csv")

df["Date"] = pd.to_datetime(df["Date"])

ts = (
    df.groupby("Date")["Weekly_Sales"]
    .sum()
    .reset_index()
)

ts.columns = ["ds", "y"]

train = ts[:-12]
test = ts[-12:]

model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=True,
    seasonality_mode="multiplicative"
)

model.fit(train)

future = model.make_future_dataframe(
    periods=12,
    freq="W"
)

forecast = model.predict(future)

pred = forecast["yhat"].tail(12).values

rmse = np.sqrt(
    mean_squared_error(test["y"], pred)
)

mae = mean_absolute_error(
    test["y"],
    pred
)

print(rmse)
print(mae)