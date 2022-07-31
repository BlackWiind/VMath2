#Решение системы линейных уравнений

from array import array
from copy import copy

iterations = 0
n = 4
accuracy = 0.0001
x = array('d', [])
prev_calculation = array('d', [])

x.append(2.5)
x.append(-2.43)
x.append(-0.88)
x.append(0.74)

while True:
    iterations += 1
    prev_calculation = copy(x)

    x[0] = 2.5 - (0.3 * prev_calculation[1] - 0.13 * prev_calculation[2] + 0.31 * prev_calculation[3])
    x[1] = -2.43 - (-0.08 * x[0] + 0.3 * prev_calculation[2] + 0.35 * prev_calculation[3])
    x[2] = -0.88 - (0.17 * x[0] + 0.29 * x[1] + 0.2 * prev_calculation[3])
    x[3] = 0.74 - (0.23 * x[0] - 0.19 * x[1] + 0.4 * x[2])

    difference = abs(x[0] - prev_calculation[0])
    for j in range(n):
        if abs(x[j] - prev_calculation[j]) > difference:
            difference = abs(x[j] - prev_calculation[j])

    if difference < accuracy:
        break

print("\tОтвет:")
for i in range(n):
    print("\tx", i, "= %.4f" % x[i])
print("Количество итераций = ", iterations)
input("Нажмите любую клавишу...")
