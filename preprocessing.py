import numpy as np
import pandas as pd

dataset = pd.read_csv('Data.csv')
X = dataset.iloc[ : , :-1].values
Y = dataset.iloc[ : , 3].values

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values) = "NaN"
