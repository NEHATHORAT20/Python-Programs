#Write a python program to load the file student_performnace_ml.csv using pandas.
#Display:
#. First 5 records
#. Last 5 records
#. Total number of rows and columns
#. List of Column names
#. Data types of each column

import pandas as pd

def main():

    Data = "student_performance_ml.csv"

    df = pd.read_csv(Data)

    Border = "-"*100

    print(Border) 
    print("First 5 Records : ") 
    print(Border+"\n")  
    print(df.head())

    print(Border) 
    print("Last 5 Records : ")
    print(Border+"\n")  
    print(df.tail())

    print(Border) 
    print("Total number of rows and columns : " , df.shape) 
    print(Border+"\n") 

    print(Border) 
    print("List of column names : ")  
    print(list(df.columns))
    print(Border+"\n")

    print(Border) 
    print("Data types of each column : ") 
    print(Border+"\n") 
    print(df.dtypes)

if __name__ == "__main__":
    main()