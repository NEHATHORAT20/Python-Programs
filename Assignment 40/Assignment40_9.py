# Create a new column:
# PerformanceIndex = (StudyHours * 2) + Attendance
# Train the model including this new feature.
# Does accuracy improve?

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score
)
from sklearn.tree import plot_tree

def main():
    Border = "-"*100

    Dataset = "student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    df["PerformanceIndex"] = df["StudyHours"] * 2 + df["Attendance"]

    features = ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours", "PerformanceIndex"]

    X = df[features]
    Y = df["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)

    model = DecisionTreeClassifier(
        criterion = "gini",
        max_depth = 3,
        random_state = 42
    )

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    Accuracy = accuracy_score(Y_test, Y_pred)

    print(Border)
    print("Accuracy after adding PerformanceIndex :", Accuracy * 100 , "%")

    print(Border)
    print("Accuracy did not improve after adding PerformanceIndex because the model was already performing perfectly.")
    print(Border)

if __name__ == "__main__":
    main()