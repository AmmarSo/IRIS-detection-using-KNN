import pandas as pd

dataframe = pd.read_csv("data/iris.csv")

dataframe.head()


# Distance calculation
def distance_euclidienne(x, xn):
    distance = 0
    for i in len(x):
        distance = distance + ((x-xn)*(x-xn))
    return distance

