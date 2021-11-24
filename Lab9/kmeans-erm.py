import sys
import numpy as np
import pandas as pd
from math import sqrt
from pyspark.sql import SQLContext 
from pyspark import SparkContext
from pyspark.mllib.clustering import KMeans

S3_DATA_SOURCE_PATH="s3://cs351-lab2/inputfile.txt"
s3_DATA_OUTPUT_PATH="s3://cs351-lab2/output1"
if __name__ == "__main__":
    spark = SparkContext(appName="KMeansExample")
    # sc =SparkContext()
    sqlContext = SQLContext(spark)
    data = spark.textFile(S3_DATA_SOURCE_PATH)
    dataset = data.map(lambda line: np.array([x for x in line.split(', ')])[np.array([0,2,11])].astype(float))
    
    
    
    # Build the model (cluster the data)
    clusters = KMeans.train(dataset, 2, maxIterations=20, initializationMode="random")
    cluster_center=np.array(clusters.centers)
    print("Centers:",clusters.centers,file=sys.stdout)
    
    pdDF = pd.DataFrame(cluster_center)
    spDF = sqlContext.createDataFrame(data = pdDF)

    spDF.rdd.saveAsTextFile(s3_DATA_OUTPUT_PATH)
    
    def cost(point):
        center = clusters.centers[clusters.predict(point)]
        return sqrt(sum([x**2 for x in (point - center)]))

    WSSSE = dataset.map(lambda point: cost(point)).reduce(lambda x, y: x + y)
    print("Within Set Sum of Squared error = " + str(WSSSE),file=sys.stdout)
    

    spark.stop()