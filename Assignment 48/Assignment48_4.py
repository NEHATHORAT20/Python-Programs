from sklearn.preprocessing import StandardScaler
import math

def main():
    
    X = [
            [25, 20000],
            [30, 40000],
            [35, 80000]
        ]
    
    EucDistance = math.sqrt(((X[1][0] - X[0][0]) ** 2) + ((X[1][1] - X[0][1]) ** 2))
    print("EUC Distance before scaling : " , EucDistance)
    
    scaler = StandardScaler()
        
    X_scaled = scaler.fit_transform(X)

    EucDistance = math.sqrt(((X_scaled[1][0] - X_scaled[0][0]) ** 2) + ((X_scaled[1][1] - X_scaled[0][1]) ** 2))
    print("EUC Distance after scaling : " , EucDistance)

    Explanation = """
    Before scaling the second feature(salary values) dominates the distance calculation because 
    its value are much larger than the first feature.
    After scaling , both features are normalised so they contribute equally to distance calculation.
    """

    print(Explanation)

if __name__ == "__main__":
    main()