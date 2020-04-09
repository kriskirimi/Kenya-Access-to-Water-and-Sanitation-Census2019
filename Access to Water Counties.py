# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 16:34:26 2020

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
cols = (['Conventional Households', 'Pond(%)', 'Dam/Lake(%)', 'Stream/River', 'Protected Spring', 'Unprotected Spring', 'Protected Well', 'Unprotected  Well', 'Borehole/ Tube well','piped into  dwelling', 'Piped to yard/ Plot', 'Bottled water', 'Rain/ Harvested water', 'Water Vendor', 'Public tap/ Standpipe','Not Stated'])
Counties= ['MOMBASA', 'KWALE','KILIFI' ,'TANA',
            'LAMU' ,'TAITA','GARISSA','WAJIR','MANDERA',
            'MARSABIT','ISIOLO','MERU','THARAKA','EMBU','KITUI','MACHAKOS',
            'MAKUENI','NYANDARUA','NYERI','KIRINYAGA','MURANGA','KIAMBU',
            'TURKANA','WEST','SAMBURU','UASIN','TRANS',
            'ELGEYO','NANDI','BARINGO','LAIKIPIA','NAKURU',
            'NAROK','KAJIADO','KERICHO','BOMET','KAKAMEGA','VIHIGA','BUNGOMA',
            'BUSIA' ,'SIAYA' ,'KISUMU','HOMA','MIGORI','KISII' ,'NYAMIRA','NAIROBI']
Counties.sort()
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')
df.dtypes
df1 = df[df['County/ Sub-County'].str.contains('|'.join(Counties))]
df1.set_index('County/ Sub-County', inplace=True)

df1.reset_index(inplace=True)

df2= df1.iloc[[0, 1, 3, 6, 10, 13, 15, 17, 22, 27, 31, 33, 38, 42, 46, 49, 51, 54, 59,
               64, 69, 72, 78, 80, 84, 87, 88, 90, 95, 98, 103, 107, 114, 118, 120, 
               123, 129, 132, 139, 141, 143, 147, 149, 152, 155, 158]]





#               53, 57, 59, 65, 67, 71, 74, 75, 80, 83, 88, 92, 97, 101, 103, 
#               106, 111, 114, 120, 122, 124, 128, 130, 131, 134, 137]]
#df2 = 
#drop_subcounties=['KILIFI NORTH', 'KILIFI SOUTH', 'LAMU EAST', 'LAMU WEST', 'WAJIR NORTH', 
#                  'WAJIR SOUTH', 'WAJIR WEST', 'MANDERA WEST', 'MANDERA CENTRA', 'MANDERA EAST', 
#                  'MANDERA NORTH', 'MARSABIT CENTRAL', 'MARSABIT NORTH', 'MARSABIT SOUTH', 'MERU CENTRAL', 
#                  'MERU NATIONAL PARK','MERU SOUTH']
#
#df = df.drop(drop_subcounties, axis=0, inplace=True)
#df.index
#
#df[['MOMBASA', 'KWALE','KILIFI' ,'TANA RIVER']].index

##f.set_index(df['County/ Sub-County'], inplace=True)
#df1=df.T
#df1 = df1.reset_index().T
#list = df1.iloc[0].str.contains(Counties)
#
#
#
#df1[df1.columns.sort_values()]
#df1.head(5)
#df1.index
#df2=df1[df1.columns.intersection(Counties)]
#
#df1 = df1.T
#
#df[[Counties]]==df.columns
#df = df[df['County/ Sub-County'].str.contains('|'.join(Counties))]
#List = df['County/ Sub-County'].tolist()



#df = df.loc[Counties]
#df.T
#df
