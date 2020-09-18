import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
%matplotlib inline

df = pd.read_csv('c:/02_Work/workspace/datasets/Lesson3/mycars.csv', delimiter=',')
df.columns

plt.boxplot(df.hp)