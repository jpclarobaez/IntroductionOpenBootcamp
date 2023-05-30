"""
Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista.
No debería haber países repetidos (haz uso de set). Finalmente, muestra por consola la lista de países ordenados
alfabéticamente y separados por comas.
"""

import re

REGEX = r"([^,\s]+(?:\s+[^,\s]+)*)"
string_input = input('Introduce una lista de países separados por comas:\n\t')
countries = list(set(re.findall(REGEX, string_input)))
countries.sort()

res = ""
for country in countries:
    res += f"{country}, "
res = res[:-2]
print(res)