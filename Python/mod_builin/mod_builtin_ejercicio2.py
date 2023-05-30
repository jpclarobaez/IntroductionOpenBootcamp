"""
En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por
parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.
"""

from functools import reduce

def sum_only_odd(values: list):
    only_odd = filter(lambda x: x%2 != 0, values)
    sum_values = reduce(lambda x, y: x+y, only_odd)
    return sum_values

values = [1, 2, 3, 4, 5, 6, 7, 9, 12, 25, 48]
print(sum_only_odd(values))