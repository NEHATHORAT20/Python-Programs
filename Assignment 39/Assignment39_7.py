# Use the trained model to predict result for a student with:
# StudyHours = 6
# Attendance = 85
# PreviousScore = 66
# AssignmentsCompleted = 7
# SleepHours = 7
# Will the student Pass or Fail.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

def main():

    Border = "-"*50
    
    Dataset = "student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    features = ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]

    X = df[features]
    y = df["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

    model = DecisionTreeClassifier(
        criterion = "gini",
        max_depth = 3,
        random_state = 42
    )

    model.fit(X_train, Y_train)

    NewStudents = pd.DataFrame(
        [[6, 85, 66, 7, 7]],
        columns = ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]
    )

    Y_pred = model.predict(NewStudents)

    print(Border)
    if Y_pred == 1:
        print("Student will Pass")
    else:
        print("Student will Fail")
    print(Border)

if __name__ == "__main__":
    main()