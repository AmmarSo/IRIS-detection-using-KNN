# Libraries
import pandas as pd
import math

# Load the dataset and variable initialization
dataframe = pd.read_csv("data/iris.csv")
distance = {}
iris = []
iris_class = {'Iris-setosa':0, 'Iris-versicolor':0, 'Iris-virginica':0 }

# Euclidean distance function that skips the first element (the ID)
def euclidean_distance(x, xn):
    dist = 0
    # start at 1 to ignore x[0] which is the ID
    for i in range(1, len(xn)):     
        dist += (x[i] - xn[i])**2
    return math.sqrt(dist)

# New point (first element is its ID)
xn = [151, 6.0,  2.8,  4.9,  1.7]

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
    print(f"ID {id_i} → Distance = {distance_with_xnew}")


k = 15

# Sort in ascending order
sorted_items = sorted(distance.items(), key=lambda item: item[1])
# We choose the k smallest element 
k_smallest = sorted_items[:k]
#print(k_smallest)

# Retrieve class 
for item in k_smallest:
    id = item[0]
    filtered_df = dataframe[dataframe['Id'] == id]
    y = filtered_df["Species"].to_list()
    if y[0] == "Iris-setosa":
        iris_class["Iris-setosa"] = iris_class["Iris-setosa"] + 1
    elif y[0] == "Iris-versicolor":
        iris_class["Iris-versicolor"] = iris_class["Iris-versicolor"] + 1
    else:
        iris_class["Iris-virginica"] = iris_class["Iris-virginica"] + 1
        
print("Vote :", iris_class)
print("Class of Pnew :", max(iris_class, key=iris_class.get))
