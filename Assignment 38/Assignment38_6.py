#Plot the histogram of StudyHours.
#Explain what the distribution tells you.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():

    Border = "-"*100

    Data = "student_performance_ml.csv"

    df = pd.read_csv(Data)

    plt.xlabel("Study Hours")
    plt.ylabel("Number of students")
    plt.title("Analysis of Study Hours")

    sns.histplot(df["StudyHours"])

    plt.show()

    print(Border)
    print("According to the histogram graph most students study between 5 to 8 hours daily." 
          "\nThis indicates that majority of students maintain regular study hours")
    print(Border)


if __name__ == "__main__":
    main()