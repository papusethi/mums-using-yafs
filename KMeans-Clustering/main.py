"""
    This file contains the code for clustering algorithm using K-means algorithm.
    Author: Papu Sethi
    Date: 16 Jan 2022
"""

import matplotlib.pyplot as mtp
import pandas as pd
from sklearn.cluster import KMeans

dataset = pd.read_csv('wireless_devices.csv')

x = dataset.iloc[:, [1, 2]].values

cluster_number = int(input("[+] Enter the number of clusters: "))

kmeans = KMeans(n_clusters=cluster_number, init='k-means++', random_state=42)
y_predict = kmeans.fit_predict(x)

dataset['CLUSTER_ID'] = y_predict
dataset.to_csv('wireless_devices_clustered.csv', index=False)

mtp.scatter(x[y_predict == 0, 0], x[y_predict == 0, 1], s=100, c='brown', label='Cluster 1')
mtp.scatter(x[y_predict == 1, 0], x[y_predict == 1, 1], s=100, c='blue', label='Cluster 2')
mtp.scatter(x[y_predict == 2, 0], x[y_predict == 2, 1], s=100, c='green', label='Cluster 3')

mtp.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow',
            label='Cell Towers')

mtp.title('Clusters of Wireless Devices')
mtp.xlabel('Wireless Device in X-axis')
mtp.ylabel('Wireless Device in Y-axis')
mtp.legend()
mtp.show()
