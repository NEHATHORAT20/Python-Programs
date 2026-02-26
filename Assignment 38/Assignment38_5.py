#Based on the dataset values , analyze whether:
#. Higher StudyHours increase the chance of passing
#. Higher Attendance improves FinalResult
#Write your observations in 4-5 lines

import pandas as pd

def main():

    Data = "student_performance_ml.csv"

    df = pd.read_csv(Data)

    Border = "-"*100

    print(Border)
    Pass = df[df["FinalResult"] == 1]["StudyHours"].mean()
    print("Average Study Hours of Pass Students : " , Pass)

    Fail = df[df["FinalResult"] == 0]["StudyHours"].mean()
    print("Average Study Hours of Fail Students : " , Fail)

    print(Border)
    Pass_Attendance = df[df["FinalResult"] == 1]["Attendance"].mean()
    print("Average Attendance of Pass Students : " , Pass_Attendance)

    Fail_Attendance = df[df["FinalResult"] == 0]["Attendance"].mean()
    print("Average Attendance of Fail Students : " , Fail_Attendance)

    print(Border)
    if Pass_Attendance > Fail_Attendance:
        print("Higher Attendance improves final result")
    else:
        print("Attendance does not affect final result")

    print(Border)

if __name__ == "__main__":
    main()