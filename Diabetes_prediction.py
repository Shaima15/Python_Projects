
#Project 1: Diabetes Prediction
#importing dependencies 

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

#Data collection and analysis

Diab = pd.read_csv('C:/Users/shaim/Downloads/diabetes.csv') 

Diab.head()

#number of rows and column 
Diab.shape

#getting statistical measures of the data 

Diab.describe()

#returns count for outcome type (0,1)

Diab['Outcome'].value_counts()

#returns mean for each column

Diab.groupby('Outcome').mean()

#separating data and labels
x= Diab.drop(columns= 'Outcome', axis =1) #separates the column named outcome from the 
#rest of the columns. axis = 1 should be specified when we are dealing with columns but
#we should use 0 if we are dealing with rows.
y= Diab['Outcome'] #stores the column outcome in y variable 

# data standardisation

Scaler = StandardScaler()
Scaler.fit(x) 
Diab_stand= Scaler.transform(x)

New_x = Diab_stand

#Train Test Split

New_x_train, New_x_test, y_train, y_test = train_test_split(New_x, y, test_size = 0.2,
                                                            stratify= y, random_state=2) 
#model training 

Classifier= svm.SVC(kernel= 'linear')

#training the SVM classifier

Classifier.fit(New_x_train,y_train)

#model evaluation 
#accuracy score

New_x_train_pred= Classifier.predict(New_x_train)
training_accuracy= accuracy_score(New_x_train_pred, y_train)

print('Accuracy score of training data :' ,training_accuracy)

#accuracy score on test data

New_x_test_pred= Classifier.predict(New_x_test)
test_accuracy = accuracy_score(New_x_test_pred, y_test)

print('Accuracy Score on Test data:', test_accuracy)

#making a predictive system 

input_data =(8,167,106,46,231,37.6,0.165,43)

#convert the list above to numpy array

Input_to_numpy_array = np.asarray(input_data)

#reshape the array as we are predicting for one instance 
input_data_reshaped = Input_to_numpy_array.reshape(1,-1)

#standardize the input data 
std_data = Scaler.transform(input_data_reshaped)
print(std_data)

prediction= Classifier.predict(std_data)
print(prediction)

if prediction[0] == 0: 
    print('The patient is not diabetic')
else: 
    print('The patient is diabetic')
