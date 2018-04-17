import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn
seaborn.set(style='ticks')

url= 'https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv'
titanic = pd.read_csv(url)
#print(titanic)
%matplotlib inline

_genders= ['female', 'male']
fg = seaborn.FacetGrid(data=titanic, hue='sex', hue_order=_genders, aspect=3)
fg.map(plt.scatter, 'age', 'fare', alpha=.6).add_legend()
plt.show()