import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('studentscores.csv')
X = dataset.iloc[ : , : 1 ].values
Y = dataset.iloc[ : , 1 ].values
X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size = 1/4, random_state = 0)
regressor = LinearRegression()
regressor = regressor.fit(X_train, Y_train)

Y_pred = regressor.predict(X_test)
plt.scatter(X_train , Y_train, color = 'red')
plt.plot(X_train , regressor.predict(X_train), color = 'blue')

plt.scatter(X_test , Y_test, color = 'red')
plt.plot(X_test, regressor.predict(X_test), color = 'blue')
