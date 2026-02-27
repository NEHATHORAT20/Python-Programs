# Train three Decision Tree models with:
# max_depth = 1
# max_depth = 3
# max_depth = None
# Compare their testing accuracies and write observations.

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

    model1 = DecisionTreeClassifier(
        criterion = "gini",
        max_depth = 1,
        random_state = 42
    )

    model1.fit(X_train, Y_train)

    Y_pred = model1.predict(X_test)

    Accuracy_Score = accuracy_score(Y_test, Y_pred)
    
    print(Border)
    print("Accuracy of model1 with max_depth = 1 : " , Accuracy_Score * 100 , "%")

    model2 = DecisionTreeClassifier(
        criterion = "gini",
        max_depth = 3,
        random_state = 42
    )

    model2.fit(X_train, Y_train)

    Y_pred = model2.predict(X_test)

    Accuracy_Score = accuracy_score(Y_test, Y_pred)
    
    print(Border)
    print("Accuracy of model2 with max_depth = 3 : " , Accuracy_Score * 100 , "%")

    model3 = DecisionTreeClassifier(
        criterion = "gini",
        max_depth = None,
        random_state = 42
    )

    model3.fit(X_train, Y_train)

    Y_pred = model3.predict(X_test)

    Accuracy_Score = accuracy_score(Y_test, Y_pred)
    
    print(Border)
    print("Accuracy of model3 with max_depth = None : " , Accuracy_Score * 100 , "%")

    print(Border)
    print("The testing accuracy for all three models is 100 %")
    print(Border)
   
if __name__ == "__main__":
    main()