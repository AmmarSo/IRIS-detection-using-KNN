# Libraries
import pandas as pd
import math

# Load the dataset
dataframe = pd.read_csv("data/iris.csv")
distance = {}
iris = []

# Euclidean distance function that skips the first element (the ID)
def euclidean_distance(x, xn):
    dist = 0
    # start at 1 to ignore x[0] which is the ID
    for i in range(1, len(xn)):     
        dist += (x[i] - xn[i])**2
    return math.sqrt(dist)

# New point (first element is its ID)
xn = [151, 5.5, 2.4, 0.2]

# Compute distance from each iris to the new point
for i in range(len(dataframe)):
    id_i = dataframe.loc[i, "Id"]
    d1   = dataframe.loc[i, "SepalLengthCm"]
    d2   = dataframe.loc[i, "SepalWidthCm"]
    d3   = dataframe.loc[i, "PetalLengthCm"]
    d4   = dataframe.loc[i, "PetalWidthCm"]

    iris = [id_i, d1, d2, d3, d4]
    distance_with_xnew = euclidean_distance(iris, xn)
    distance[id_i] = distance_with_xnew
    #print(f"ID {id_i} → Distance = {distance_with_xnew}")


k = 3
# Sort in ascending order
sorted_items = sorted(distance.items(), key=lambda item: item[1])

# We choose the k smallest element 
k_smallest = sorted_items[:k]
print(k_smallest)