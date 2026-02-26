#Write a program to:
#. Display total number of students in the dataset
#. Count how many students Passed(FinalResult = 1)
#. Count how many students Failed(FinalResult = 0)

import pandas as pd

def main():

    Data = "student_performance_ml.csv"

    df = pd.read_csv(Data)

    Border = "-"*50

    print(Border)
    print("Total number of students :", len(df.FinalResult))

    print(Border)
    print("Total number of students passed :", (df["FinalResult"] == 1).sum())

    print(Border)
    #StudentsFailed = 0
    #for i in range(len(df.FinalResult)):
        #if df.FinalResult[i] == 0:
            #StudentsFailed = StudentsFailed + 1

    print("Total number of students failed :", (df["FinalResult"] == 0).sum())
    print(Border)

if __name__ == "__main__":
    main()