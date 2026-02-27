# Decision Tree Visualization
# Use:
# from sklearn.tree import plot_tree
# Visualize the trained decision tree.
# Which feature appears at the root node?
# Why do you think that feature was selected first?

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier , plot_tree

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

    print(Border)
    print("Decision Tree Visualization")
    print(Border)
    
    plt.figure(figsize=(5, 3))
    plot_tree(
        model,
        feature_names = features,
        class_names = ["Fail", "Pass"],
        filled = True,
        fontsize = 8
    )
    plt.show()

    print(Border)
    print("Attendance appears at the root node because it is the most important feature and gives the purest split in the dataset.")
    print(Border)

if __name__ == "__main__":
    main()