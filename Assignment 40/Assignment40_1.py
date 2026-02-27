# Dataset Description – Student Performance ML Dataset
# The dataset student_performance_ml.csv contains academic and behavioral information of students.
# The objective of this dataset is to predict whether a student will Pass (1) or Fail (0) based on various input features.
# Each row in the dataset represents one student, and each column represents a measurable factor that may influence academic performance.

# Features Description:
# StudyHours – Number of hours a student studies per day.
# Attendance – Percentage of class attendance.
# PreviousScore – Marks obtained in the previous examination.
# AssignmentsCompleted – Number of assignments completed by the student.
# SleepHours – Average number of hours the student sleeps per day.
# FinalResult – Target variable (Output):
# 1 – Pass
# 0 – Fail

# Objective of the Dataset:
# Analyze how different factors affect student performance.
# Build a Machine Learning model to predict whether a student will pass or fail.
# Understand concepts such as training, testing, accuracy, confusion matrix, overfitting, and model evaluation.

# After training the Decision Tree model, use:
# model.feature_importances_
# Display importance score of each feature.
# Which feature contributes the most in predicting FinalResult?
# Which feature contributes the least?

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def main():

    Border = "-"*50

    Dataset = "student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    features = ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]

    X = df[features]
    Y = df["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)

    model = DecisionTreeClassifier(
        criterion = "gini",
        max_depth = 3,
        random_state = 42
    )

    model.fit(X_train, Y_train)

    print(Border)
    print("Feature importance :")

    importance = model.feature_importances_
    
    for feature, score in zip(features, importance):
        print(feature, ":", score)

    max_value = max(importance)
    print(Border)
    print("Feature contributing Most:")

    for feature, value in zip(features, importance):
        if value == max_value:
            print(feature)

    min_value = min(importance)
    print(Border)
    print("Features contributing Least:")

    for feature, value in zip(features, importance):
        if value == min_value:
            print(feature)

    print(Border)

if __name__ == "__main__":
    main()