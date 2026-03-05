import math

def EuclideanDistance(P1, P2):

    Ans = math.sqrt((P1["X"] - P2["X"]) ** 2 + (P1["Y"] - P2["Y"]) ** 2)
    return Ans

def KNeighborsClassifier():

    Border = "-"*50

    Dataset = [
                {"point" : "A", "X" : 1, "Y" : 2, "label" : "Red"},
                {"point" : "B", "X" : 2, "Y" : 3, "label" : "Red"},
                {"point" : "C", "X" : 3, "Y" : 1, "label" : "Blue"},
                {"point" : "D", "X" : 6, "Y" : 5, "label" : "Blue"}
              ]

    x_cordinate = int(input("Enter X coordinate : "))
    y_cordinate = int(input("Enter Y coordinate : "))

    new_point = {"X" : x_cordinate , "Y" : y_cordinate}

    for d in Dataset:
        d["distance"] = EuclideanDistance(d, new_point)

    sorted_data = sorted(Dataset, key = lambda item : item['distance'])

    K = 3
    nearest = sorted_data[:K]

    print(Border)
    print("Nearest Neighbours :")
    
    for d in nearest:
        print(f"{d['point']} - Distance : ", d['distance'])

    Votes = {}
    
    for neighbour in nearest:
        label = neighbour['label']
        Votes[label] = Votes.get(label, 0) + 1

    predicted_class = max(Votes, key = Votes.get)

    print(Border)
    print("Predicted class : " , predicted_class)
    print(Border)

def main():

    KNeighborsClassifier()
    
if __name__ == "__main__":
    main()