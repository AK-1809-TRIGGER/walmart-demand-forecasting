import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings

warnings.filterwarnings('ignore')

train = pd.read_csv(r"G:\walmart-demand-forecasting\data\train.csv")
stores = pd.read_csv(r"G:\walmart-demand-forecasting\data\stores.csv")
features = pd.read_csv(r"G:\walmart-demand-forecasting\data\features.csv")

df = train.merge(stores, on='Store', how='left')

df = df.merge(
    features,
    on=['Store', 'Date'],
    how='left'
)

df['Date'] = pd.to_datetime(df['Date'])

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Week'] = df['Date'].dt.isocalendar().week.astype(int)

df.to_csv(
    r"G:\walmart-demand-forecasting\\data\\merged_data.csv",
    index=False
)

print("Dataset Shape:", df.shape)
print("Data Range:", df['Date'].min(), "to", df['Date'].max())
print("Stores:", df['Store'].nunique(),
      "| Departments:", df['Dept'].nunique())

print("\nSample:")
print(df.head(3))
