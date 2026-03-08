import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def Advertise(DataPath):

    Border = "-"*40
    #-----------------------------------------------------------------
    # Step 1 - Load Dataset
    #-----------------------------------------------------------------
    print(Border)
    print("Step 1 - Load Dataset")
    print(Border)
    df = pd.read_csv(DataPath)

    print("Some records from dataset : ")
    print(df.head())

    #-----------------------------------------------------------------
    # Step 2 - Remove Unwanted Columns
    #-----------------------------------------------------------------
    print(Border)
    print("Step 2 - Remove Unwanted Columns")
    print(Border)

    print("Shape of dataset before removal : " , df.shape)

    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'], inplace=True)

    print("Shape of dataset after removal : " , df.shape)

    print(Border)
    print("Clean dataset is : ")
    print(Border)

    print(df.head())

    #-----------------------------------------------------------------
    # Step 3 - Check missing values
    #-----------------------------------------------------------------
    print(Border)
    print("Step 3 - Check Missing Values")
    print(Border)

    print("Count of Missing Values :\n" , df.isnull().sum())

    #-----------------------------------------------------------------
    # Step 4 - Display Statistical Summary
    #-----------------------------------------------------------------
    print(Border)
    print("Step 4 - Display Statistical Summary")
    print(Border)

    print(df.describe())

    #-----------------------------------------------------------------
    # Step 5 - Correlation between columns
    #-----------------------------------------------------------------
    print(Border)
    print("Step 5 - Correlation between columns")
    print(Border)

    print("Correlation matrix")
    print(df.corr())

    #-----------------------------------------------------------------
    # Step 6 - Split dataset into independent and dependent variables
    #-----------------------------------------------------------------
    print(Border)
    print("Step 6 - Split dataset into independent and dependent variables")
    print(Border)

    X = df[['TV', 'radio', 'newspaper']]
    Y = df['sales']

    print("Shape of independent variables : " , X.shape)
    print("Shape of dependent variables : " , Y.shape)

    #-----------------------------------------------------------------
    # Step 7 - Split the dataset for training and testing
    #-----------------------------------------------------------------
    print(Border)
    print("Step 7 - Split the dataset for training and testing")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    print("X_train shape : " , X_train.shape)
    print("X_test shape : " , X_test.shape)
    print("Y_train shape : " , Y_train.shape)
    print("Y_test shape : " ,  Y_test.shape)

    #-----------------------------------------------------------------
    # Step 8 - Create & train the model
    #-----------------------------------------------------------------
    print(Border)
    print("Step 8 - Create & train the model")
    print(Border)

    model = LinearRegression()

    model.fit(X_train, Y_train)

    #-----------------------------------------------------------------
    # Step 9 - Test the model
    #-----------------------------------------------------------------
    print(Border)
    print("Step 9 - Test the model")
    print(Border)

    Y_pred = model.predict(X_test)

    #-----------------------------------------------------------------
    # Step 10 - Evaluate the model
    #-----------------------------------------------------------------
    print(Border)
    print("Step 10 - Evaluate the model")
    print(Border)

    MSE = mean_squared_error(Y_test, Y_pred)
    RMSE = np.sqrt(MSE)
    R2 = r2_score(Y_test, Y_pred)

    print("Mean Squared Error :", MSE)
    print("Root Mean Squared Error :", RMSE)
    print("R Sqaure Error :", R2)

    #-----------------------------------------------------------------
    # Step 11 - Calculate model coefficient
    #-----------------------------------------------------------------
    print(Border)
    print("Step 11 - Calculate model coefficient")
    print(Border)

    for column, value in zip(X.columns, model.coef_):
        print(f"{column} : {value}")

    print("Intercept :", model.intercept_)

    #-----------------------------------------------------------------
    # Step 12 - Compare the actual and predicted values
    #-----------------------------------------------------------------
    print(Border)
    print("Step 12 - Comapre actual and predicted values")
    print(Border)

    Result = pd.DataFrame({'Actual Sales' : Y_test.values,
                           'Predicted Sales' : Y_pred
                         })
    
    print(Result.head())

    #-----------------------------------------------------------------
    # Step 13 - Plot Actual vs Predicted
    #-----------------------------------------------------------------
    print(Border)
    print("Step 13 - Plot Actual vs Predicted")
    print(Border)

    plt.figure(figsize=(8, 5))
    plt.scatter(Y_test, Y_pred , color='red')
    plt.xlabel("Actual Sales")
    plt.ylabel("Predicted Sales")
    plt.title("Actual Sales vs Predicted Sales")
    plt.grid(True)
    plt.show()

def main():
    
    Advertise("Advertising.csv")

if __name__ == "__main__":
    main()