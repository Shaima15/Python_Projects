# -*- coding: utf-8 -*-
"""

@author: shaim
"""

####Code for the project###
import pandas as pd
#loads the excel file into python
HRdata= pd.read_excel('HR_Employee_Data.xlsx')
#produces an overview of the dataset 
HRdata.info()
HRdata.head()
#checks the number of observations
len(HRdata)
###########################################################################################
###Data cleaning###
##########################################################################################
# Checks for null values and creates a dataframe that sums them up for each column
missing_values = HRdata.isnull().sum()

#checks for duplicated rows in the dataframe and sums them up
HRdata.duplicated().sum()
#renames the average_montly_hours column to fix spelling mistake in montly
HRdata.rename(columns={'average_montly_hours':'average_monthly_hours'}, inplace=True)

#decting outliers##
#Creates boxplot for all numeric columns to visually check for outliers 
import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(x=HRdata['satisfaction_level']) 
plt.show()

sns.boxplot(x=HRdata['last_evaluation']) 
plt.show()

sns.boxplot(x=HRdata['number_project']) 
plt.show()

sns.boxplot(x=HRdata['average_monthly_hours']) 
plt.show()

sns.boxplot(x=HRdata['time_spend_company']) 
plt.show()

##dealing with outliers
#understanding whether the identified outliers are true values or errors

#create a dataframe using the pivot function to show how much time employees in 
#each department spend in the company
HRdata_pivot1= HRdata.pivot(columns='Department', values='time_spend_company')
#create boxplot to visualize the time spend in the company for managers
sns.boxplot(x= HRdata_pivot1['management']) 
plt.show()

#use the pivot function to create a dataframe that comprises of the salary levels
#for each department 
HRdata_pivot2= HRdata.pivot(columns='Department', values='salary')
#find the most common salary level for managers using the mode function
HRdata_pivot2.management.mode() 

#check if 10 is outlier or true value by comparing time_spend_company column with
#satisfaction_level column
#check the mean satisfaction level for employees at each time period spend in the company 
HRdata.pivot_table(values='satisfaction_level', index='time_spend_company', aggfunc='mean')

##############################################################################################
#descriptive analytics section
#######################################################################################
#initially, calculate the mean value for each variable
HRdata.mean()

#satisfaction and left column 
#create a new dataframe only containing satisfaction level for those who left and
#stayed
HRdata_pivot3= HRdata.pivot(columns='left', values='satisfaction_level')
HRdata_pivot3[1].mean() #mean satisfaction level for employees who left
HRdata_pivot3[0].mean() #mean satisfaction level for employees who did not leave

# create a histogram to visualize the distribution of satisfaction for employees
# a) employees who left
	
HRdata_pivot3[1].plot(kind='hist', bins=30)
plt.title('Distribution of Satisfaction Levels for Employees Who Left')
plt.xlabel('Satisfaction Level')
plt.ylabel('Frequency')
plt.legend()
plt.show()
#b)employees who did not leave
HRdata_pivot3[0].plot(kind='hist', bins=30)
plt.title('Distribution of Satisfaction Levels for Employees Who stayed')
plt.xlabel('Satisfaction Level')
plt.ylabel('Frequency')
plt.legend()
plt.show()

#department, satisfaction, and left columns 
#calculate the mean satisfaction level for each department 
HRdata.pivot_table(values='satisfaction_level', index='Department', aggfunc='mean')

#create a chart that shows current employees and those who left for each department 
plt.figure(figsize=(11,7))
sns.countplot(x="Department", hue="left", data=HRdata)
plt.show()

#create a dataframe containing satisfaction level for each department
HRdata_pivot= HRdata.pivot(columns='Department', values='satisfaction_level')

#calcualte the standard deviation for the satisfaction level in each department
HRstd= HRdata_pivot.std()
HRdata_pivot.std()

# Employee departure/left, number of projects, and last evaluation 
#a) departure and number of projects
#create a countplot showing the number of projects for both the employees who left
#and did not leave
sns.countplot(x="number_project", hue="left", data=HRdata)
plt.show()

#b) #departure and last evaluation
HRdata_pivot4= HRdata.pivot(columns='left', values='last_evaluation')
#create a histogram to show the distribution of the last evaluation percent 
#for employees who left
HRdata_pivot4[1].plot(kind='hist', bins=30)
plt.title('Distribution of last evaluation for Employees Who Left')
plt.xlabel('last_evaluation')
plt.ylabel('Frequency')
plt.legend()
plt.show()

#create a histogram to show the distribution of the last evaluation percent 
#for employees who stayed
HRdata_pivot4[0].plot(kind='hist', bins=30)
plt.title('Distribution of last evaluation for Employees Who stayed')
plt.xlabel('last_evaluation')
plt.ylabel('Frequency')
plt.legend()
plt.show()

#calculate the standard deviation of last evaluation for those who left and stayed
HRdata_pivot4.std()

#Salary, department, last evaluation, and employee departure
#a) salary and department
#create a count plot showing the count of salaries for each department 
plt.figure(figsize=(11,7))
sns.countplot(x="Department", hue="salary", data=HRdata)
plt.show()
 # b) department and left
#calcualte the mean value for those employees who left for each department
HRdata.pivot_table(values='left', index='Department', aggfunc='mean')
#c) #department and last evaluation 
#calculate the median value for the last evaluation column 
HRdata['last_evaluation'].median()
#use pivot table to calculate the median last evaluation value for each department
HRdata.pivot_table(values='last_evaluation', index='Department', aggfunc='median')

#Work accident and left
#create a count plot to compare the work accident between the employees who left 
#and did not leave 
sns.countplot(x="left", hue="Work_accident", data=HRdata)
plt.show()

#Average monthly hours and employee departure
#creates a dataframe that set left as the column and the average monthly hours
# as the values
HRdata_pivot5= HRdata.pivot(columns='left', values='average_monthly_hours')
#create a histogram to visualize the distribution of average monthly hours
#for the employees who left the company
HRdata_pivot5[1].plot(kind='hist', bins=30)
plt.title('Distribution of monthly hours worked for Employees Who Left')
plt.xlabel('average monthly hours')
plt.ylabel('Frequency')
plt.legend()
plt.show()

#create a histogram to visualize the distribution of average monthly hours
#for the employees who did not leave the company
HRdata_pivot5[0].plot(kind='hist', bins=30)
plt.title('Distribution of monthly hours worked for Employees Who stayed')
plt.xlabel('average monthly hours')
plt.ylabel('Frequency')
plt.legend()
plt.show()

#calculate the standard deviation of average monthly hours for those who left 
#and stayed
HRdata_pivot5.std()
##############################################################################
