# Consider the following task:

# 1. Train a Linear Regression model.
# 2. Predict salary for 6 years of experience.
# 3. Plot the regression line using matplotlib.

# Dataset
# Experience | Salary
#          1 | 20000
#          2 | 25000
#          3 | 30000
#          4 | 35000
#          5 | 40000

# Expected Output
# Predicted Salary for 6 Years Experience : ₹45000

# Graph should display:
# • Data points
# • Regression line

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def main():

    X = [[1], [2], [3], [4], [5]]
    Y = [20000, 25000, 30000, 35000, 40000]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model = LinearRegression()

    model.fit(X_train, Y_train)

    Y_Pred = model.predict([[6]])

    print("-"*50)
    print(f"Predicted Salary for 6 Years Experience : ₹{Y_Pred[0]}")
    print("-"*50)
    
    n = len(X)

    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + (X[i] - mean_x) * (Y[i] - mean_y)
        denominator = denominator + ((X[i] - mean_x) ** 2)

    m = numerator / denominator

    C = mean_y - (m * mean_x)

    x = np.linspace(1, 6, n)
    y = C + m * x

    plt.plot(x, y, color = "black", label = "Regression Line")

    plt.scatter(X, Y, color = 'Red', label = "Data Points")

    plt.xlabel("Experience (Years)")
    plt.ylabel("Salary")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()