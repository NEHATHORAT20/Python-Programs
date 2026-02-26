#Create a plot showing relatiionship between AssignmentsCompleted and FinalResults
#Explain your observation

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():

    Border = "-"*100

    Data = "student_performance_ml.csv"

    df = pd.read_csv(Data)

    #plt.scatter(df["AssignmentsCompleted"], df["FinalResult"])

    plt.grid(True , color = "black")
    sns.scatterplot(x = "AssignmentsCompleted" , y = "FinalResult" , data = df , color = "red")
    plt.title("Relationship between Assignments Completed & FinalResult")
    
    plt.show()

    print(Border)
    print("The scatter plot shows the relationship between AssignmentsCompleted and FinalResult."
        "\nStudents who completed fewer assignments i.e 3 to 4 mostly failed."
        "\nStudents who completed more than 5 assignments mostly passed."
        "\nHence, completing more assignments increases the probability of passing.")
    print(Border)

if __name__ == "__main__":
    main()