# iris_analysis.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset
try:
    # Load the Iris dataset
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    
    print("✅ Dataset loaded successfully!\n")
    print("🔹 First 5 rows of the dataset:")
    print(df.head())

    # Check structure and missing values
    print("\n🔹 Data types:")
    print(df.dtypes)

    print("\n🔹 Missing values:")
    print(df.isnull().sum())

    # No missing values here; if there were, we could:
    # df.fillna(method='ffill', inplace=True)  OR  df.dropna(inplace=True)

except FileNotFoundError:
    print("❌ File not found. Please check the dataset path.")
except Exception as e:
    print(f"❌ An error occurred: {e}")

# Task 2: Basic Data Analysis

print("\n✅ Basic Statistics:")
print(df.describe())

# Group by species and compute mean
grouped = df.groupby('species').mean()
print("\n🔹 Mean values grouped by species:")
print(grouped)

# Task 3: Data Visualization

sns.set(style="whitegrid")
plt.figure(figsize=(12, 8))

# 1. Line chart – average measurements per species
plt.subplot(2, 2, 1)
grouped.T.plot(kind='line', marker='o', ax=plt.gca())
plt.title("📈 Avg Feature Measurements by Species")
plt.xlabel("Features")
plt.ylabel("Measurement (cm)")
plt.legend(title='Species')

# 2. Bar chart – average petal length per species
plt.subplot(2, 2, 2)
sns.barplot(data=df, x='species', y='petal length (cm)', palette="viridis", ci=None)
plt.title("📊 Avg Petal Length by Species")
plt.ylabel("Petal Length (cm)")

# 3. Histogram – distribution of sepal length
plt.subplot(2, 2, 3)
sns.histplot(data=df, x='sepal length (cm)', bins=15, kde=True, color='salmon')
plt.title("📉 Sepal Length Distribution")

# 4. Scatter plot – Sepal vs Petal length
plt.subplot(2, 2, 4)
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species', palette="deep")
plt.title("🔎 Sepal vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title='Species')

plt.tight_layout()
plt.show()
