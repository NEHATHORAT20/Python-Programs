# Write a single structured Python program that performs:
# Dataset loading
# Data analysis
# Visualization
# Train-test split
# Model training
# Prediction
# Accuracy calculation
# Confusion matrix generation
# Final conclusion
# The code should include proper comments explaining each step.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

Border = "-"*100

##########################################################
# Step 1 - Load the dataset
##########################################################

print(Border)
print("Step 1- Load the Dataset")
print(Border)

Dataset = "student_performance_ml.csv"

df = pd.read_csv(Dataset)

print("Dataset gets loaded succesfully\n")

##########################################################
# Step 2 - Data Analysis (EDA)
##########################################################

print(Border)
print("Step 2 - Data Analysis")
print(Border)

print("Shape of dataset : ", df.shape)
print("Column names :", list(df.columns))

print("\nMissing Values : ")
print(df.isnull().sum())

print("\nClass Distribution : ")
print(df["FinalResult"].value_counts())

print("\nStatistical Report of dataset : ")
print(df.describe() , "\n")

##########################################################
# Step 3 - Visualisation of Dataset
##########################################################

print(Border)
print("Step 3 - Visualisation of Dataset")
print(Border)

plt.figure(figsize=(6, 4))

plt.hist(df["FinalResult"])

plt.title("Analysis of Students Data")
plt.xlabel("Pass = 1 OR Fail = 0")
plt.ylabel("Number Of Students")

plt.show()

##########################################################
# Step 4 - Split the dataset for training
##########################################################

print(Border)
print("Step 4 - Split the dataset for training")
print(Border)

# Test size = 20%
# Train size = 80%

features = ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]

X = df[features]
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)

print("Data Splitting Activity Done :")

print("X - Independent : ", X.shape)
print("Y - Dependent : ", Y.shape )

print("X_train : ", X_train.shape) 
print("X_test : ", X_test.shape) 

print("Y_train : ", Y_train.shape) 
print("Y_test : ", Y_test.shape , "\n") 

##########################################################
# Step 5 - Model selection and training
##########################################################

print(Border)
print("Step 5 - Model selection and training")
print(Border)

model = DecisionTreeClassifier(
    criterion = "gini",
    max_depth = 3,
    random_state = 42
)

model.fit(X_train, Y_train)

print("Model training completed\n")


##########################################################
# Step 6 - Prediction
##########################################################

print(Border)
print("Step 6 - Prediction")
print(Border)

Y_pred = model.predict(X_test)

print("Model prediction completed")
print(Y_pred.shape , "\n")

print("Actual Values : ")
print(Y_test , "\n")

print("Predicted Values : ")
print(Y_pred , "\n")

##########################################################
# Step 7 - Accuracy Calculation
##########################################################

print(Border)
print("Step 7 - Accuracy Calculation")
print(Border)

Accuracy = accuracy_score(Y_test, Y_pred)
print("Accuracy of model is :", Accuracy * 100 , "%\n")

##########################################################
# Step 8 - Confusion matrix
##########################################################

print(Border)
print("Step 8 - Confusion matrix")
print(Border)

conf_matrix = confusion_matrix(Y_test, Y_pred)

print("Confusion matrix :")
print(conf_matrix , "\n")

Display = ConfusionMatrixDisplay(confusion_matrix = conf_matrix)
Display.plot()

##########################################################
# Step 9 - Final Conclusion
##########################################################

print(Border)
print("Step 9 - Final Conclusion")
print(Border)

print("The Decision Tree model was successfully trained and evaluated.")
print("The model achieved an accuracy of : ", Accuracy * 100, "%")  

print(Border)