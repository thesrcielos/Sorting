import time

from sorting import algorithms
from sorting import constants
from sorting import data_generator
import tracemalloc

def take_execution_time(minimum_size, maximum_size, step, samples_by_size, two=False):
    return_table = []

    for size in range(minimum_size, maximum_size + 1, step):
        print("Processing size: " + str(size))
        table_row = [size]
        times = take_times(size, samples_by_size, two)
        return_table.append(table_row + times)

    return return_table


"""
    It will return three values, one for each algorithm: The execution time for that size on each algorithm
"""


def take_times(size, samples_by_size, two):
    samples = []
    for _ in range(samples_by_size):
        samples.append(data_generator.get_random_list(size))
    if two:
        return [
        take_time_for_algorithm(samples, algorithms.quick_sort),
        take_time_for_algorithm(samples, algorithms.heap_sort),
        ]
    return [
        take_time_for_algorithm(samples, algorithms.selection_sort),
        take_time_for_algorithm(samples, algorithms.quick_sort),
        take_time_for_algorithm(samples, algorithms.heap_sort),
    ]


"""
    Returns the median of the execution time measures for a sorting approach given in 
"""


def take_time_for_algorithm(samples_array, sorting_approach):
    times = []
    memory_usage = []
    for sample in samples_array:
        tracemalloc.start()
        start_time = time.time()
        sorting_approach(sample.copy())
        end_time = time.time()
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        times.append(int(constants.TIME_MULTIPLIER * (end_time - start_time)))
        memory_usage.append(peak)
    times.sort()
    return times[len(times) // 2], memory_usage[len(memory_usage) // 2]
