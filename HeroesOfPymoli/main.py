#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


# Dependencies and Setup
import pandas as pd
import numpy as np
# File to Load (Remember to Change These)


# Read Purchasing File and store into Pandas data frame
df = pd.read_csv('Resources/purchase_data.csv')
df


# ## Player Count

# * Display the total number of players
# 

# In[2]:


players = df['SN'].unique()
players


# In[3]:


len(players)


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[4]:


items = df['Item Name'].unique()


# In[5]:


len(items)


# In[6]:


avgprice = df['Price'].mean()
avgprice


# In[7]:


len(df['Purchase ID'])


# In[8]:


rev = df['Price'].sum()
rev


# In[9]:


summary = [{"Unique Items": '179', 'Average Price': '$3.05', 'Purchases': '780', 'Revenue':'$2379.77'}]
summ_df = pd.DataFrame(summary)
summ_df


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[10]:


unique_df = df.drop_duplicates(subset = ['SN'])
unique_df['Gender'].value_counts()


# In[11]:


Male = (484/ (len(unique_df))) * 100
Female = (81 / (len(unique_df))) * 100
Other = (11 / (len(unique_df))) * 100
print(Male)
print(Female)
print(Other)


# In[12]:


#better way I found later to do above
unique_df['Gender'].value_counts(normalize = True)


# In[13]:


gendersumm_df = pd.DataFrame(
    {"Gender": ["Male", "Female", "Other"],
    "Toatl Count": ["484", "81", "11"],
    "Percentage of Players": ["84.03%", "14.06%", "1.91%"]})
gendersumm_df


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[14]:


gender_group_df = df.groupby(['Gender'])


# In[15]:


gender_group_df.count()


# In[16]:


gender_group_df["Price"].mean()


# In[17]:


gender_group_df["Price"].sum()


# In[18]:


FemAvg = 361.94 / 81
MaleAvg = 1967.64 / 484
OtherAvg = 50.19 / 11
print(FemAvg)
print(MaleAvg)
print(OtherAvg)


# In[19]:


GenderAnalysis_df = pd.DataFrame(
    {'Gender': ['Male', 'Female', 'Other'],
    'Purchase Count': ['652', '113', '15'],
    'Average Purchase Price': ['$3.02', '$3.20', '$3.35'],
    'Total Purchase Value': ['$1967.64','361.94', '50.19'],
    'Avg Purchase Total per Person': ['$4.07', '$4.47', '$4.56']})
GenderAnalysis_df


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[20]:


bins = [0, 9, 14, 19, 24, 29, 34, 39, 100]
group_names = ['<10', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40+']


# In[21]:


df['Age Bin'] = pd.cut(df['Age'], bins, labels = group_names, include_lowest = True)
df


# In[22]:


unique_df = df.drop_duplicates(subset = ['SN'])
unique_df


# In[23]:


Age_Count_df = unique_df['Age Bin'].value_counts(sort = False)
pd.DataFrame(Age_Count_df)


# In[24]:


Percent_of_Players_df = unique_df['Age Bin'].value_counts(normalize = True, sort = False)
pd.DataFrame(Percent_of_Players_df)


# In[25]:


Age_Demo_df = pd.merge(Age_Count_df, Percent_of_Players_df, left_index = True, right_index = True, how = 'outer')
Age_Demo_df = Age_Demo_df.rename(columns = {'Age Bin_x':'Player Count', 'Age Bin_y':'Percent of Players'})
Age_Demo_df


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[26]:


df


# In[27]:


age_group_df = df.groupby(['Age Bin'])


# In[28]:


age_purchase_count_df = age_group_df['Purchase ID'].count()
pd.DataFrame(age_purchase_count_df)


# In[29]:


age_avg_df = age_group_df["Price"].mean()
pd.DataFrame(age_avg_df)


# In[30]:


age_sum_df = age_group_df["Price"].sum()
pd.DataFrame(age_sum_df)


# In[31]:


Age_Summ_df = pd.merge(age_purchase_count_df, age_avg_df, on = 'Age Bin')
Age_Summ_df


# In[32]:


Age_Summ_df = pd.merge(Age_Summ_df, age_sum_df, on = 'Age Bin')
Age_Summ_df


# In[33]:


Age_Summ_df['Average Total Purchase per Person'] = (age_group_df["Price"].sum() / unique_df['Age Bin'].value_counts(sort = False))


# In[34]:


Age_Summ_df = Age_Summ_df.rename(columns = {'Purchase ID': 'Purchase Count', 'Price_x':'Average Purchase Price', 'Price_y':'Total Purchase Value'})
Age_Summ_df


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[35]:


sn_avg_df = df.groupby('SN').mean()
sn_avg_df.drop(columns=['Purchase ID', 'Age', 'Item ID'], axis=1, inplace=True)
sn_avg_df.rename(columns={'Price':'Average Purchase Price'}, inplace=True)
sn_avg_df


# In[36]:


sn_tot_df = df.groupby('SN').sum()
sn_tot_df.drop(columns=['Purchase ID', 'Age', 'Item ID'], axis=1, inplace=True)
sn_tot_df.rename(columns={'Price':'Total Purchase Value'}, inplace=True)
sn_tot_df


# In[37]:


sn_count_df = df.groupby('SN').count()
sn_count_df.drop(columns=['Purchase ID', 'Age', 'Gender', 'Item ID', 'Item Name', 'Price'], axis=1, inplace=True)
sn_count_df.rename(columns={'Age Bin':'Purchase Count'}, inplace=True)
sn_count_df


# In[38]:


Top_Spenders_df = pd.merge(sn_count_df, sn_avg_df, on = 'SN')
Top_Spenders_df = pd.merge(Top_Spenders_df, sn_tot_df, on = 'SN')
Top_Spenders_df = Top_Spenders_df.sort_values('Total Purchase Value', ascending=False)
Top_Spenders_df


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, average item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[45]:


item_count_df = df.groupby('Item ID').count()
item_count_df.drop(columns=['Purchase ID', 'Age', 'Gender', 'Item Name', 'Price', 'Age Bin'], axis=1, inplace=True)
item_count_df.rename(columns={'SN':'Purchase Count'}, inplace=True)
item_count_df


# In[49]:


item_avg_df = df.groupby('Item ID').mean()
item_avg_df.drop(columns=['Purchase ID', 'Age'], axis=1, inplace=True)
item_avg_df.rename(columns={'Price':'Item Price'}, inplace=True)
item_avg_df


# In[53]:


item_tot_df = df.groupby('Item ID').sum()
item_tot_df.drop(columns=['Purchase ID', 'Age'], axis=1, inplace=True)
item_tot_df.rename(columns={'Price':'Total Purchase Value'}, inplace=True)
item_tot_df


# In[58]:


item_name_df = df.drop_duplicates(subset=['Item ID'])
item_name_df.drop(columns=['Purchase ID', 'SN', 'Age', 'Gender', 'Price', 'Age Bin'], inplace=True)
item_name_df


# In[68]:


Most_Pop_Item_df = pd.merge(item_name_df, item_count_df, on='Item ID')
Most_Pop_Item_df = pd.merge(Most_Pop_Item_df, item_avg_df, on='Item ID')
Most_Pop_Item_df = pd.merge(Most_Pop_Item_df, item_tot_df, on='Item ID')
Most_Pop_Item_df.sort_values(['Purchase Count', 'Total Purchase Value'], ascending =False)


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[66]:


Most_Pop_Item_df.sort_values('Total Purchase Value', ascending =False)

