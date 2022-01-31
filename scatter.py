import pandas as pd 
import plotly.express as px 
df = pd.read_csv('/Users/ruth/Desktop/coding/python/projects/c-103/cases.csv')
fig = px.scatter(df,x='date',y='cases',color='country')
fig.show()