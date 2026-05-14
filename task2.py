#Unemployment Analysis with Python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Unemployment in India.csv")

# Remove spaces from column names
df.columns = df.columns.str.strip()

# Show first rows
print(df.head())

# Basic info
print(df.info())

# Check missing values
print(df.isnull().sum())

# Remove missing values
df = df.dropna()

# Rename columns for easier use
df.columns = [
    "Region",
    "Date",
    "Frequency",
    "Estimated_Unemployment_Rate",
    "Estimated_Employed",
    "Estimated_Labour_Participation_Rate",
    "Area"
]

# Convert date column
df["Date"] = pd.to_datetime(df["Date"])

# -------------------------------
# Average unemployment by region
# -------------------------------

avg_unemployment = df.groupby("Region")[
    "Estimated_Unemployment_Rate"
].mean().sort_values()

print(avg_unemployment)

# -------------------------------
# Plot unemployment by region
# -------------------------------

plt.figure(figsize=(12,6))

sns.barplot(
    x=avg_unemployment.index,
    y=avg_unemployment.values
)

plt.xticks(rotation=90)

plt.title("Average Unemployment Rate by Region")
plt.xlabel("Region")
plt.ylabel("Unemployment Rate")

plt.show()

# -------------------------------
# Covid impact analysis
# -------------------------------

plt.figure(figsize=(12,6))

sns.lineplot(
    data=df,
    x="Date",
    y="Estimated_Unemployment_Rate"
)

plt.title("Unemployment Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate")

plt.show()