"""
Author: Wiktor Kulesza
Date: 23.03.2021r.
"""
import functions as f
import ga
import numpy as np
import matplotlib.pyplot as plt


a = np.array([[-3, -3, -3, -3, -3, -3]])
print(f'Maksimum globalne funkcji (obliczone przeze mnie nie przez algorytm): {f.function1(a)[0]}')
min_lim = -15
max_lim = 15
num_of_iter = 5000
numbers = np.arange(1, num_of_iter + 2)
# needs a lot of time to run algorithm for population equal to 6000
populations = [6, 12, 60, 120, 600, 6000]
for num_of_pop in populations:
    pop, y, values = ga.genetic_algorithm(population=f.create_starting_population(num_of_pop, 6, min_lim, max_lim),
                                          c_p=0.75, m_p=0.05, num_of_iter=num_of_iter, min_lim=-min_lim, max_lim=max_lim)
    print(f'num of population: {num_of_pop}')
    print(f'best value: {f.function1(y)[0]} for entity: {y}')
    fig, ax = plt.subplots()
    ax.set_title(f'Ilość osobników w populacji = {num_of_pop}')
    plt.xlabel(f'Numer iteracji')
    plt.ylabel(f'Max_val funkcji przystosowania')
    trace_line = plt.plot(numbers, values, '--', linewidth=1, markersize=2)
    plt.show()

