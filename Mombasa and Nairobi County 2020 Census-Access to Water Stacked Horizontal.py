# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 09:25:13 2020

@author: KIRIMI
"""

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\KIRIMI\Documents\GitHub\Kenya-Access-to-Water-and-Sanitation-Census2019-Analysis-and-Visualization\Data\volume_4-table-2.15_chouseholds-by-main-source-of-drinking-water-area-of-residence-county-and-su.csv')
df.head(5)
df.shape
df.dtypes
df.columns
df.index
df.isnull().sum().sum()
df.iloc[265:275, :]
cols = (['Conventional Households', 'Pond(%)', 'Dam/Lake(%)', 'Stream/River', 'Protected Spring', 'Unprotected Spring', 'Protected Well', 'Unprotected  Well', 'Borehole/ Tube well','piped into  dwelling', 'Piped to yard/ Plot', 'Bottled water', 'Rain/ Harvested water', 'Water Vendor', 'Public tap/ Standpipe','Not Stated'])
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')
df1 = df[df['County/ Sub-County'].str.contains('NAIROBI|MOMBASA')]
df1.index
df1.columns
df1.set_index('County/ Sub-County', inplace=True)
df1.sort_values(by=['NAIROBI CITY', 'MOMBASA'], axis=1, ascending=False, inplace=True)
percent_to_population = lambda x:x/100* df1['Conventional Households']
df2=df1.iloc[:,1:].apply(percent_to_population)
df2['Summation'] = df2.iloc[:,0:7].sum(axis=1)
df2['Summation']
population_to_percent = lambda x:x/df2['Summation']*100
df3= df2.iloc[:,0:7].apply(population_to_percent)
plt.style.use('bmh')
df3.plot(kind = 'barh', figsize=(12,5), stacked=True, edgecolor='white', width=0.15)
plt.legend(loc='best')
plt.xlabel('Percentage of County Population (%)')
plt.title('Distribution of Conventional Households by Main Source of Drinking Water, Census 2019')
plt.show()

