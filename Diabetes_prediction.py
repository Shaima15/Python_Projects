
# Diabetes Prediction 


import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

#Data exploration

Diab = pd.read_csv('C:/Users/shaim/Downloads/diabetes.csv') 

Diab.head()

Diab.describe()

#separating data and labels
X= Diab.drop(columns= 'Outcome', axis =1) #separates the column named outcome from the 
#rest of the columns. axis = 1 should be specified when we are dealing with columns but
#we should use 0 if we are dealing with rows.
y= Diab['Outcome'] #stores the column outcome in y variable 

#Decision tree

# Split the data into training and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the model on the training set
model = DecisionTreeClassifier(random_state=0)
model.fit(X_train, y_train)

# Evaluate the model on the testing set
y_pred = model.predict(X_test)

# Print evaluation metrics
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Neural net 

# Train the model
model = MLPClassifier(hidden_layer_sizes=(100,), max_iter=500, random_state=0)
model.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = model.predict(X_test)

# Evaluate the model's performance
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
