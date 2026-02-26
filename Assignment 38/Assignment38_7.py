#Create a scatter plot of:
#StudyHours vs PreviousScore
#Use different colors to Pass and Fail students

import pandas as pd
import matplotlib.pyplot as plt

def main():

    Data = "student_performance_ml.csv"

    df = pd.read_csv(Data)

    colors = df["FinalResult"].map({1 : "red" , 0 : "blue"})

    plt.scatter(df["StudyHours"], df["PreviousScore"] , c = colors)

    #for fn in df["FinalResult"].unique():
        #temp = df[df["FinalResult"] == fn]
        #plt.scatter(temp["StudyHours"], temp["PreviousScore"], label = fn)

    plt.xlabel("Study Hours")
    plt.ylabel("Previous Score")
    plt.title("Study Hours vs Previous Score")
    #plt.legend()
    plt.grid(True)

    plt.show()

if __name__ == "__main__":
    main()