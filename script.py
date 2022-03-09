#! usr/bin/env python
import sys
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def regression(species_subset, i):
    """Makes a linear regression model based on the given iris species, comparing petal length and sepal length.
       Initial save name is "species.png", which can be changed in the regression function or outside using a rename function.
    """
    x = species_subset.petal_length_cm
    y = species_subset.sepal_length_cm
    regression = stats.linregress(x, y)
    slope = regression.slope
    intercept = regression.intercept
    plt.scatter(x, y, label = 'Data')
    plt.plot(x, slope * x + intercept, color = "red", label = 'Fitted line')
    plt.xlabel("Petal length (cm)")
    plt.ylabel("Sepal length (cm)")
    plt.legend()
    plt.title("%s" % i)
    plt.savefig("%s.png" % i)
    plt.clf()
def species_regression():
    """
    Loops through unique species in dataset in order to run linear regression function.
    Figures are renamed with appropriate species information and
    plt.clf is used to clear the plot between figures.
    """
    species_list = dataset.species.unique()
    print(species_list)
    for i in species_list:
        print(i)
        species_subset = dataset[dataset.species == i]
        regression(species_subset, i)

if __name__ == '__main__':
    dataset = pd.read_csv("iris.csv")
    species_regression()
