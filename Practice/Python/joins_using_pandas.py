# 1.Inner join
import pandas as pd
# Creating dataframe a
a = pd.DataFrame()
# Creating Dictionary
d = {'id': [1, 2, 10, 12],
'val1': ['a', 'b', 'c', 'd']}
a = pd.DataFrame(d)
# Creating dataframe b
b = pd.DataFrame()

print(a)
# Creating dictionary
d = {'id': [1, 2, 9, 8],
'val1': ['p', 'q', 'r', 's']}
b = pd.DataFrame(d)
print(b)

#innerjoin
df= pd.merge(a, b, on= 'id' ,how= 'right')
print(df)
# 2.Index join
