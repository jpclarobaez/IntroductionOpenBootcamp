"""
En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del
archivo. Para ello, tendréis que acceder dos veces al archivo creado.
"""
import os

filename = 'myfile.txt'

# Crear archivo vacío si no existe
if not os.path.isfile(filename):
    f = open(filename, 'w+')
    f.close()

# Escribimos algo
f = open(filename, 'a')
f.write('Nueva línea por cada ejecución\n')
f.close()

# Lo leemos
f = open(filename, 'r')
datos = f.read()
f.close()
print(datos)