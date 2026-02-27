# Create a new DataFrame with details of 5 new students.
# Use the trained model to predict their results.
# Display predictions clearly.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():

    Border = "-"*100

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

    New_Dataframe = pd.read_csv("New_Student_Data.csv")

    Y_pred = model.predict(New_Dataframe[["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted"]])

    print(Border)
    print("New Student Data's Actual Values :")
    print(New_Dataframe["FinalResult"])

    print(Border)
    print("New Student Data's Predicted Values :", Y_pred)
    print(Border)

if __name__ == "__main__":
    main()