import pandas as pd
import csv



roster = pd.read_csv('FIFA17final.csv',encoding = 'utf8')
# roster.describe()

print(roster[1:10])