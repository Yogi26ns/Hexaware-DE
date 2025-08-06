
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = r"C:\Users\nsyog\Downloads\LoanData (1).csv"
data = pd.read_csv(file_path)

# Apply transformations (optional)
data['outputcolumn'] = data['LoanAmount'].apply(lambda x: x / 10)
data['appcolumn'] = data['ApplicantIncome'].apply(lambda x: x / 10)

# Scatter Plot: ApplicantIncome vs CoapplicantIncome
data.plot(x='ApplicantIncome', y='CoapplicantIncome', kind='scatter', title='Income Scatter')
plt.xlabel("Applicant Income")
plt.ylabel("Coapplicant Income")
plt.grid(True)
plt.tight_layout()
plt.show()

# Histogram: Coapplicant Income distribution grouped by Applicant Income
data.plot(x='ApplicantIncome', y='CoapplicantIncome', kind='hist', bins=30, title='Histogram of Coapplicant Income')
plt.xlabel("Coapplicant Income")
plt.tight_layout()
plt.show()



