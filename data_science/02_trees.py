#https://www.kaggle.com/nycparks/tree-census
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt 


# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df = pd.read_csv('/kaggle/input/tree-census/new_york_tree_census_2015.csv')
df1995 = pd.read_csv('/kaggle/input/tree-census/new_york_tree_census_1995.csv')

df = pd.DataFrame(df, columns=['longitude', 'latitude'])
df.info()

import seaborn as sns
dfcorr = df.corr()
sns.heatmap(dfcorr,annot=True,cmap='coolwarm')

d1995 = pd.DataFrame(df1995, columns=['longitude', 'latitude'])
d1995.info()
d1995.head(20)


df.plot.scatter('longitude', 'latitude', figsize=(20,20))
d1995.plot.scatter('longitude', 'latitude', figsize=(10,10))

nyc_min_lon = -74.05
nyc_max_lon = -73.75

nyc_min_lat = 40.63
nyc_max_lat = 40.85
        
for long in ['longitude', 'longitude']:
    d1995 = d1995[(d1995[long] > nyc_min_lon) & (d1995[long] < nyc_max_lon) ]

for lat in ['latitude', 'latitude']:
    d1995 = d1995[(d1995[lat] > nyc_min_lat) & (d1995[lat] < nyc_max_lat)]

d1995.describe()
d1995.plot.scatter('longitude', 'latitude', figsize=(20,20))
df.plot.scatter('longitude', 'latitude', figsize=(20,20))
