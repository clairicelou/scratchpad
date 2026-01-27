# %%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import skimpy as skim 


df = pd.read_csv('./data/craiglist_cville_cars_long.csv')
df.head()
 
# %%

sns.histplot( np.log( df['price']), bins = 50 )

df['price'].describe()

# %%

sns.ecdfplot( df['price']) 

# %%

sns.boxplot( x = df['price'])

# %%

x = df['price']

def outlier_analyze(x):
    q75 = np.quantile( x, .75)
    q25 = np.quantile( x, .25)
    iqr = q75 - q25
    uw = q75 + 1.5 * iqr # upper whisker
    lw = q25 - 1.5 * iqr # lower whisker
    upper_outlier = ( x > uw ).astype(int)
    lower_outlier = ( x < lw ).astype(int)
    outlier = upper_outlier + lower_outlier
    winsorize = (
        upper_outlier * uw + # map upper outlier to upper whisker
        lower_outlier * lw + # map lower outliers to lower whisker
        ( 1 - outlier ) * x # if neither, keep original value
    )

    return outlier, winsorize






# %%

outlier, winsorize = outlier_analyze(x)
# %%

sns.scatterplot( x=x, y=winsorize)

# %%
