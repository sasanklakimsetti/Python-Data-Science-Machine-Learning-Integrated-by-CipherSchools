#creating interactive visualizations with plotly
#Definition:
#• Plotly: Plotly is a graphing library that makes interactive. publication-quality graphs online. It supports a wide variety of charts, including
#line plots, scatter pl&. bar charts. histograms. heatmaps, and more. Plotly is particularly useful for creating interactive visualizations that
#can be embedded in web applications and shared online.
#Key Features of Plotly
#I. Interactivity: Plotly charts are interactive by default. allowing users to zoom. pan. and hover over data points to get more information.
#2. Wide Range of Chart Types: Plotly supports a variety of chart types, including basic plots, statistical plots. 3D plots, and maps.
#3. Customization: Extensive options to customize the appearance and behavior of charts.
#4. integration: Easy integration with web applications and other libraries like Dash for building interactive dashboards,

import pandas as pd
#loading the dataset
filepath='C:\Personal Coding\Python, Data Science & Machine Learning Integrated by CipherSchools\Lecture 19\sales_data (1).csv'
df=pd.read_csv(filepath)
print(df.head())
import plotly.express as px
#create a line plot
fig1=px.line(df,x='Date',y='Sales',title='Sales trend over time',markers=True)
fig1.show()

#creating a bar chart
fig2=px.bar(df,x='Region',y='Sales',title='Sales by Region',color='Region')
fig2.show()

#creating a scatter plot
fig3=px.scatter(df,x='Sales',y='Profit',title='Sales vs Profit',color='Region',size='Quantity',hover_data=['Product'])
fig3.show()

#creating a histogram
fig4=px.histogram(df,x='Sales',title='Distribution of Sales',nbins=10)
fig4.show()

#creating a piechart
fig5=px.pie(df,values='Sales',names='Product',title='Sales Distribution by Product')
fig5.show()

#creating an interactive line plot
fig6=px.line(df,x='Date',y='Sales',title='Interactive sales over time',markers=True,color='Region',hover_data=['Product'])
fig6.show()

data={
    'City':['New York','Los Angeles','Chicago','Houston','Phoenix'],
    'State':['NY','IL','TX','AZ'],
    'Population':[8419000,3980400,2716000,2328000,1690000]
}
#Creating the dataframe
df=pd.DataFrame(data)
#create a geographical map
fig=px.choropleth(df,locations='State',locationmode='USA-States',color_continuous_midpoint='Population',scope='usa',title='Population by areas')
fig.show()

