import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN, KMeans

from icecream import ic

def get_palette_plot(img, algo, n_colors):
    # Image read
    data = np.asarray(img, dtype="int32")

    points = data.reshape(data.shape[0]*data.shape[1], 3)/255.0 # converting labels to represent rgb colors from 0-255

    kmeans = KMeans(n_clusters=n_colors).fit(points)
    color_arr = []
    # color palette with plt.Circle
    for i in range(n_colors):
        color_arr.append(list((points * (kmeans.labels_==i).reshape(-1,1)).sum(axis=0) / sum((kmeans.labels_==i))*256))
  
    return str(color_arr)
