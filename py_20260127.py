# %%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import skimpy as skim 

print("Did you detect these changes?")

df = pd.read_csv('./data/craiglist_cville_cars_long.csv')
df.head()
 
# %%

sns.histplot( np.log( df['price']), bins = 50 )

df['price'].describe()

# %%

sns.ecdfplot( df['price']) 

# %%
