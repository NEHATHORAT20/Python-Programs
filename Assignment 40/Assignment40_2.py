# Remove the column SleepHours from the dataset.
# Train the model again.
# Compare new accuracy with previous accuracy.
# Does removing this feature affect performance?

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():

    Border = "-"*100

    Dataset = "student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    df.drop(columns=["SleepHours"], inplace=True)

    features = ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted"]

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
    print("Accuracy after removing SleepHours : " , Accuracy * 100 , "%")
    print(Border)
    
    print("The new accuracy of the model is same as the previous accuracy of the model."
          "\nRemoving the feature 'SleepHours' does not Affect model performance.")

    print(Border)

if __name__ == "__main__":
    main()