import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import Birch, KMeans, AgglomerativeClustering
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import silhouette_score

from icecream import ic

class Clustering_algos():

    def __init__(self, img, algo, n_colors) -> None:
        self.img = img
        self.algo = algo
        self.n_colors = n_colors

         # Image read
        data = np.asarray(img, dtype="int32")
        # converting labels to represent rgb colors from 0-255
        self.points = data.reshape(data.shape[0]*data.shape[1], 3)/255.0 

    def get_palette_plot(self):
        ic(self.points.shape)
        self.algo = self.algo.lower()
        labels = ''
        ic(self.algo)
        if (self.algo == 'kmeans'):
            labels = self.kmeans()
        elif (self.algo == 'kmeans_plus'):
            labels = self.kmeans_plus()
        elif (self.algo == 'hac'):
            labels = self.agglomerative()
        elif (self.algo == 'birch'):
            labels = self.birch()
        
        colors = self.create_color_palette_from_labels(labels)
        return colors
    
    def create_color_palette_from_labels(self, labels):
        color_arr = []
        for i in range(self.n_colors):
            color_arr.append(list(np.round((self.points * (labels == i).reshape(-1,1)).sum(axis=0) / sum((labels ==i))*256)))
        return str(color_arr)

    def kmeans(self):
        kmeans_model = KMeans(n_clusters=self.n_colors, n_init=10)
        param_grid = {
            'algorithm': ['full', 'elkan']
            }
        predictors = GridSearchCV(estimator=kmeans_model, param_grid=param_grid, scoring=silhouette_score, cv=None, refit=True)
        best_kmeans_model = predictors.fit(self.points, y=None)
        return best_kmeans_model.predict(self.points)

    def birch(self):
        birch_model = Birch(threshold=0.03, n_clusters=self.n_colors).fit(self.points)
        return birch_model.labels_

    def agglomerative(self):
        agglo_model = AgglomerativeClustering(n_clusters=self.n_colors, linkage='ward', compute_full_tree=False).fit(self.points)
        return agglo_model.labels_

    def kmeans_plus(self):
        kmeans_plus_model = KMeans(n_clusters=self.n_colors,  init='k-means++', n_init=10).fit(self.points)
        return kmeans_plus_model.labels_



