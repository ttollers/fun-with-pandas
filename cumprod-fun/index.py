
import pandas as pd
import numpy as np

df = pandas.read_csv("./data.csv")

df['CumProd'] = np.cumprod(df['point_latitude'])

#df_Clay = df[df['county']== 'CLAY COUNTY']
##df_Clay = df_Clay[df_Clay['construction']== 'Wood']
#def filterFunction(x):
#    print(x)
#    return x['county'] == 'CLAY COUNTY'
#    
#
#
#df_Smodger = [{
#        'county': 'CLAY COUNTY'
#        }, {
#                'county': 'NOT CLAY COUNTY'
#                }]
#
#df_10inch = list(df['county'])
#
#print(list(df.values.tolist()))
#
#df_George = list(filter(filterFunction, df.values.tolist()))
#print(df_George)

import statsmodels.formula.api as sm

result = sm.ols(formula="tiv_2012 ~ tiv_2011 ", data=df).fit()

print(result.summary())