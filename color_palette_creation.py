import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN, KMeans
import io

from icecream import ic

def get_palette_plot(img):
    # Image read
    data = np.asarray(img, dtype="int32")
    ic(data.shape)

    points = data.reshape(data.shape[0]*data.shape[1], 3)/255.0 # converting labels to represent rgb colors from 0-255

    kmeans = KMeans(n_clusters=6).fit(points)

    fig, ax = plt.subplots(1,2, figsize=(12,12))
    ax[0].imshow(img)

    # # # No ticks (no axis labels) for the image
    ax[0].set_xticks([])
    ax[0].set_yticks([])

    # color palette with plt.Circle
    for i in range(6):
        circle = plt.Circle((0, (i+1.4)/8), 0.05, color=(points * (kmeans.labels_==i).reshape(-1,1)).sum(axis=0) / sum((kmeans.labels_==i)))
        ax[1].add_artist(circle)

    # make xy scale equal & axis off for the color circles
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')

    plt.tight_layout()

    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image