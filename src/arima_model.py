import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
import numpy as np
df = pd.read_csv(r"G:\walmart-demand-forecasting\data\merged_data.csv")

df["Date"] = pd.to_datetime(df["Date"])

ts = (
    df.groupby("Date")["Weekly_Sales"]
    .sum()
)

train = ts[:-12]
test = ts[-12:]

model = ARIMA(
    train,
    order=(1, 1, 1),
    seasonal_order=(1, 1, 0, 52)
)

fit = model.fit()

forecast = fit.forecast(steps=12)

rmse = np.sqrt(
    mean_squared_error(test, forecast)
)

mae = mean_absolute_error(test, forecast)

print(rmse)
print(mae)