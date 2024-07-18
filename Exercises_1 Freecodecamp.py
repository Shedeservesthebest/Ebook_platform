#!/usr/bin/env python
# coding: utf-8

# ![rmotr](https://user-images.githubusercontent.com/7065401/52071918-bda15380-2562-11e9-828c-7f95297e4a82.png)
# <hr style="margin-bottom: 40px;">
# 
# <img src="https://user-images.githubusercontent.com/7065401/58563302-42466a80-8201-11e9-9948-b3e9f88a5662.jpg"
#     style="width:400px; float: right; margin: 0 40px 40px 40px;"></img>
# 
# # Exercises
# ## Bike store sales

# ![Red-divider](https://user-images.githubusercontent.com/7065401/52071927-c1cd7100-2562-11e9-908a-dde91ba14e59.png)
# 
# ## Hands on! 

# In[247]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[248]:


import os

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Change the current working directory to the Downloads directory
os.chdir(desktop_path)

# Verify the change
print("Current working directory:", os.getcwd())


# In[249]:


sales = pd.read_csv(
    'sales_data.csv',
    parse_dates=['Date'])


# In[250]:


sales.head()


# ![Red-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### What's the mean of `Customers_Age`?

# In[251]:


# your code goes here
sales['Customer_Age'].mean()


# Why don't you try with `.mean()`

# In[252]:


sales['Customer_Age'].mean()


# Go ahead and show a <b>density (KDE)</b> and a <b>box plot</b> with the `Customer_Age` data:

# In[253]:


# your code goes here
sales['Customer_Age'].plot(kind= 'density', figsize= (14,6))


# In[254]:


sales['Customer_Age'].plot(kind= 'box', figsize= (14,6))


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### What's the mean of `Order_Quantity`?

# In[255]:


# your code goes here
sales['Order_Quantity'].mean()


# In[256]:


sales['Order_Quantity'].mean()


# In[257]:


sales['Order_Quantity'].plot(kind= 'hist', figsize=(14,6))


# In[258]:


# your code goes here
sales['Order_Quantity'].plot(kind= 'box', figsize=(6,6))


# Go ahead and show a <b>histogram</b> and a <b>box plot</b> with the `Order_Quantity` data:

# In[259]:


sales['Order_Quantity'].plot(kind='hist', bins=30, figsize=(14,6))


# In[260]:


sales['Order_Quantity'].plot(kind='box', vert=False, figsize=(14,6))


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### How many sales per year do we have?

# In[147]:


sales.columns


# In[148]:


# your code goes here
sales['Year'].value_counts()


# In[149]:


sy= sales['Year'].value_counts()


# Go ahead and show a <b>pie plot</b> with the previous data:

# In[150]:


# your code goes here
sy.plot(kind='pie')


# In[266]:


sales['Year'].value_counts().plot(kind='pie', figsize=(5,5))


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### How many sales per month do we have?

# In[152]:


# your code goes here
sales['Month'].value_counts()


# Go ahead and show a <b>bar plot</b> with the previous data:

# In[153]:


# your code goes here
s_m = sales['Month'].value_counts()
s_m.plot(kind= 'bar')


# In[154]:


sales['Month'].value_counts().plot(kind='bar', figsize=(14,6))


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Which country has the most sales `quantity of sales`?

# In[155]:


# your code goes here
sales['Country'].value_counts().max()

# I didn't know how to move forward here.


# In[156]:


sc = sales['Country'].value_counts().head(1)


# In[157]:


sales['Country'].value_counts()


# Go ahead and show a <b>bar plot</b> of the sales per country:

# In[158]:


# your code goes here
sales['Country'].value_counts().plot(kind='bar',figsize=(14,6))


# In[159]:


sales['Country'].value_counts()


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Create a list of every product sold

# In[160]:


# your code goes here
sales['Product'].unique()


# In[161]:


#sales.loc[:, 'Product'].unique()

sales['Product'].unique()


# Create a **bar plot** showing the 10 most sold products (best sellers):

# In[162]:


# your code goes here
sales['Product'].value_counts().head(10).plot(kind='bar', figsize=(14,6))


# In[163]:


sales['Product'].value_counts().head(10).plot(kind='bar', figsize=(14,6))


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Can you see any relationship between `Unit_Cost` and `Unit_Price`?
# 
# Show a <b>scatter plot</b> between both columns.

