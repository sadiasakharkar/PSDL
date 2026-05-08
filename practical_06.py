import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("Dengue_diseases_dataset_modified (1).csv")

print(df.head())
print(df.tail())
print(df.info())
print(df.shape)
print(df.columns)

print(df.loc[5])
print(df.iloc[-1])

subset = df[['age' , 'gender' , 'rbc_count']]
print("Maximum: " , subset['rbc_count'].max())
print("Minimum: " , subset['rbc_count'].min())
print("Mean: " , subset['rbc_count'].mean())
print("Median: " , subset['rbc_count'].median())
print("Standard Deviation: " , subset['rbc_count'].std())
print("Variance: " , subset['rbc_count'].var())
print("Skewness: " , subset['rbc_count'].skew())


# box plot
plt.figure()
subset['rbc_count'].plot(kind = 'box')
plt.title("Box plot")
plt.xlabel('RBC Count')
plt.show()

# Histogram
plt.figure()
subset['rbc_count'].plot(kind = 'hist')
plt.title("Histogram")
plt.xlabel('RBC Count')
plt.ylabel('Frequency')
plt.show()

# bar graph
plt.figure()
subset['age'].value_counts().plot(kind = 'bar')
plt.title("bar graph")
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# scattered plot
plt.figure()
plt.scatter(subset['age'], subset['rbc_count'])
plt.title("scattered plot")
plt.xlabel('Age')
plt.ylabel('RBC Count'  )
plt.show()