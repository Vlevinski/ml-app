#!/usr/bin/python

import random
import numpy as np

from sklearn import linear_model
import matplotlib.pyplot as plt


def get_car_size():
    return [2.0, 2.4, 1.5, 3.5, 3.5, 3.5, 3.5, 3.7, 3.7]


def get_car_co2():
    return [196, 221, 136, 255, 244, 230, 232, 255, 267]


def set_x():
    return np.array(range(10)).reshape((-1, 1))


def set_y():
    return np.array([random.gauss(x, 0.75) for x in range(10)])


def model(x, y):
    return linear_model.LinearRegression().fit(x, y)


def view_data(x, y):
    """ plot scatter """
    plt.scatter(x, y)
    plt.title("Linear Regression ", fontsize=10)
    plt.xlabel('Independent values (X)')
    plt.ylabel('Dependent values (Y)')


def main():
    X = set_x()
    Y = set_y()
    print( "Input data")
    print("X: ", X)
    print("Y: ", Y)
    
    # model
    mdl = model(X, Y)
    print("")
    print("Linear_regression \n\t slope: ", mdl.coef_, "\n\t intercept:", mdl.intercept_)
    Y_ = mdl.predict(X)

    # show
    view_data(X, Y)
    plt.plot(X, Y_, color='coral', linewidth=3)
    plt.grid()
    plt.savefig("linear_regression.png", bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    main()
