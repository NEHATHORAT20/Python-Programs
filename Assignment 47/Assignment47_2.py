import pandas as pd
import numpy as np

def main():
    X = np.array([4, 6, 8, 10, 12])

    # Calculation of mean
    total = 0
    for value in X:
        total = total + value

    mean_X = total / len(X)
    print("Mean of X is :", mean_X)

    # Calculation of deviation
    deviation = []
    for value in X:
        deviation_of_val = (value - mean_X)
        print(f"Deviation of {value} :", deviation_of_val)
        deviation.append(float(deviation_of_val))

    # Calculating square of each deviation
    Square_of_deviation = [value*value for value in deviation]
    print("Square of each deviation val :", Square_of_deviation)

    # Calculating the variance of dataset
    total = 0
    for value in Square_of_deviation:
        total = total + value

    variance = total / len(Square_of_deviation)
    print("Variance of the dataset :", variance)

if __name__ == "__main__":
    main()