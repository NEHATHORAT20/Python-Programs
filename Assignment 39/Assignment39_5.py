# Calculate:
# Training accuracy
# Testing accuracy
# Compare both and comment whether the model is overfitting or underfitting.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

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

    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)
    
    Train_Accuracy = accuracy_score(Y_train, train_pred)
    Test_Accuracy = accuracy_score(Y_test, test_pred)

    print(Border)
    print("Training accuracy :", Train_Accuracy * 100 , "%")
    print("Testing accuracy :", Test_Accuracy * 100 , "%")
    print(Border)

    if Train_Accuracy > Test_Accuracy:
        print("Model may be Overfitting")
    else:
        print("Model is balanced well")
    print(Border)
    
if __name__ == "__main__":
    main()