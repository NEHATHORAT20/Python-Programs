# Train model with:
# max_depth = None
# Calculate:
# Training accuracy
# Testing accuracy
# If training accuracy is 100% but testing accuracy is lower, explain why this happens.

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
        max_depth = None,
        random_state = 42
    )

    model.fit(X_train, Y_train)

    print(Border)
    train_pred = model.predict(X_train)
    train_accuracy = accuracy_score(Y_train, train_pred)
    print("Training accuracy is :", train_accuracy * 100 , "%")
    print(Border)
    
    test_pred = model.predict(X_test)
    test_accuracy = accuracy_score(Y_test, test_pred)
    print("Testing accuracy is :", test_accuracy * 100 , "%")

    print(Border)
    print("Training accuracy becomes 100% due to overfitting ,"
        " while testing accuracy decreases because the model"
        " memorizes training data instead of learning general patterns.")
    print(Border)
    
if __name__ == "__main__":
    main()