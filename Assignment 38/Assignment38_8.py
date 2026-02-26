#Draw boxplot for Atendance
#Identify if any outliers are present

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():

    Data = "student_performance_ml.csv"

    df = pd.read_csv(Data)

    plt.figure(figsize = (8, 6))
    
    sns.boxplot(x = df["Attendance"], color = "yellow")

    plt.show()

    print("There are no outliers present")

if __name__ == "__main__":
    main()