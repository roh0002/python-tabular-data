#! usr/bin/env python
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats 

def regression():
    """Makes a linear regression model based on the given iris species
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
    plt.savefig("species.png")

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
        regression()
        os.rename('species.png', "regress_%s.png" % i)
        plt.clf()

if __name__ == '__main__':
    dataset = pd.read_csv("iris.csv")
    species_regression()
