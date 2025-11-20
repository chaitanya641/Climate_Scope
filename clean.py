import pandas as pd

print("📥 Loading CSV...")

df = pd.read_csv(r"C:\Users\HP\Downloads\infosys_SpringBoard\GlobalWeatherRepository.csv")

print("\n📌 First 15 rows:")
print(df.head())

print("\n🔎 Checking missing values...")
print(df.isnull().sum())

# Drop duplicate rows
print("\n🧹 Removing duplicate rows...")
df = df.drop_duplicates()

# Optional: Drop columns with too many null values (if needed)
# df = df.dropna(axis=1, how='all')

# Fill missing numeric values with median
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

# Fill missing text with "Unknown"
text_cols = df.select_dtypes(include=['object']).columns
df[text_cols] = df[text_cols].fillna("Unknown")

print("\n📊 Dataset info after cleaning:")
print(df.info())

# Save cleaned file
output_path = r"C:\Users\HP\Downloads\infosys_SpringBoard\GlobalWeatherRepository_cleaned.csv"
df.to_csv(output_path, index=False)

print(f"\n✅ Cleaning completed! Cleaned file saved as:\n{output_path}")
