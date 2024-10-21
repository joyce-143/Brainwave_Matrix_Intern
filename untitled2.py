# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Vu-vDMKjDRizw8xwtnpWBo4cTZzwDEfB
"""

import zipfile
import os

# Define the path to the uploaded zip file and the extraction directory
zip_path = '/content/drive/MyDrive/archive (1).zip'
extraction_dir = '/content/drive/MyDrive/extracted_files'

# Extract the zip file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extraction_dir)

# List the extracted files to see what is inside
extracted_files = os.listdir(extraction_dir)
extracted_files

import pandas as pd

# Load the extracted CSV file to inspect the data
data_file_path = os.path.join('/content/drive/MyDrive/extracted_files, data.csv')
data = pd.read_csv('/content/drive/MyDrive/archive (1).zip')

# Display the first few rows and general information about the data
data.head(), data.info()

import matplotlib.pyplot as plt
import seaborn as sns

# 1. Descriptive Statistics
sales_summary = data.describe()

# 2. Handling missing data
missing_data = data.isnull().sum()

# Fill missing Item_Weight with the mean weight
data['Item_Weight'].fillna(data['Item_Weight'].mean(), inplace=True)

# Fill missing Outlet_Size with 'Unknown'
data['Outlet_Size'].fillna('Unknown', inplace=True)

# 3. Grouped Sales Analysis: Sales by Outlet Type
sales_by_outlet_type = data.groupby('Outlet_Type')['Item_Outlet_Sales'].sum().sort_values()

# 4. Visualizations: Sales Distribution and Trends
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Sales distribution
sns.histplot(data['Item_Outlet_Sales'], bins=30, kde=True, ax=axes[0, 0])
axes[0, 0].set_title('Distribution of Item Outlet Sales')

# Sales by Outlet Type
sns.barplot(x=sales_by_outlet_type.index, y=sales_by_outlet_type.values, ax=axes[0, 1])
axes[0, 1].set_title('Total Sales by Outlet Type')
axes[0, 1].set_xticklabels(axes[0, 1].get_xticklabels(), rotation=45)

# Item Visibility vs Sales
sns.scatterplot(data=data, x='Item_Visibility', y='Item_Outlet_Sales', ax=axes[1, 0])
axes[1, 0].set_title('Item Visibility vs Sales')

# Sales by Item Type (Top 10)
sales_by_item_type = data.groupby('Item_Type')['Item_Outlet_Sales'].sum().sort_values(ascending=False).head(10)
sns.barplot(x=sales_by_item_type.index, y=sales_by_item_type.values, ax=axes[1, 1])
axes[1, 1].set_title('Top 10 Item Types by Sales')
axes[1, 1].set_xticklabels(axes[1, 1].get_xticklabels(), rotation=45)

plt.tight_layout()
plt.show()

sales_summary, missing_data