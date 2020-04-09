# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 17:28:52 2020

@author: KIRIMI
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 
df = pd.read_csv(r'C:\Users\KIRIMI\Documents\GitHub\Kenya-Access-to-Water-and-Sanitation-Census2019-Analysis-and-Visualization\Data\volume_4-table-2.15_chouseholds-by-main-source-of-drinking-water-area-of-residence-county-and-su.csv')
df.head(5)
df.shape
df.dtypes
df.columns
df.index
df.isnull().sum().sum()
df.iloc[265:275, :]
cols = (['Conventional Households', 'Pond(%)', 'Dam/Lake(%)', 
         'Stream/River', 'Protected Spring', 'Unprotected Spring', 
         'Protected Well', 'Unprotected  Well', 'Borehole/ Tube well',
         'piped into  dwelling', 'Piped to yard/ Plot', 'Bottled water', 
         'Rain/ Harvested water', 'Water Vendor', 
         'Public tap/ Standpipe','Not Stated'])
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')
df1 = df[df['County/ Sub-County'].str.contains('NAIROBI|MOMBASA')]
df1.set_index('County/ Sub-County', inplace=True)
df1.sort_values(by=['NAIROBI CITY', 'MOMBASA'], 
                axis=1, ascending=False, inplace=True)
percent_to_population = lambda x:x/100* df1['Conventional Households']
df2=df1.iloc[:,1:].apply(percent_to_population)
df3 = df2.iloc[:,0:7].T
fig, (ax1, ax2) = plt.subplots(1,2, figsize=(3,6))
plt.style.use('seaborn')
explode = (0.05, 0.05, 0.0, 0.0, 0.0, 0.0, 0.0)
plt.tight_layout()
ax1.pie(df3['MOMBASA'], labels=df3.index, explode=explode, 
        autopct='%1.1f%%', radius=0.5)
ax2.pie(df3['NAIROBI CITY'], labels=df3.index, explode=explode, 
        autopct='%1.1f%%', radius=1.0)
matplotlib.rcParams['font.size'] = 12
ax1.set_title('Mombasa County Access to Water, Census 2019')
ax2.set_title('Nairobi County Access to Water, Census 2019')
plt.show()