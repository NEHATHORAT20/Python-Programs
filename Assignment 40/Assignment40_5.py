# Without using accuracy_score, manually calculate accuracy:
# Verify whether it matches sklearn accuracy.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix

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

    conf_matrix = confusion_matrix(Y_pred, Y_test)

    print(Border)
    print("Confusion matrix : ")
    print(conf_matrix)

    # Confusion matrix :
    # [[5 0]    -> TP = 5, FP = 0
    #  [0 1]]   -> FN = 0, TN = 1

    # Accuracy_matrix = ((TP + TN) / (TP + TN + FP + FN)) * 100

    Manual_Accuracy = ((5 + 1) / (5 + 1 + 0 + 0)) * 100

    print(Border)
    print("Manual Accuracy :", Manual_Accuracy , "%")
    print(Border)

if __name__ == "__main__":
    main()