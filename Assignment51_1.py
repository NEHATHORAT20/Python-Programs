import pandas as pd 
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import VotingClassifier

def main():

    Border = "-" * 100

    #------------------------------------------------------
    # Step 1 - Load Dataset
    #------------------------------------------------------

    true_data = pd.read_csv("True.csv")
    fake_data = pd.read_csv("Fake.csv")

    print(Border)
    print("Dataset entries before adding labels:")
    print(true_data.head())

    print(Border)
    true_data['label'] = 1
    print("After adding label (Real = 1):")
    print(true_data.head())

    print(Border)
    print("Dataset entries before adding labels:")
    print(fake_data.head())

    print(Border)
    fake_data['label'] = 0
    print("After adding label (Fake = 0):")
    print(fake_data.head())

    df = pd.concat([true_data, fake_data], axis=0)

    df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    print(Border)
    print("Dataset after concatenation : ")
    print(df.head())

    #------------------------------------------------------
    # Step 2 - Preprocessing 
    #------------------------------------------------------

    print(Border)
    print("Shape of the dataset : ")
    print(df.shape)

    print(Border)
    print("Columns in the dataset : ")
    print(list(df.columns))

    print(Border)
    print("Missing values count in the dataset :")
    print(df.isnull().sum())

    df = df.dropna()

    X = df['title'] + " " + df['text']
    Y = df['label']

    # ------------------------------------------------------
    # Step 3 - Train-Test Split
    # ------------------------------------------------------

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42
    )

    # ------------------------------------------------------
    # Step 4 - TF-IDF Vectorization 
    # ------------------------------------------------------

    vectorizer = TfidfVectorizer(stop_words='english')

    X_train = vectorizer.fit_transform(X_train)
    X_test = vectorizer.transform(X_test)

    #------------------------------------------------------
    # Step 5 - Model Training
    #------------------------------------------------------

    lr_model = LogisticRegression(max_iter=1000)
    dt_model = DecisionTreeClassifier(random_state=42)

    lr_model.fit(X_train, Y_train)
    dt_model.fit(X_train, Y_train)

    Y_pred_lr = lr_model.predict(X_test)
    Y_pred_dt = dt_model.predict(X_test)

    # ------------------------------------------------------
    # Step 6 - Voting Classifier
    # ------------------------------------------------------

    hard_model = VotingClassifier(
        estimators=[('lr', lr_model), ('dt', dt_model)],
        voting='hard'
    )

    hard_model.fit(X_train, Y_train)
    Y_pred_hard = hard_model.predict(X_test)

    soft_model = VotingClassifier(
        estimators=[('lr', lr_model), ('dt', dt_model)],
        voting='soft'
    )

    soft_model.fit(X_train, Y_train)
    Y_pred_soft = soft_model.predict(X_test)

    #------------------------------------------------------
    # Step 5 - Evaluation of models
    #------------------------------------------------------

    acc_lr = accuracy_score(Y_test, Y_pred_hard)
    acc_dt = accuracy_score(Y_test, Y_pred_soft)
    acc_hard = accuracy_score(Y_test, Y_pred_hard)
    acc_soft = accuracy_score(Y_test, Y_pred_soft)

    print(Border)
    print("Accuracy of the Logistic Regression : " , acc_lr*100)
    print("Accuracy of the Decision Tree : " , acc_dt*100)
    print("Accuracy of the Hard Voting : " , acc_hard*100)
    print("Accuracy of the Soft Voting : " , acc_soft*100)

    print(Border)
    print(f"Comparison → Accuracy of Hard Voting: {acc_hard:.4f} | Soft Voting: {acc_soft:.4f}")

    cm_lr = confusion_matrix(Y_test, Y_pred_hard)
    cm_dt = confusion_matrix(Y_test, Y_pred_hard)
    cm_hard = confusion_matrix(Y_test, Y_pred_hard)
    cm_soft = confusion_matrix(Y_test, Y_pred_soft)

    print(Border)
    print("Confusion matrix of Logistic Regression : \n" , cm_lr) 
    print("Confusion matrix of Decision Tree : \n" , cm_dt) 
    print("Confusion matrix of Hard Voting : \n" , cm_hard) 
    print("Confusion matrix of Soft Voting : \n" , cm_soft)
    print(Border)

if __name__ == "__main__":
    main()