import numpy as np
import pandas as pd
from scipy import stats
from sklearn.linear_model import LinearRegression

eco = pd.read_excel("/Users/angul/Desktop/Data.xlsx", sep = ";").dropna()

eco.columns

eco.country.unique()

lR = LinearRegression()

m = lR.fit(eco.Real_GDP_pc.reshape(len(eco),1), eco[['Consumption', 'Investment', 'Expenditure']])

m.coef_

ms = eco.groupby('country').apply(lambda x: LinearRegression().fit(x['Real_GDP_pc'].reshape(len(x),1), x[['Consumption', 'Investment', 'Expenditure']]))

ms['SPAIN           '].coef_

from sklearn.neural_network import MLPClassifier

clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)

y = eco.Real_GDP_pc
X = eco[['Consumption', 'Investment', 'Expenditure']]
clf.max_iter = 10000
