import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, 
    confusion_matrix, 
    classification_report, 
    roc_auc_score, 
    RocCurveDisplay, 
    ConfusionMatrixDisplay
)

def main():

    Border = "-" * 100

    #------------------------------------------------------------
    # Step 1 - Load the dataset
    #------------------------------------------------------------

    df = pd.read_csv("bank-full.csv", sep=";")

    #------------------------------------------------------------
    # Step 2 - Analysis of the dataset
    #------------------------------------------------------------

    print(Border)
    print("Shape of dataset : ")
    print(df.shape)

    print(Border)
    print("First few records : ")
    print(df.head())

    print(Border)
    print("Columns in dataset : ")
    print(list(df.columns))

    print(Border)
    print("Statistical Summary : ")
    print(df.describe())

    print(Border)
    print("Missing values of dataset : ")
    print(df.isnull().sum())

    #------------------------------------------------------------
    # Step 3 - Visualization of dataset
    #------------------------------------------------------------

    sns.countplot(x='y', data=df)
    plt.title("Target Variable Distribution")
    plt.show()

    #------------------------------------------------------------
    # Step 4 - Preprocessing and encoding
    #------------------------------------------------------------

    df = pd.get_dummies(df, drop_first=True)

    print(Border)
    print("Data after encoding:")
    print(df.head())

    # Target column becomes y_yes after encoding
    X = df.drop('y_yes', axis=1)
    Y = df['y_yes']

    #------------------------------------------------------------
    # Step 5 - Split the dataset 
    #------------------------------------------------------------

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    #------------------------------------------------------------
    # Step 6 - Feature Scaling
    #------------------------------------------------------------

    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    print(Border)
    print("Data after standerd Scalling :")
    print(X_train[:10])

    #------------------------------------------------------------
    # Step 7 - Training classification models
    #------------------------------------------------------------

    model_knn = KNeighborsClassifier(n_neighbors=5)  
    model_lr = LogisticRegression(max_iter=1000) 
    model_rf = RandomForestClassifier() 

    model_knn.fit(X_train, Y_train)
    model_lr.fit(X_train, Y_train)
    model_rf.fit(X_train, Y_train)

    Y_pred_knn = model_knn.predict(X_test)
    Y_pred_lr = model_lr.predict(X_test)
    Y_pred_rf = model_rf.predict(X_test)

    #------------------------------------------------------------
    # Step 8 - Evaluation of the model
    #------------------------------------------------------------

    knn_acc = accuracy_score(Y_test, Y_pred_knn)
    lr_acc = accuracy_score(Y_test, Y_pred_lr)
    rf_acc = accuracy_score(Y_test, Y_pred_rf)

    print(Border)
    print("Accuracy of using KNN :", knn_acc)
    print(Border)
    print("Accuracy of using Logistic Regression :", lr_acc)
    print(Border)
    print("Accuracy of using Random forest :", rf_acc)
    print(Border)

    print("Confusion Matrix of KNN :")
    knn_cm = confusion_matrix(Y_test, Y_pred_knn)
    print(knn_cm)
    print(Border)

    print("Confusion Matrix of Logistic Regression :")
    lr_cm = confusion_matrix(Y_test, Y_pred_lr)
    print(lr_cm)
    print(Border)

    print("Confusion Matrix of Random forest :")
    rf_cm = confusion_matrix(Y_test, Y_pred_rf)
    print(rf_cm)
    print(Border)

    print("Classification report of KNN :")
    knn_cr = classification_report(Y_test, Y_pred_knn)
    print(knn_cr)
    print(Border)

    print("Classification report of Logistic Regression :")
    lr_cr = classification_report(Y_test, Y_pred_lr)
    print(lr_cr)
    print(Border)
    
    print("Classification report of Random Forest :")
    rf_cr = classification_report(Y_test, Y_pred_rf)
    print(rf_cr)
    print(Border)

    print("ROC_AUC Score of KNN :", roc_auc_score(Y_test, Y_pred_knn))
    print(Border)
    print("ROC_AUC Score of Logistic Regression :", roc_auc_score(Y_test, Y_pred_lr))
    print(Border)
    print("ROC_AUC Score of Random Forest :", roc_auc_score(Y_test, Y_pred_rf))
    print(Border)
    
    #------------------------------------------------------------
    # Step 9 - Plotting confusion matrix and ROC curve
    #------------------------------------------------------------

    print("Confusion Matrix of KNN :")
    ConfusionMatrixDisplay(knn_cm).plot()
    plt.title("KNN Confusion Matrix")
    plt.show()
    print(Border)

    print("Confusion Matrix of Lofistic Regression :")
    ConfusionMatrixDisplay(lr_cm).plot()
    plt.title("Logistic Regression Confusion Matrix")
    plt.show()
    print(Border)

    print("Confusion Matrix of Random Forest :")
    ConfusionMatrixDisplay(rf_cm).plot()
    plt.title("Random Forest Confusion Matrix")
    plt.show()
    print(Border)

    print("ROC Curve of KNN :")
    RocCurveDisplay.from_estimator(model_knn, X_test, Y_test)
    plt.title("ROC Curve - KNN")
    plt.show()
    print(Border)

    print("ROC Curve of Logistic Regression :")
    RocCurveDisplay.from_estimator(model_lr, X_test, Y_test)
    plt.title("ROC Curve - Logistic")
    plt.show()
    print(Border)

    print("ROC Curve of Random Forest :")
    RocCurveDisplay.from_estimator(model_rf, X_test, Y_test)
    plt.title("ROC Curve - Random Forest")
    plt.show()
    print(Border)

    # ------------------------------------------------------------
    # Step 9 - Final Output
    # ------------------------------------------------------------

    Prediction = pd.DataFrame({
        "KNN": Y_pred_knn,
        "Logistic": Y_pred_lr,
        "RandomForest": Y_pred_rf,
        "Actual": Y_test.values
    })

    print(Border)
    print("Predictions:")
    print(Prediction.head())

    print(Border)
    Prediction.to_csv("Bank_Predictions.csv", index=False)
    print("Predictions saved to Bank_Predictions.csv")
    print(Border)

if __name__ == "__main__":
    main() 