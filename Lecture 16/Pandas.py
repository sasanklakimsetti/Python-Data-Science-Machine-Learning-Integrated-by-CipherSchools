#Definition: Pandas is a powerful and flexible opensource data analysis and manipulation library for Python
#provides data structures like Series (one-dimensional) and DataFrame (two-dimensional) that are efficient f
#handling large datasets. Pandas allows for data manipulation, aggregation, and merging.
#Use Case in Real Life: Pandas can be used in various data analysis scenarios, such as customer data
#analysis, financial data analysis, and marketing campaign analysis.

import pandas as pd;

# creating a dataframe from a dictionary
data={
    'Name': ['Alice','Bob','Charlie'],
    'Age':[25,30,35],
    'City':['New York','Los Angeles','Chicago']
}
df=pd.DataFrame(data)
print(df)
print("\n")
# creating a dataframe from a list of dictionaries
data1=[
    {'Name':'Alice', 'Age':25, 'City':'New York'},
    {'Name':'Bob', 'Age':30, 'City':'Los Angeles'},
    {'Name':'Charlie', 'Age':35, 'City':'Chicago'}
]
df1=pd.DataFrame(data1)
print(df1)

#creating a dataframe from a csv file
df2=pd.read_csv("Lecture 16\Mall_Customers.csv")
print(df2.head())  # prints the first 5 rows
print(df2.head(10)) #prints the first 10 rows
print(df2.tail())  #last 5 rows
print(df2.info())  #getting whole information of the dataframe about non-null,null,datatype
print(df2.describe()) # getting whole statistics in description form for every column
# Selecting a single column
print(df2['Genre'])
#selecting multiple columns
print(df2[['Age','CustomerID']])
#Filtering rows
#filtering rows based on condition
print(df2[df2['CustomerID']>100])
#Adding new columns
df2['ID']=range(1,len(df2)+1)  # no.of values must be equal to no.of rows
print(df2.head())
#modifying existing columns
df2['ID']=df2['ID']+1
print(df2.head())
#Dropping columns and rows
df2=df2.drop(columns=['ID'])
print(df2.head())
df2=df2.drop(index=1)  #dropping rows
print(df2.head())
#Grouping data
grouped=df2.groupby('Genre')
print(grouped['CustomerID'].mean())
#aggregating data
aggregrated=df2.groupby('CustomerID').agg({'Annual Income (k$)':['mean','min','max']})
print(aggregrated)

#merging dataframes
df3=pd.DataFrame({'ID':[1,2,3],'Name':['Alice','Bob','Charlie']})
df4=pd.DataFrame({'ID':[1,2,4],'Salary':[5000,6000,7000]})
#merging dataframes on a column
merged_df=pd.merge(df3,df4,on='ID',how='inner')  #this is like inner join is sql i.e. the merging of dataframe will be done on same IDs as mentioned in 'on' part. how defines which join to be applied
print(merged_df)
merged_df2=pd.merge(df3,df4,on='ID',how='outer')
print(merged_df2)

#joining dataframes
joined_df=df3.join(df4,how='left')  #applies left join between them
print(joined_df)