import pandas as pd
import numpy as np

##import datasets/apps.csv
apps=pd.read_csv('datasets/apps.csv')

##preview data
#print(apps.info())
#print(apps.isna().sum())
#print(apps.head())

##clean and convert Installs column to dtype integer
apps['Installs']=apps['Installs'].str.replace(r'\W+','', regex=True).astype(int)

##group Apps by category and return aggregate analyses of Category Counts, Average, Price, and Average Rating
app_category_info = apps.groupby('Category').agg({'Category':'count','Price': ['mean'],'Rating':['mean']})
app_category_info = app_category_info.reset_index()
app_category_info.columns = ['Category','Number of apps','Average price', 'Average rating']
app_category_info = pd.DataFrame(app_category_info)