# In[164]:


# your code goes here
sales.plot(kind='scatter', x='Unit_Cost', y='Unit_Price', figsize=(6,6))


# In[165]:


sales.plot(kind='scatter', x='Unit_Cost', y='Unit_Price', figsize=(6,6))


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Can you see any relationship between `Order_Quantity` and `Profit`?
# 
# Show a <b>scatter plot</b> between both columns.

# In[166]:


# your code goes here
sales.plot(kind = 'scatter', x='Order_Quantity', y='Profit')


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Can you see any relationship between `Profit` per `Country`?
# 
# Show a grouped <b>box plot</b> per country with the profit values.

# In[168]:


sales[['Profit','Country']].boxplot(by='Country')


# In[169]:


# your code goes here
sales[['Profit', 'Country']].boxplot(by='Country', figsize=(10,6))


# In[170]:


sales[['Profit', 'Country']].boxplot(by='Country', figsize=(10,6))


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Can you see any relationship between the `Customer_Age` per `Country`?
# 
# Show a grouped <b>box plot</b> per country with the customer age values.

# In[171]:


sales[['Customer_Age', 'Country']].boxplot(by='Country', figsize=(10,6))


# In[172]:


# your code goes here
sales[['Profit', 'Country']].boxplot(by='Country', figsize=(10,6))


# In[173]:


sales[['Customer_Age', 'Country']].boxplot(by='Country', figsize=(10,6))


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Add and calculate a new `Calculated_Date` column
# 
# Use `Day`, `Month`, `Year` to create a `Date` column (`YYYY-MM-DD`).

# In[179]:


# your code goes here

Date = sales[['Year', 'Month', 'Day']]


# In[180]:


sales['Calculated_Date'] = sales[['Year', 'Month', 'Day']].apply(lambda x: '{}-{}-{}'.format(x[0], x[1], x[2]), axis=1)

sales['Calculated_Date'].head()


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Parse your `Calculated_Date` column into a datetime object

# In[176]:


# your code goes here
month_mapping = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4, 
    'May': 5, 'June': 6, 'July': 7, 'August': 8, 
    'September': 9, 'October': 10, 'November': 11, 'December': 12
}

sales['Month'] = sales['Month'].map(month_mapping)
sales['Calculated_Date'] = pd.to_datetime(sales[['Year', 'Month', 'Day']])


print(sales['Calculated_Date'].head())


# In[177]:


sales['Calculated_Date'] = pd.to_datetime(sales['Calculated_Date'])

sales['Calculated_Date'].head()


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### How did sales evolve through the years?
# 
# Show a <b>line plot</b> using `Calculated_Date` column as the x-axis and the count of sales as the y-axis.

# In[185]:


sales.columns


# In[194]:


import seaborn as sns


# In[205]:


# your code goes here
sales['Calculated_Date'].value_counts().plot(kind='line', figsize=(14,6))


# In[204]:


sales['Calculated_Date'].value_counts().plot(kind='line', figsize=(14,6))


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Increase 50 U$S revenue to every sale

# In[208]:


# your code goes here
sales['Revenue'] += 50


# In[132]:


#sales['Revenue'] = sales['Revenue'] + 50

sales['Revenue'] += 50


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### How many orders were made in `Canada` or `France`?

# In[214]:


# your code goes here
sales.loc[(sales['Country'] == 'Canada')|(sales['Country'] == 'France')].shape[0]


# In[114]:


sales.loc[(sales['Country'] == 'Canada') | (sales['Country'] == 'France')].shape[0]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### How many `Bike Racks` orders were made from Canada?

# In[215]:


# your code goes here
sales.loc[(sales['Country'] == 'Canada') & (sales['Sub_Category'] == 'Bike Racks')].shape[0]


# In[ ]:


sales.loc[(sales['Country'] == 'Canada') & (sales['Sub_Category'] == 'Bike Racks')].shape[0]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### How many orders were made in each region (state) of France?

# In[216]:


# your code goes here
france_states = sales.loc[sales['Country'] == 'France', 'State'].value_counts()

france_states


# In[ ]:


france_states = sales.loc[sales['Country'] == 'France', 'State'].value_counts()

france_states


# Go ahead and show a <b>bar plot</b> with the results:

# In[218]:


# your code goes here
france_states.plot(kind = 'bar', figsize=(14,6))


