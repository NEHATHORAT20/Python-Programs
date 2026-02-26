#Using pandas functions, calculate and display:
#. Average StudyHours
#. Average Attendance
#. Maximum PreviousScore
#. Minimum SleepHours

import pandas as pd

def main():

    Data = "student_performance_ml.csv"

    df = pd.read_csv(Data)

    Border = "-"*50

    print(Border)
    print("Average of Study Hours :", df["StudyHours"].mean())

    print(Border)
    print("Average of Attendance :", df["Attendance"].mean())

    print(Border)
    print("Maximum Previous Score :", df["PreviousScore"].max())

    print(Border)
    print("Minimum Sleep Hours :", df["SleepHours"].min())

    print(Border)

if __name__ == "__main__":
    main()