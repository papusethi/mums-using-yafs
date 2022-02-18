"""
    This file contains the code for choosing the best value K using Elbow method.
    Author: Papu Sethi
    Date: 16 Jan 2022
"""

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as mtp

dataset = pd.read_csv('wireless_devices.csv')
x = dataset.iloc[:, [1, 2]].values

# Initializing the list for the values of WCSS: Within Cluster Sum of Squares
# Using for loop for iterations from 1 to 10
# This finds the best K value
wcss_list = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(x)
    wcss_list.append(kmeans.inertia_)

mtp.plot(range(1, 11), wcss_list)
mtp.title("The Elbow Method Graph")
mtp.xlabel("Number of Clusters(k)")
mtp.ylabel("wcss_list")
mtp.show()
