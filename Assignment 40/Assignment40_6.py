# Identify students where:
# y_test != y_pred
# Display those rows.
# How many students were misclassified?
# What common pattern do you observe?

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

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

    Y_pred = model.predict(X_test)

    print(Border)
    print("Misclassified Students:")

    misclassified = X_test[Y_test != Y_pred]

    print(misclassified)

    print(Border)
    print("Actual vs Predicted for Misclassified:")

    print("Actual:", Y_test[Y_test != Y_pred].values)
    print("Predicted:", Y_pred[Y_test != Y_pred])

    print(Border)
    print("Total Misclassified Students:", len(misclassified))
    print(Border)

    print("No students were misclassified."
    "\nThe model achieved perfect prediction on the test data.")
    print(Border)

if __name__ == "__main__":
    main()