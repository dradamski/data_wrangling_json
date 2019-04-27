# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 17:14:55 2019

@author: Drew
"""
import json
import pandas as pd
from pandas.io.json import json_normalize

json.load(open('data/world_bank_projects.json'))

json_df = pd.read_json('data/world_bank_projects.json')

# Question 1
print(json_df.countryname.value_counts().head(10))

# Question 2
projects=json.load((open('data/world_bank_projects.json')))
mjthemes=json_normalize(projects,'mjtheme_namecode')
codecounts=mjthemes['code'].value_counts()
codecounts.name='counts'
codecounts

# Question 3
# Create dataframe of codes with corresponding names
# 
themecodes = mjthemes[mjthemes['name'] != ''].drop_duplicates()

# Perform inner join on 'code' column 
filled = mjthemes.merge(themecodes, on='code', how='inner')
filled = filled.drop(columns='name_x')
print(filled)