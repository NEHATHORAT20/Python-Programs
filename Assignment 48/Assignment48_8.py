from sklearn.metrics import confusion_matrix

def main():
    actual =    [1, 1, 1, 1, 0, 0, 0, 0]
    predicted = [1, 1, 0, 1, 0, 1, 0, 0]

    cm = confusion_matrix(actual, predicted)

    TN = cm[0][0]
    FP = cm[0][1]
    FN = cm[1][0]
    TP = cm[1][1]

    #TN , FP , FN , TP = cm.ravel()

    print("True Positive : " , TP)
    print("True Negative : " , TN)
    print("False Positive : " , FP)
    print("False Negative : " , FN)
                
if __name__ == "__main__":
    main()