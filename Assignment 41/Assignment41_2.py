import math 

def EucDistance(P1, P2):
    Ans = math.sqrt((P1['X'] - P2['X']) ** 2 + (P1['Y'] - P2['Y']) ** 2)
    return Ans

def Predicted_Class(nearest):

    Votes = {}

    for neighbour in nearest:
        label = neighbour['label']
        Votes[label] = Votes.get(label, 0) + 1

    predicted_class = max(Votes, key = Votes.get)

    return predicted_class

def KNeighboursClassifier():

    Border = "-"*50

    Dataset = [
                {"point" : "A", "X" : 1, "Y" : 2, "label" : "Red"},
                {"point" : "B", "X" : 2, "Y" : 3, "label" : "Red"},
                {"point" : "C", "X" : 3, "Y" : 1, "label" : "Blue"},
                {"point" : "D", "X" : 6, "Y" : 5, "label" : "Blue"}
              ]

    x_cordinate = int(input("Enter X coordinate : "))
    y_cordinate = int(input("Enter y coordinate : "))

    new_point = {"X" : x_cordinate, "Y" : y_cordinate}

    for d in Dataset:
        d['distance'] = EucDistance(d, new_point)

    sorted_data = sorted(Dataset, key = lambda item : item['distance'])

    K = 1
    nearest_1 = sorted_data[:K]

    K = 3
    nearest_3 = sorted_data[:K]

    K = 5
    nearest_5 = sorted_data[:K]

    print(Border)
    print("Predicted results ")

    Value1 = Predicted_Class(nearest_1)
    print("K = 1 -> ", Value1)

    Value2 = Predicted_Class(nearest_3)
    print("K = 3 -> ", Value2)

    Value3 = Predicted_Class(nearest_5)
    print("K = 5 -> ", Value3)

    print(Border)
    Explanation = """
    
    The value of K determines how many nearest neighbors are used for classification.
    When the value of k increases, more nearest neighbors are considered for voting.

    K = 1  -> Only closest neighbor decides the class.
    K = 3  -> 3 nearest neighbors vote & majority class is selected.
    K = 5  -> More neighbors influence the decision.

    As K increases, more data points participate in voting,
    so the predicted class may change.
    """
    
    print(Explanation)

    print(Border)

def main():

    KNeighboursClassifier() 

if __name__ == "__main__":
    main()