# In[ ]:


france_states.plot(kind='bar', figsize=(14,6))


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### How many sales were made per category?

# In[219]:


# your code goes here
sales['Product_Category'].value_counts()


# In[222]:


ct = sales['Product_Category'].value_counts()


# Go ahead and show a <b>pie plot</b> with the results:

# In[223]:


# your code goes here
ct.plot(kind = 'pie')


# In[ ]:


sales['Product_Category'].value_counts().plot(kind='pie', figsize=(6,6))


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### How many orders were made per accessory sub-categories?

# In[224]:


# your code goes here
accessories = sales.loc[sales['Product_Category'] == 'Accessories', 'Sub_Category'].value_counts()

accessories


# In[ ]:


accessories = sales.loc[sales['Product_Category'] == 'Accessories', 'Sub_Category'].value_counts()

accessories


# Go ahead and show a <b>bar plot</b> with the results:

# In[225]:


# your code goes here
accessories.plot(kind = 'bar')


# In[ ]:


accessories.plot(kind='bar', figsize=(14,6))


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### How many orders were made per bike sub-categories?

# In[272]:


# your code goes here
bikes = sales.loc[sales['Product_Category'] == 'Bikes', 'Sub_Category'].value_counts()

bikes


# In[270]:


bikes = sales.loc[sales['Product_Category'] == 'Bikes', 'Sub_Category'].value_counts()

bikes


# Go ahead and show a <b>pie plot</b> with the results:

# In[271]:


# your code goes here
bikes.plot(kind='pie', figsize=(6,6))


# In[ ]:


bikes.plot(kind='pie', figsize=(6,6))


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Which gender has the most amount of sales?

# In[226]:


# your code goes here
sales['Customer_Gender'].value_counts()


# In[ ]:


sales['Customer_Gender'].value_counts()


# In[229]:


sales['Customer_Gender'].value_counts().plot(kind='bar')


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### How many sales with more than 500 in `Revenue` were made by men?

# In[268]:


# your code goes here
sales.loc[(sales['Customer_Gender'] == 'M') & (sales['Revenue'] >= 500)].shape[0]


# In[267]:


# This isn't for more than 500
sales.loc[(sales['Customer_Gender'] == 'M') & (sales['Revenue'] == 500)].shape[0]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Get the top-5 sales with the highest revenue

# In[283]:


# your code goes here
sales.sort_values(['Revenue'], ascending=False).head(5)


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Get the sale with the highest revenue

# In[ ]:


# your code goes here
#sales.sort_values(['Revenue'], ascending=False).head(1)

cond = sales['Revenue'] == sales['Revenue'].max()

sales.loc[cond]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### What is the mean `Order_Quantity` of orders with more than 10K in revenue?

# In[274]:


# your code goes here
OQ = sales['Revenue'] > 10_000

sales.loc[OQ, 'Order_Quantity'].mean()


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### What is the mean `Order_Quantity` of orders with less than 10K in revenue?

# In[234]:


# your code goes here
moq = sales['Revenue'] < 10_000

sales.loc[moq , 'Order_Quantity'].mean()



# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### How many orders were made in May of 2016?

# In[243]:


# your code goes here
cond = (sales['Year'] == 2016) & (sales['Month'] == 'May')

sales.loc[cond].shape[0]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### How many orders were made between May and July of 2016?

# In[262]:


# your code goes here
cond = (sales['Year'] == 2016) & (sales['Month'].isin(['May', 'June', 'July']))

sales.loc[cond].shape[0]


# Show a grouped <b>box plot</b> per month with the profit values.

# In[263]:


# your code goes here
profit_2016 = sales.loc[sales['Year'] == 2016, ['Profit', 'Month']]

profit_2016.boxplot(by='Month', figsize=(14,6))


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Add 7.2% TAX on every sale `Unit_Price` within United States

# In[273]:


# your code goes here

#sales.loc[sales['Country'] == 'United States', 'Unit_Price'] = sales.loc[sales['Country'] == 'United States', 'Unit_Price'] * 1.072

sales.loc[sales['Country'] == 'United States', 'Unit_Price'] *= 1.072
sales['Unit_Price']


# ![purple-divider](https://user-images.githubusercontent.com/7065401/52071927-c1cd7100-2562-11e9-908a-dde91ba14e59.png)
