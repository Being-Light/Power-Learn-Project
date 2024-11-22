# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset

# Load the Iris dataset using sklearn
iris = load_iris()

# Convert to pandas DataFrame
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['species'] = iris.target_names[iris.target]

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(iris_df.head())

# Check for missing values
print("\nMissing values in the dataset:")
print(iris_df.isnull().sum())

# Check the data types of the columns
print("\nData types of the columns:")
print(iris_df.dtypes)

# Clean the dataset: Handle missing values (if any)
# Here, we'll assume there are no missing values. If there were, we could do:
# iris_df = iris_df.dropna()  # Or use iris_df.fillna(iris_df.mean())

# Task 2: Basic Data Analysis

# Basic statistics for numerical columns
print("\nBasic statistics of numerical columns:")
print(iris_df.describe())

# Group by species and calculate the mean of numerical columns
df_grouped = iris_df.groupby('species').mean()
print("\nMean values grouped by species:")
print(df_grouped)

# Task 3: Data Visualization

# 1. Line Chart: Trends Over Time (For demonstration, we'll create a line chart for petal length over rows)
plt.figure(figsize=(10, 6))
plt.plot(iris_df.index, iris_df['petal length (cm)'], label='Petal Length', color='blue')
plt.title('Petal Length Trend (Row Index)')
plt.xlabel('Row Index')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.grid(True)
plt.show()

# 2. Bar Chart: Average Petal Length by Species
plt.figure(figsize=(8, 6))
sns.barplot(x='species', y='petal length (cm)', data=iris_df)
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.show()

# 3. Histogram: Distribution of Sepal Length
plt.figure(figsize=(8, 6))
sns.histplot(iris_df['sepal length (cm)'], kde=True, bins=15)
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter Plot: Sepal Length vs Petal Length
plt.figure(figsize=(8, 6))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', data=iris_df, hue='species')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()

# Optional: Save the plots as images
# plt.savefig('petal_length_trend.png')
