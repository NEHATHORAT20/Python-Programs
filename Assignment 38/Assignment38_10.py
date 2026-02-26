#Plot SleepHours against FinalResult
#Does sleeping more gurantee success?Explain

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():

    Border = "-"*100

    Data = "student_performance_ml.csv"

    df = pd.read_csv(Data)

    plt.grid(True , color = "black")
    sns.scatterplot(x = "SleepHours" , y = "FinalResult" , data = df , color = "green")
    plt.title("Sleep Hours VS Final Result")
    plt.grid(True)

    plt.show()

    print(Border)
    print("Students who sleep for 7 to 8 hours mostly passed."
        "\nStudents with lower sleep hours are more likely to fail."
        "\nTho sleeping more does not guarantee success, but proper sleep may improve performance.")
    print(Border)

if __name__ == "__main__":
    main()