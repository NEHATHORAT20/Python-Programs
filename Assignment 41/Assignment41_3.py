import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def main():
    
    Dataset = [
                {'Study Hours' : 2, 'Attendance' : 60, 'Result' : 'Fail'},
                {'Study Hours' : 5, 'Attendance' : 80, 'Result' : 'Pass'},
                {'Study Hours' : 6, 'Attendance' : 85, 'Result' : 'Pass'},
                {'Study Hours' : 1, 'Attendance' : 50, 'Result' : 'Fail'}
              ]

    Study_Hours = int(input("Enter Study Hours : "))
    Attendance = int(input("Enter Attendance : "))

    df = pd.DataFrame(Dataset)
    X = df[['Study Hours', 'Attendance']]
    Y = df['Result']

    model = KNeighborsClassifier(n_neighbors = 3)

    model.fit(X , Y)

    new_data = pd.DataFrame([[Study_Hours,Attendance]], columns=['Study Hours','Attendance'])

    Y_pred = model.predict(new_data)

    print("Predicted Result : " , Y_pred[0])

if __name__ == "__main__":
    main()