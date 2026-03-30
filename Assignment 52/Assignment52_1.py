import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def main():

    Border = "-" * 100

    # ----------------------------------------------------------
    # Step 1 - Load Dataset
    # ----------------------------------------------------------

    df = pd.read_csv("student-mat.csv", sep=";")

    print(Border)
    print("First 5 records : ")
    print(df.head())

    print(Border)
    print("Shape of dataset : " , df.shape)

    print(Border)
    print("Missing values : ")
    print(df.isnull().sum())

    # ----------------------------------------------------------
    # Step 2 - Select Features
    # ----------------------------------------------------------

    X = df[['G1', 'G2', 'G3', 'studytime', 'failures', 'absences']]

    print(Border)
    print("Selected features : ")
    print(X.head())

    print(Border)
    print("Statistical Summary : ")
    print(X.describe())

    # ----------------------------------------------------------
    # Step 3 - Feature Scaling
    # ----------------------------------------------------------

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # ----------------------------------------------------------
    # Step 4 - Apply KMeans Clustering
    # ----------------------------------------------------------

    model = KMeans(n_clusters=3, random_state=42)

    clusters = model.fit_predict(X_scaled)

    df['Cluster'] = clusters

    print(Border)
    print("Cluster : ")
    print(df[['G3', 'studytime', 'failures', 'absences', 'Cluster']].head())

    # ----------------------------------------------------------
    # Step 5 - Cluster Interpretation
    # ----------------------------------------------------------

    print(Border)
    print("Cluster Means:")
    cluster_means = df.groupby('Cluster')[['G3', 'studytime', 'failures', 'absences']].mean()
    print(cluster_means)

    top_cluster = cluster_means['G3'].idxmax()

    low_cluster = cluster_means['G3'].idxmin()

    avg_cluster = list(set([0,1,2]) - set([top_cluster, low_cluster]))[0]

    def assign_label(cluster):
        if cluster == top_cluster:
            return "Top Performer"
        elif cluster == avg_cluster:
            return "Average Student"
        else:
            return "Struggling Student"

    df['Performance'] = df['Cluster'].apply(assign_label)

    print(Border)
    print("Final labeled data : ")
    print(df[['G3', 'studytime', 'failures', 'absences', 'Cluster', 'Performance']].head())

    print(Border)
    print("Performance Count : ")
    print(df['Performance'].value_counts())

    # ----------------------------------------------------------
    # Step 6 - Visualization
    # ----------------------------------------------------------

    plt.figure()
    sns.scatterplot(x=df['G3'], y=df['studytime'], hue=df['Performance'])
    plt.title("Student Performance Clusters")
    plt.xlabel("Final Grade (G3)")
    plt.ylabel("Study Time")
    plt.show()

    # ----------------------------------------------------------
    # Step 7 - Prediction for new student
    # ----------------------------------------------------------

    new_student = pd.DataFrame(
            [[5, 6, 6, 2, 0, 6]],
            columns=['G1', 'G2', 'G3', 'studytime', 'failures', 'absences']
            )

    new_scaled = scaler.transform(new_student)

    pred_cluster = model.predict(new_scaled)[0]

    pred_label = assign_label(pred_cluster)

    print(Border)
    print("New student cluster : " , pred_cluster)
    print("Performance category : " , pred_label)
    print(Border)

if __name__ == "__main__":
    main()