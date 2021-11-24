import sys
import numpy as np
from math import sqrt

from pyspark import SparkContext
from pyspark.mllib.clustering import KMeans


if __name__ == "__main__":
    sc = SparkContext(appName="KMeansExample")

    data = sc.textFile("file:///mnt/c/Users/ankit/desktop/inputfile.txt")
    
    parsedData = data.map(lambda line: np.array([x for x in line.split(', ')])[np.array([0,2,11])].astype(float))
    
    
    
    clusters = KMeans.train(parsedData, 2, maxIterations=20, initializationMode="random")
    cluster_center=clusters.centers
    
    
    
    def error(point):

        center = clusters.centers[clusters.predict(point)]
        return sqrt(sum([x**2 for x in (point - center)]))

    WSSSE = parsedData.map(lambda point: error(point)).reduce(lambda x, y: x + y)
    
    
    print("Centers:",clusters.centers,"WSSSE=",WSSSE,file=sys.stdout)

    sc.stop()
