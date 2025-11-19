import pandas as pd

print("Loading CSV...")

df = pd.read_csv(r"C:\Users\HP\Downloads\infosys_SpringBoard\GlobalWeatherRepository.csv")

print("First 5 rows:")
print(df.head())
