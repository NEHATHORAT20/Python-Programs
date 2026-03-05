# Implement Simple Linear Regression manually without using any ML library.

# Dataset
# X = [1, 2, 3, 4, 5]
# Y = [3, 4, 2, 4, 5]

# Tasks
# Calculate the following:
# 1. Mean of X (X̄)
# 2. Mean of Y (Ȳ)
# 3. Slope (m)
# 4. Intercept (c)

# Expected Output Example
# Mean of X = 3
# Mean of Y = 3.6
# Slope (m) = 0.4
# Intercept (c) = 2.4

# Regression Equation:
# Y = 0.4X + 2.4

# Predicted Y for X = 6 : 4.8

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
    print("Mean of X :", mean_x)

    print(Border)
    mean_y = mean(Y)
    print("Mean of Y :", mean_y)

    n = len(X)

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + (X[i] - mean_x) * (Y[i] - mean_y)
        denominator = denominator + ((X[i] - mean_x) ** 2)

    m = numerator / denominator

    print(Border)
    print("Slope (m) : " , m)

    print(Border)
    C = mean_y - (m * mean_x)
    print("Y - intercept (C) : " , C)

    print(Border)
    print("Regression equation : " , f"Y = {m}X + {C}")

    print(Border)
    Y_pred = m*6 + C
    print("Predicted Y for X = 6 : " , Y_pred)

if __name__ == "__main__":
    main()