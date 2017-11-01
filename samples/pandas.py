import pandas as pd
import numpy as np

import numpy as np
import pandas as pd
import pandas_datareader as web

'''
Example of pandas library
'''

s_0 = pd.date_range('20130101', periods=100)
s_1 = pd.Series(np.arange(100))
s_2 = pd.Series(np.random.poisson(1, 100))

type(s_0)
dir(s_0)

s_1.std()
s_1.var()
s_1.mean()
s_1 = s_1.apply(lambda x: x + 1)
s_1 = s_1 - 1

s_2.value_counts()

DF = pd.DataFrame({'A' : s_1,
                   'B' : s_2})

DF.index = s_0

DF.head()
DF.dtypes
DF.columns()
DF[(DF.index > "2013-03-20") & (DF.A > 50) | (DF['B'] == 2)]
DF.loc["2013-03-20",:]
DF.iloc[0:2]
DF['X'] = DF.A + DF.B
DF.apply(lambda x: max(x))
DF.apply(lambda x: max(x), axis = 1)

# join 

left = pd.DataFrame({'key': ['foo', 'foo', 'bar'], 'lval': [1, 2, 3]})
right = pd.DataFrame({'key': ['foo', 'foo', 'bar'], 'rval': [4, 5 , 6]})

pd.merge(left, right, on='key')

url = 'https://raw.github.com/pandas-dev/pandas/master/pandas/tests/data/tips.csv'

tips = pd.read_csv(url)
tips.head()
tips.day.unique()

tips.groupby(['sex', 'day']).sum()

tips_1 = pd.pivot_table(tips, values = 'total_bill', index = ['sex', 'smoker'], columns = 'day', aggfunc = "count")
tips_1.stack()

###
 
quotes = np.array(['BBVA.MC', 'SAN.MC', 'SAB.MC', 'BKT.MC', 'CABK.MC'])

list(map(lambda x: web.get_data_yahoo(x), quotes))


# Leer de diferentes funtes

# data = pd.read_sql_query("SELECT * FROM TABLE")

data = pd.read_csv("/Users/angul/Documents/R/PyCourse/data/data.csv")
data = pd.read_excel("/Users/angul/Documents/R/PyCourse/data/data.xls")

data.head()

data.corr()

