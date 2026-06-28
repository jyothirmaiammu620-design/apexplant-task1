import pandas as pd

# Load Excel dataset
df = pd.read_excel(r"C:\Users\DELL\Downloads\ApexPlanet_DataAnalytics_Dataset.xlsx")

# Display first 5 rows
print(df.head())

# Check missing values
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Save cleaned dataset
df.to_excel("cleaned_sales_data.xlsx", index=False)

print("Data cleaning completed successfully!")
import matplotlib.pyplot as plt
import seaborn as sns

# Histogram for numerical columns
df.hist(figsize=(10,8))
plt.show()

# Correlation heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Example bar chart (change column names if needed)
df.select_dtypes(include='number').mean().plot(kind='bar')
plt.title("Average Values of Numerical Columns")
plt.xlabel("Columns")
plt.ylabel("Average")
plt.show()