import sys
from sorting import algorithms
from sorting import execution_time_gathering
import matplotlib.pyplot as plt

def graphicsAlgorithms():
    minimum_size = 1000
    maximum_size = 5000
    step = 1000
    samples_by_size = 5
    
    table = execution_time_gathering.take_execution_time(minimum_size, maximum_size, step, samples_by_size)

    print("Size | Selection Sort | Quick sort | Heap sort")
    for row in table:
        print(row)


    # La primera columna será el eje X
    x = [row[0] for row in table]
    # Las siguientes columnas serán los valores de Y
    y1 = [row[1][0] for row in table]
    y2 = [row[2][0] for row in table]
    y3 = [row[3][0] for row in table]

    # Crear el gráfico
    plt.plot(x, y1, label="Selection", color='blue')
    plt.plot(x, y2, label="Quick", color='green')
    plt.plot(x, y3, label="Heap", color='red')

    plt.title('Comparation Sorting algorithms')
    plt.xlabel('Size')
    plt.ylabel('Time')
    plt.legend()
    plt.show()

    y1 = [row[1][1] for row in table]
    y2 = [row[2][1] for row in table]
    y3 = [row[3][1] for row in table]

    plt.plot(x, y1, label="Selection", color='blue')
    plt.plot(x, y2, label="Quick", color='green')
    plt.plot(x, y3, label="Heap", color='red')

    plt.title('Comparation Sorting algorithms Memory Usage')
    plt.xlabel('Size')
    plt.ylabel('Memory')
    plt.legend()
    plt.show()

def graphicsQuickHeap():
    minimum_size = 100000
    maximum_size = 500000
    step = 50000
    samples_by_size = 5
    table = execution_time_gathering.take_execution_time(minimum_size, maximum_size, step, samples_by_size, True)
    print("Size | Quick sort | Heap sort")
    for row in table:
        print(row)

    # La primera columna será el eje X
    x = [row[0] for row in table]
    # Las siguientes columnas serán los valores de Y
    y1 = [row[1][0] for row in table]
    y2 = [row[2][0] for row in table]

    # Crear el gráfico
    plt.plot(x, y1, label="Quick", color='blue')
    plt.plot(x, y2, label="Heap", color='green')

    plt.title('Comparation Sorting algorithms')
    plt.xlabel('Size')
    plt.ylabel('Time')
    plt.legend()
    plt.show()

    y1 = [row[1][1] for row in table]
    y2 = [row[2][1] for row in table]

    plt.plot(x, y1, label="Quick", color='blue')
    plt.plot(x, y2, label="Heap", color='green')

    plt.title('Comparation Sorting algorithms Memory Usage')
    plt.xlabel('Size')
    plt.ylabel('Memory')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    graphicsAlgorithms()
    graphicsQuickHeap()