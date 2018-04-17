import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

url= 'https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv'
titanic = pd.read_csv(url)

%matplotlib inline

slices_hours = [titanic.sex.value_counts()['male'], titanic.sex.value_counts()['female']]
activities = ['Male', 'Female']
colors = ['r', 'g']

plt.pie(slices_hours, labels=activities, colors=colors, startangle=90, autopct='%.1f%%')
plt.show()