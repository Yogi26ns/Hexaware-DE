import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Optional: Ignore warnings for cleaner output
warnings.filterwarnings('ignore')

# Load the dataset
file_path = r"C:\Users\nsyog\Downloads\LoanData (1).csv"
  # Update path if needed
data = pd.read_csv(file_path)

# Set plot style and size
plt.style.use('fivethirtyeight')
plt.rcParams['figure.figsize'] = (15, 5)

# Create subplots for boxplots
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
sns.boxplot(x=data['ApplicantIncome'])
plt.title("Applicant Income")

plt.subplot(1, 3, 2)
sns.boxplot(x=data['CoapplicantIncome'])
plt.title("Coapplicant Income")

plt.subplot(1, 3, 3)
sns.boxplot(x=data['LoanAmount'])
plt.title("Loan Amount")

plt.suptitle('Outliers Detection', fontsize=16)
plt.tight_layout(pad=2.0)
plt.show()