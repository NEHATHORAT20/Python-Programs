# Using the same dataset from the previous question, calculate model performance.

# Tasks
# 1. Predict all Y values using the regression equation.
# 2. Calculate:
#    • Mean Squared Error (MSE)
#    • R² Score
# Show all intermediate calculations.

def mean(Value):

    Sum = 0
    n = len(Value) 

    for i in Value:
        Sum = Sum + i

    return Sum / n

def main():

    Border = "-"*50
    print(Border)

    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]

    mean_x = mean(X)

    mean_y = mean(Y)

    n = len(X)

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + (X[i] - mean_x) * (Y[i] - mean_y)
        denominator = denominator + ((X[i] - mean_x) ** 2)

    m = numerator / denominator

    C = mean_y - (m * mean_x)

    print("Predicted Y value for X : ")
    for i in X:
        print(f"Predicted Y for X = {i} : " , m*i + C)

    print(Border)

    SSE = 0
    for i in range(n):
        Y_Predicted = m * X[i] + C
        SSE = SSE + ((Y[i] - Y_Predicted) ** 2)

    MSE = SSE / n

    print("Mean Square Error (MSE) : " , MSE)

    print(Border)

    SS_res = 0
    SS_tot = 0
    
    for i in range(n):
        Y_Predicted = (m * X[i] + C)
        SS_res = SS_res + (Y[i] - Y_Predicted) ** 2
        SS_tot = SS_tot + (Y[i] - mean_y) ** 2

    R_Square = 1- (SS_res / SS_tot)

    print("R_Square Score : " , R_Square)

    print(Border)

if __name__ == "__main__":
    main()