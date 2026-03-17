import numpy as np

def ScaledVal(val):

    # Given
    mean_X = 9
    standard_deviation = 2

    return (val - mean_X) / standard_deviation

def main():

    X = np.array([6, 7, 8, 9, 10, 11, 12])

    array = [6, 9, 12]

    for val in array:
        Scaled_Val = ScaledVal(val)
        print(f"Scaled val for {val} : ", Scaled_Val)

if __name__ == "__main__":
    main()