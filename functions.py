"""
Author: Wiktor Kulesza
Date: 23.03.2021r.
"""
import numpy as np


def function1(x):
    if x.ndim == 1:
        x = np.reshape(x, (x.shape[0], 1))
    return -1 / 2 * np.sum(np.add(np.add(np.power(x, 4), np.multiply(np.power(x, 2), -16)), np.multiply(x, 5)), axis=1)


def evaluate(population):
    return np.sum(function1(population))


def evaluate_absolute(population):
    return np.sum(np.abs(function1(population)))


def find_best_in_population(population):
    arr = function1(population)
    return np.array([population[np.where( arr == np.amax(arr))[0]][0]])


def find_worst_in_population(population):
    arr = function1(population)
    return np.array([population[np.where( arr == np.amin(arr))[0]][0]])


def create_starting_population(num_of_entities, dimension, min_lim, max_lim):
    return np.random.randint(min_lim, high=max_lim, size=(num_of_entities, dimension))