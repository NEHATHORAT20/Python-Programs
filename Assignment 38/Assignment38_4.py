#Use value_counts() to analyze the distribution of FinalResult
#Calculate the percentage of Pass and Fail students
#Is the dataset balanced?Justify your answer

import pandas as pd 

def main():

    Data = "student_performance_ml.csv"

    df =  pd.read_csv(Data)

    Border = "-"*50

    print(Border)
    Pass, Fail = df["FinalResult"].value_counts()
    print("Count of Passed Students :", Pass)
    print("Count of Failed Students :", Fail)

    print(Border)
    PassPercentage = (Pass / len(df.FinalResult)) * 100
    print("Percentage of Passed Students :", PassPercentage)

    print(Border)
    FailPercentage = (Fail / len(df.FinalResult)) * 100
    print("Percentage of Failed Students :", FailPercentage)

    print(Border)
    print("Yes, the dataset is balanced. It contains a 60/40 split , \nwhere 60% of students are passed & 40% of students are failed , \nwhich is an acceptable ratio for a balanced dataset.")

    print(Border)

if __name__ == "__main__":
    main()