import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset=pd.read_csv("bestsellers with categories.csv")

dataset.head(2)

dataset.tail(5)

dataset.columns

dataset.info()
dataset.shape

dataset.describe()

dataset.isnull().sum()

dataset.corr()

corr_matris=dataset.corr()
sns.heatmap(corr_matris,annot=True)
plt.show()

dataset['Author'].value_counts()

dataset['Author'].value_counts(ascending=True)

dataset['Author'].value_counts(ascending=True).sort_index(ascending=True)

a=dataset.groupby('Year')['Name'].value_counts().to_frame()

dataset['Genre'].value_counts().plot(kind="pie",autopct='%.2f',labels=dataset['Genre'].unique())





















