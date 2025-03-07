import sys
from sorting import algorithms
from sorting import execution_time_gathering
import matplotlib.pyplot as plt
import numpy as np

def graphicsQuickHeap():
    minimum_size = 100000
    maximum_size = 1000000
    step = 50000
    samples_by_size = 5
    table = execution_time_gathering.take_execution_time(minimum_size, maximum_size, step, samples_by_size, True)
    print("Size | Quick sort | Heap sort")
    for row in table:
        print(row)
    data = np.array(table)

    # La primera columna será el eje X
    x = data[:, 0]
    # Las siguientes columnas serán los valores de Y
    y1 = data[:, 1]
    y2 = data[:, 2]

    # Crear el gráfico
    plt.plot(x, y1, label="Quick", color='green')
    plt.plot(x, y2, label="Heap", color='red')

    plt.title('Comparation Sorting algorithms')
    plt.xlabel('X')
    plt.ylabel('Y')

    plt.legend()

    plt.show()

if __name__ == "__main__":
    minimum_size = 1000
    maximum_size = 10000
    step = 500
    samples_by_size = 5
    
    table = execution_time_gathering.take_execution_time(minimum_size, maximum_size, step, samples_by_size)

    print("Size | Selection Sort | Quick sort | Heap sort")
    for row in table:
        print(row)


    data = np.array(table)

    # La primera columna será el eje X
    x = data[:, 0]
    # Las siguientes columnas serán los valores de Y
    y1 = data[:, 1]
    y2 = data[:, 2]
    y3 = data[:, 3]

    # Crear el gráfico
    plt.plot(x, y1, label="Selection", color='blue')
    plt.plot(x, y2, label="Quick", color='green')
    plt.plot(x, y3, label="Heap", color='red')

    plt.title('Comparation Sorting algorithms')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()
    graphicsQuickHeap()