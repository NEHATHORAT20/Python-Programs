import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
from sklearn.model_selection import train_test_split

def CheckAccuracy(Y_test, Y_pred):

    Y_Test = Y_test.values
    Right = 0
    total = len(Y_Test)

    for i in range(total):
        if Y_Test[i] == Y_pred[i]:
            Right = Right + 1

    Accurate = Right / total
    return Accurate

def PlayPredictor(FilePath):

    Border = "-"*40

    #---------------------------------------------------
    # Step 1 - Load Dataset
    #---------------------------------------------------
    print(Border)
    print("Step 1 - Load Dataset")
    print(Border)

    df = pd.read_csv(FilePath)

    print("Some Records from dataset : ")
    print(df.head())

    #---------------------------------------------------
    # Step 2 - Remove Unwanted Columns
    #---------------------------------------------------
    print(Border)
    print("Step 2 - Remove Unwanted Columns")
    print(Border)

    print("Shpae of dataset before Removal : " , df.shape)

    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'], inplace=True)

    print("Shape of dataset after Removal : " , df.shape)

    print(Border)
    print("Clean dataset is : ")
    print(Border)

    print(df.head())

    #---------------------------------------------------
    # Step 3 - Checking Missing Values
    #---------------------------------------------------
    print(Border)
    print("Step 3 - Checking Missing Values")
    print(Border)

    print("Count of Missing Values : ")
    print(df.isnull().sum())

    #---------------------------------------------------
    # Step 4 - Display Statistical Summary
    #---------------------------------------------------
    print(Border)
    print("Step 4 - Display Statistical Summary")
    print(Border)

    print(df.describe())

    #---------------------------------------------------
    # Step 5 - Encoding of features and labels
    #---------------------------------------------------
    print(Border)
    print("Step 5 - Encoding of features and labels")
    print(Border)

    Features = OrdinalEncoder()
    df[['Weather', 'Temperature']] = Features.fit_transform(df[['Weather', 'Temperature']])

    Labels = LabelEncoder()
    df['Play'] = Labels.fit_transform(df['Play'])

    print("Few records after encoding : ")
    print(df.head())

    #---------------------------------------------------
    # Step 6 - Split the dataset into independent and dependent variables
    #---------------------------------------------------
    print(Border)
    print("Step 6 - Split the dataset into independent and dependent variables")
    print(Border)

    X = df[['Weather', 'Temperature']]
    Y = df['Play']

    print("Shape of Independent variables : " , X.shape)
    print("Shape of dependent variables : " , Y.shape)

    #---------------------------------------------------
    # Step 7 - Split the data into training and testing
    #---------------------------------------------------
    print(Border)
    print("Step 7 - Split the data into training and testing")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    print("X_train shape : " , X_train.shape)
    print("X_test shape : " , X_test.shape)
    print("Y_train shape : " , Y_train.shape)
    print("Y_test shape : " , Y_test.shape)

    #---------------------------------------------------
    # Step 8 - Create and train the model
    #---------------------------------------------------
    print(Border)
    print("Step 8 - Create and train the model")
    print(Border)

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X_train, Y_train)

    #-----------------------------------------------------------------
    # Step 9 - Test the model
    #-----------------------------------------------------------------
    print(Border)
    print("Step 9 - Test the model")
    print(Border)

    Y_pred = model.predict(X_test)

    #-----------------------------------------------------------------
    # Step 10 - Compare the actual and predicted values
    #-----------------------------------------------------------------
    print(Border)
    print("Step 10 - Comapre actual and predicted values")
    print(Border)

    Result = pd.DataFrame({'Actual play' : Y_test.values,
                           'Predicted play' : Y_pred
                         })
    
    print(Result.head())

    #-----------------------------------------------------------------
    # Step 11 - Evaluate the model
    #-----------------------------------------------------------------
    print(Border)
    print("Step 11 - Evaluate the model")
    print(Border)

    Accuracy = CheckAccuracy(Y_test, Y_pred)

    print("Accuracy of the model for n = 3 is : ")
    print("Accuracy of the model :", Accuracy * 100 , "%")

    #-----------------------------------------------------------------
    # Step 12 - Evaluation of the model for K = 5
    #-----------------------------------------------------------------
    print(Border)
    print("Step 12 - Evaluation of the model for K = 5")
    print(Border)

    print("Accuracy of model for n = 5 is :")

    model = KNeighborsClassifier(n_neighbors=5)

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    Accuracy = CheckAccuracy(Y_test, Y_pred)

    print("Accuracy of the model :", Accuracy * 100 , "%")

    print(Border)

def main():
    
    PlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()