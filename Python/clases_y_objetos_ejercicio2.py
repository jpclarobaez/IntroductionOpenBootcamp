
class Alumno:
    _nombre = ""
    _nota = -1

    def __init__(self, nombre="", nota=-1):
        self._set_nombre(nombre)
        self._set_nota(nota)

    def _set_nota(self, nota):
        if nota >= 0:
            self._nota = nota
        else:
            nota = input(f'¿Qué nota ha sacado {self._get_nombre()}?\n\t')
            self._set_nota(int(nota))

    def _get_nota(self):
        return self._nota

    def _set_nombre(self, nombre):
        if len(nombre) == 0:
            self._set_nombre(input('Introduce el nombre del alumno:\n\t'))
        else:
            self._nombre = nombre

    def _get_nombre(self):
        return self._nombre

    def cambiar_nota(self, nota):
        print(f'La nota de {self._get_nombre()} cambia de {self._get_nota()} a {nota}')
        self._set_nota(nota)

    def _aprobado(self):
        if self._get_nota() >= 5:
            return True
        else:
            return False

    def __str__(self):

        info = f"\nEsta clase representa al alumno {self._get_nombre()} y que tiene una nota de {self._get_nota()}."
        if self._aprobado():
            info += "\nPor lo tanto ha aprobado. \n\t\tENHORABUENA!\n\n"
        else:
            info += "\nLamentablemente ha suspendido. Prueba en Septiembre!"
        return info

# Instancia de la clase con los dos argumentos
alumno1 = Alumno('Pepe', 5)
print(alumno1)

# Instancia de la clase con sólo un argumento
alumno2 = Alumno('Juan')
print(alumno2)
alumno2.cambiar_nota(3) # Cambio de argumento
print(alumno2)

# Instancia de la clase sin argumentos para que te los pida por pantalla
alumno3 = Alumno()
print(alumno3)