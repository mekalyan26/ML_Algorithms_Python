# Importing important libraries for Python Machine Learning Project
import numpy
import pandas
import seaborn


# Read CSV file using pandas
df = pandas.read_csv('/02_Work/workspace/datasets/datasetfile.csv', delimiter = ',')
# dimensionality check
var = df.shape
print(df)
print(var)

# Types of Dataset

