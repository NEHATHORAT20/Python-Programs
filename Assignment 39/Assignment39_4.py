# Generate confusion matrix using sklearn.
# Display it using ConfusionMatrixDisplay.
# Explain clearly:
# True Positive
# True Negative
# False Positive
# False Negative

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay
)

def main():

    Border = "-"*50

    Dataset = "student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    features = ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]

    X = df[features]
    y = df["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier(
        criterion="gini",
        max_depth=3,
        random_state=42
    )

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)
    
    conf_matrix = confusion_matrix(Y_test, Y_pred)

    print(Border)
    print("Confusion matrix : ")
    print(conf_matrix)
    print(Border)

    Display = ConfusionMatrixDisplay(confusion_matrix = conf_matrix)
    Display.plot()

    plt.title("Confusion Matrix")
    plt.show()
    
if __name__ == "__main__":
    main()

# TP -> True Positive -> if actual value is PASS then it give PASS.(Correct Pass prediction)
# TN -> True Negative -> if actual value is FAIL then it give FAIL.(Correct Fail prediction)
# FP -> Flase Positive -> if actual value is FAIL then it give PASS.(Predicted Pass but actually Fail)
# FN -> Flase Negative -> if actual value is PASS then it give FAIL.(Predicted Fail but actually Pass)