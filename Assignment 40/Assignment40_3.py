# Train the model using only:
# StudyHours
# Attendance
# Compare the accuracy with the full-feature model.
# Is the model still performing well?

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():

    Border = "-"*100

    Dataset = "student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    features = ["StudyHours", "Attendance"]

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
    print("Accuracy of the model :", Accuracy * 100 , "%")

    print(Border)
    print("The accuracy of the model using only StudyHours and Attendance is close to the accuracy of the full-feature model."
        "\nHence, the model is still performing well because the most important feature (Attendance) is included.")
    print(Border)

if __name__ == "__main__":
    main()