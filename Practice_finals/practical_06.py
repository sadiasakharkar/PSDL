import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("/Users/sadiasakharkar/Cummins/SEM 4/PSDL/Dengue_diseases_dataset_modified (1).csv")

print(df.head())
print(df.tail())
print(df.info())
print(df.shape)
print(df.columns)
print(df.loc[3])
print(df.iloc[-1])

subset = df[['age' , 'gender' , 'rbc_count']]
print(subset.head())
print(subset.tail())
print(subset['rbc_count'].min())
print(subset['rbc_count'].max())
print(subset['rbc_count'].mean())
print(subset['rbc_count'].median())
print(subset['rbc_count'].std())
print(subset['rbc_count'].var())
print(subset['rbc_count'].skew())


# box plot
plt.figure()
df['rbc_count'].plot(kind='box')
plt.title("box plot")
plt.xlabel("rbc_count")
plt.show()

# histogram 
plt.figure()
df['rbc_count'].plot(kind='hist', bins= 10)
plt.title("histogram")
plt.xlabel("rbc_count")
plt.ylabel('Frequency')
plt.show()

# bar 
plt.figure()
df['gender'].value_counts().plot(kind='bar')
plt.title("bar chart")
plt.xlabel("gender")
plt.ylabel("Frequency")
plt.show()

# scatter
plt.figure()
plt.scatter(df['age'] , df['rbc_count'])
plt.title("scatter plot")
plt.xlabel("age")
plt.ylabel("rbc_count")
plt.show()

plt.figure()
df['rbc_count'].value_counts().plot(kind='pie')
plt.title("pie chart")
plt.xlabel("rbc_count")
plt.ylabel("Frequency")
plt.show()

plt.figure()
df['rbc_count'].value_counts().plot(kind='line')
plt.title("line chart")
plt.xlabel("rbc_count")
plt.ylabel("Frequency")
plt.show()
