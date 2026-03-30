import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

def main():

    Border = "-"*100
    
    #-----------------------------------------------------
    # Step 1 - Exploratory Data Analysis(EDA)
    #-----------------------------------------------------

    df = pd.read_csv("diabetes.csv")

    print(Border)
    print("First five records : ")
    print(df.head())
    print(Border)

    print("Missing values : ")
    print(df.isnull().sum())
    print(Border)

    print("Statistical Summary : ")
    print(df.describe())
    print(Border)

    print(Border)
    print("Distribution of the target variable : ")
    sns.countplot(x='Outcome', data=df)
    plt.title("Target Variable Distribution")
    plt.show()
    print(Border)

    print(Border)
    print("Histogram of the target variable :")
    plt.figure(figsize=(8, 5))
    plt.hist(df['Outcome'], bins=10, color='green', edgecolor='black')
    plt.title("Histogram of Outcome")
    plt.show()
    print(Border)

    print(Border)
    print("Outliers Visualization in the dataset :")
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df)
    plt.title("Boxplot for Outliers")
    plt.show()
    print(Border)

    print(Border)
    print("Pairplot of the dataset :")
    sns.pairplot(df, hue='Outcome')
    plt.show()
    print(Border)

    #-----------------------------------------------------
    # Step 2 - Data Preprocessing
    #-----------------------------------------------------

    cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]

    for col in cols:
        print(f"{col} -> Zero values : ", (df[col] == 0).sum())

    X = df.drop('Outcome', axis=1)
    Y = df['Outcome']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    print(Border)
    print("Dataset after scaling :")
    print(X_train[:10])
    print(Border)

    #-----------------------------------------------------
    # Step 3 - Model Building
    #-----------------------------------------------------

    model_1 = DecisionTreeClassifier(criterion='gini' , max_depth=5 , random_state=42)

    model_2 = KNeighborsClassifier(n_neighbors=3)

    model_3 = LogisticRegression(max_iter=200)

    model_1.fit(X_train, Y_train)
    model_2.fit(X_train, Y_train)
    model_3.fit(X_train, Y_train)

    Y_pred1 = model_1.predict(X_test)
    Y_pred2 = model_2.predict(X_test)
    Y_pred3 = model_3.predict(X_test)

    #-----------------------------------------------------
    # Step 4 - Model Evaluation
    #-----------------------------------------------------

    acc1 = accuracy_score(Y_test, Y_pred1)
    acc2 = accuracy_score(Y_test, Y_pred2)
    acc3 = accuracy_score(Y_test, Y_pred3)

    print(Border)
    print("Decision Tree Accuracy : ", acc1*100)
    print(Border)
    print("KNN Accuracy : ", acc2*100)
    print(Border)
    print("Logistic Regression Accuracy : ", acc3*100)
    print(Border)

    print(Border)
    print("Confusion Matrix - Decision Tree")
    cm1 = confusion_matrix(Y_test, Y_pred1)
    print(cm1)
    print(Border)

    print("Confusion Matrix - KNN")
    cm2 = confusion_matrix(Y_test, Y_pred2)
    print(cm2)
    print(Border)

    print("Confusion Matrix - Logistic Regression")
    cm3 = confusion_matrix(Y_test, Y_pred3)
    print(cm3)
    print(Border)

    print(Border)
    print("Classification Report - Decision Tree")
    print(classification_report(Y_test, Y_pred1))
    print(Border)

    print(Border)
    print("Classification Report - KNN")
    print(classification_report(Y_test, Y_pred2))
    print(Border)

    print(Border)
    print("Classification Report - Logistic Regression")
    print(classification_report(Y_test, Y_pred3))
    print(Border)

    print(Border)
    print("Visualization of confusion matrix for Decision Tree Classifier : ")
    sns.heatmap(cm1, annot=True, fmt='d', cmap='Blues')
    plt.title("Decision Tree Confusion Matrix")
    plt.show()
    print(Border)

    print(Border)
    print("Visualization of confusion matrix for K-Neighbour Classifier : ")
    sns.heatmap(cm2, annot=True, fmt='d', cmap='Blues')
    plt.title("KNN Confusion Matrix")
    plt.show()
    print(Border)

    print(Border)
    print("Visualization of confusion matrix for Logistic Regression : ")
    sns.heatmap(cm3, annot=True, fmt='d', cmap='Blues')
    plt.title("Logistic Regression Confusion Matrix")
    plt.show()
    print(Border)

    #-----------------------------------------------------
    # Step 5 - Final Output
    #-----------------------------------------------------

    print(Border)
    print("Actual values of target variable : ")
    print(Y_test.values)

    print(Border)
    print("Prediction - Decision Tree : ")
    print(Y_pred1)

    print(Border)
    print("Prediction - KNN : ")
    print(Y_pred2)

    print(Border)
    print("Prediction - Logistic Regression : ")
    print(Y_pred3)

    Prediction = pd.DataFrame({
        "Decision Tree": Y_pred1,
        "KNN": Y_pred2,
        "Logistic Regression": Y_pred3,
        "Actual": Y_test.values
    })

    Prediction.to_csv("Prediction.csv", index=False)

    print(Border)
    print("Predictions saved to Prediction.csv")

if __name__ == "__main__":
    main()