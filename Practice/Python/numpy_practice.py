import numpy as np
from openpyxl.compat.numbers import NUMPY
from pandas.io.sql import PandasSQL

cvalues = [20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9, 20.1]
data = np.array(cvalues)
print(data)
fvalues = [ x*9/5 + 32 for x in cvalues]
print(fvalues)

a= np.arange(1,10)
print(a)
import numpy as np
import pandas as pd
NaN = np.nan
dataframe = pd.DataFrame({'Name': ['Shobhit', 'Vaibhav',
'Vimal', 'Sourabh',
'Rahul', 'Shobhit'],
'Physics': [11, 12, 13, 14, NaN, 11],
'Chemistry': [10, 14, NaN, 18, 20, 10],
'Math': [13, 10, 15, NaN, NaN, 13]})

data = [["James","","Smith",30,"M",60000],
["Michael","Rose","",50,"M",70000],
["Robert","","Williams",42,"",400000],
["Maria","Anne","Jones",38,"F",500000],
["Jen","Mary","Brown",45,None,0]]
columns=['First Name','Middle Name','Last Name','Age','Gender','Salary']
# Create the pandas DataFrame
pandasDF=pd.DataFrame(data=data, columns=columns)
# print dataframe.



