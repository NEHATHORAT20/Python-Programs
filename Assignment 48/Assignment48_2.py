import numpy as np
import math

def main():
    X = [6, 7, 8, 9, 10, 11, 12]

    mean_x = np.mean(X)

    numerator = 0
    denominator = len(X)

    for x in X:
        numerator = numerator + ((x - mean_x) ** 2)

    Variance = numerator / denominator

    print("Value of Variance :", Variance)

    std = math.sqrt(Variance)

    print("Value of Standard Deviation :", std)

if __name__ == "__main__":
    main()