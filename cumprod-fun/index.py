
import pandas as pd
import numpy as np

df = pandas.read_csv("./data.csv")

df['CumProd'] = np.cumprod(df['point_latitude'])

df_florida = df[df['statecode']=='FL']
df_Clay = df[df['county']== 'CLAY COUNTY']