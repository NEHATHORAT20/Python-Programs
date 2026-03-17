import numpy as np

def main():

    X = np.array([5, 7, 9, 11, 13])

    # Calculate the mean 
    mean_X = sum(X) / len(X)
    print("Mean of X is :", mean_X)

    # Calculate deviation of each value
    deviation_of_each_val = [float(val - mean_X) for val in X]
    print("Deviation of each value :", deviation_of_each_val)
    
    # Square of each deviation
    square_list = [val * val for val in deviation_of_each_val]
    print("Square of each deviation :", square_list)

    # Calculate Variance
    variance = sum(square_list) / len(square_list)
    print("Variance of the dataset :", variance)

    #Calculate Standard Deviation
    std_dev = np.sqrt(variance)
    print("Standard deviation :", std_dev)

if __name__ == "__main__":
    main()
