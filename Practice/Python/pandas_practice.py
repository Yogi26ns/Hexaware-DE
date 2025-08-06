
# importing Libraries
import pandas as pd
import numpy as np

# Creating dataframe using dictionary
NaN = np.nan
dataframe = pd.DataFrame({
    'Name': ['Shobhit', 'Vaibhav', 'Vimal', 'Sourabh', 'Rahul', 'Shobhit'],
    'Physics': [11, 12, 13, 14, NaN, 11],
    'Chemistry': [10, 14, NaN, 18, 20, 10],
    'Math': [13, 10, 15, NaN, NaN, 13]
})

print("Created Dataframe")
print(dataframe)

# finding Count of all columns
print("\nCount of all values wrt columns")
print(dataframe.count())

# Count according to rows
print("\nCount of all values wrt rows")
print(dataframe.count(axis=1))
print(dataframe.count(axis='columns'))

# count of null values
print("\nNull Values counts")
print(dataframe.isnull().sum())
print("Total null values:", dataframe.isnull().sum().sum())

# count of students with greater than 11 marks in physics
print("\nCount of students with physics marks greater than 11 is->",
      dataframe[dataframe['Physics'] > 11]['Name'].count())

# resultant of above dataframe
print("\nStudents with Physics > 11:")
print(dataframe[dataframe['Physics'] > 11])

# count of students meeting multiple criteria
print("\nCount of students with Physics>10, Chemistry>11, Math>9:",
      dataframe[(dataframe['Physics'] > 10) &
               (dataframe['Chemistry'] > 11) &
               (dataframe['Math'] > 9)]['Name'].count())

print("\nThese students are:")
print(dataframe[(dataframe['Physics'] > 10) &
               (dataframe['Chemistry'] > 11) &
               (dataframe['Math'] > 9)])

import pandas as pd
# Load the data
file_path = r"C:\Users\nsyog\Downloads\LoanData (1).csv"

data = pd.read_csv(file_path)

# Print the first 5 rows
print("\nFirst 5 Rows:")
print(data.head())

# Print column names
print("\nColumn Names:")
print(data.columns)

# Summary of DataFrame
print("\nData Summary (Info):")
print(data.info())

# Descriptive statistics
print("\nDescriptive Statistics:")
print(data.describe())

# Check for missing values
print("\nMissing Data:")
print(data.isnull().sum())
data['outputcolumn'] = data['LoanAmount'].apply(lambda x:x/10)
data['appcolumn'] = data['ApplicantIncome'].apply(lambda x:x/10)
data.head()
