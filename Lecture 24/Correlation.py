# Definition:
# • Correlation measures the strength and direction of a linear relationship between two variables. The correlation coefficient (Pearson's r) ranges from -1 to 1.
# Use Case:
# • Correlation analysis is used in finance to determine the relationship between different financial assets, helping in portfolio diversification.

import pandas as pd;
import numpy as np;
# Seed for reproducibility
np.random.seed(42)
#Generate sample data
data={
    'Age':np.random.normal(30,10,100).astype(int),
    'Annual Income (k$)':np.random.normal(50,20,100).astype(int),
    'Spending Score (1-100)':np.random.randint(1,100,100),
    'Years with company':np.random.normal(5,2,100).astype(int)
}
#create dataframe
df=pd.DataFrame(data)
print(df)
# Correlation matrix
from tabulate import tabulate
correlation_matrix=df.corr()
print(tabulate(correlation_matrix,headers='keys',tablefmt='grid',numalign="right",floatfmt=".2f"))