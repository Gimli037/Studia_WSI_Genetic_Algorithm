"""
Author: Wiktor Kulesza
Date: 23.03.2021r.
"""
import numpy as np
import sys
import functions as f


def genetic_algorithm(population, c_p, m_p, num_of_iter, min_lim, max_lim):
    all_populations = [population]
    best_entity = f.find_best_in_population(population)
    best_values = [f.function1(best_entity)]
    for _ in range(num_of_iter):
        r = reproduction(population)
        m = crossing_and_mutation(r, c_p, m_p, min_lim, max_lim)
        x = f.find_best_in_population(m)
        if f.function1(x) > f.function1(best_entity):
            best_entity = x
        all_populations.append(m)
        best_values.append(f.function1(x))
    return all_populations, best_entity, best_values


def crossing_and_mutation(r, c_p, m_p, min_lim, max_lim):
    r = crossing(r, c_p)
    np.apply_along_axis(mutation, 1, r, m_p, min_lim, max_lim)
    return r


def crossing(r, c_p):
    r = np.random.permutation(r)
    for i in range(0, len(r), 2):
        if np.random.uniform(0, 1) <= c_p:
            length = len(r[i])
            x = np.random.randint(1, length - 1)
            r[i] = np.concatenate((r[i, 0:x], r[i + 1, x:]))
            r[i + 1] = np.concatenate((r[i + 1, 0:x], r[i, x:]))
    return r


def mutation(r, m_p, min_lim, max_lim):
    for j in range(len(r)):
            if np.random.uniform(0, 1) <= m_p:
                if np.random.uniform(0, 1) <= 0.5:
                    if r[j] + 1 <= max_lim:
                        r[j] += 1
                else:
                    if r[j] - 1 >= min_lim:
                        r[j] -= 1


def reproduction(population):
    a = np.subtract(f.function1(population), f.function1(f.find_worst_in_population(population)))
    r = np.divide(a, np.sum(a))
    r = r.cumsum()
    u = np.random.rand(len(r), 1)
    choices = (u < r).argmax(axis=1)
    return population[choices]
