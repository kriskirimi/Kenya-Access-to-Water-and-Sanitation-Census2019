# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 12:03:07 2020

@author: KIRIMI
"""

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\KIRIMI\.spyder-py3\My Projects\Kenya Access to Water and Sanitation Census 2019\Data\volume_4-table-2.15_chouseholds-by-main-source-of-drinking-water-area-of-residence-county-and-su.csv')
df.head(5)
df.shape
df.dtypes
df.columns
df.index
df.isnull().sum().sum()
df.iloc[265:275, :]

columns = (['Conventional Households', 'Pond(%)', 'Dam/Lake(%)', 
         'Stream/River', 'Protected Spring', 'Unprotected Spring', 
         'Protected Well', 'Unprotected  Well', 'Borehole/ Tube well',
         'piped into  dwelling', 'Piped to yard/ Plot', 'Bottled water', 
         'Rain/ Harvested water', 'Water Vendor', 
         'Public tap/ Standpipe','Not Stated'])

df[columns] = df[columns].apply(pd.to_numeric, errors='coerce')
df.dtypes
df = df.drop_duplicates(subset='County/ Sub-County')
df['County/ Sub-County']=df['County/ Sub-County'].str.replace(' ', '-').str.replace('/', '-').str.replace("'", "")

Counties_List = ['MOMBASA' ,'KWALE' , 'BUSIA', 'KILIFI' ,'TANA-RIVER' ,'LAMU','TAITA-TAVETA','GARISSA','WAJIR',
'MANDERA','MARSABIT','ISIOLO','MERU','THARAKA-NITHI','EMBU','KITUI','MACHAKOS',
'MAKUENI','NYANDARUA','NYERI','KIRINYAGA','MURANGA','KIAMBU','TURKANA','WEST-POKOT',
'SAMBURU','UASIN-GISHU','TRANS-NZOIA', 'ELGEYO-MARAKWET', 'NANDI','BARINGO','LAIKIPIA','NAKURU',
'NAROK','KAJIADO','KERICHO','BOMET','KAKAMEGA','VIHIGA','BUNGOMA', 'SIAYA', 
'KISUMU','HOMA-BAY','MIGORI','KISII' ,'NYAMIRA','NAIROBI-CITY']

df1 = df[df['County/ Sub-County'].str.contains(r'^(?:{})$'.format('|'.join(Counties_List)))]
df1.reset_index(inplace=True, drop=True)
df1['Piped to dwelling or yard/ Plot']=df1.loc[:,['piped into  dwelling', 'Piped to yard/ Plot']].sum(axis=1)
df1=df1.sort_values(by='Piped to dwelling or yard/ Plot', ascending=False)
df1=df1.reset_index(drop=True)
df2=df1.iloc[:7,].append(df1.iloc[-7:,])
df2=df2.reset_index(drop=True)
df2.columns
plt.style.use('bmh')
fig, ax = plt.subplots(figsize=(17,3))
bars= ax.bar(df2['County/ Sub-County'], df2['Piped to dwelling or yard/ Plot'],  width=0.45)
for bar in bars:
    yval = bar.get_height().round(0)
    plt.text(bar.get_x(), yval + 1.5, yval)
ax.set_xticklabels(df2['County/ Sub-County'], fontsize=7.5)
ax.set_ylabel('(%) of County Population')
ax.set_xlabel('County')
ax.set_title('Counties Access to Water Piped to Dwelling and or Plot(Top 7 and Bottom 7 Counties), Census 2019')
plt.tight_layout()
plt.show()
