import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('diabetes.csv')
summary_stats = df.describe()
print(summary_stats)

missing_values = df.isnull().sum()
print(missing_values)

columns_with_zero_as_missing = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
for column in columns_with_zero_as_missing:
    missing_count = (df[column]==0).sum()
    print (f"missing values in {column}: {missing_count}")
    
#replacing the na data 
for column in columns_with_zero_as_missing:
    df[column]=df[column].replace(0, np.nan)
    df[column]=df[column].mean()
    
#visual
#histograms 
df.hist(bins=30, figsize=(15,10))
plt.show()

#pair plot
sns.pairplot(df, hue='Outcome')
plt.plot()

#correlation heatmap
corr_matrix=df.corr()
plt.figure(figsize=(12,8))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.show()
