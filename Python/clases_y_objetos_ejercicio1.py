
class Ruedas:
    marca = 'Michelin'
    diametro = 21
    ancho = 180

class Vehiculo:
    color = ""
    ruedas = Ruedas()
    puertas = 4

    def __init__(self, color = "", puertas = 4):
        self.color      = color
        self.puertas    = puertas

class Coche(Vehiculo):
    velocidad = 120
    cilindrada = 0

    def __init__(self, cilindrada=0, color='Rojo', puertas=4):
        super().__init__(color, puertas)
        self.cilindrada = cilindrada

    def __str__(self):
        info = f"\nEste coche de {self.cilindrada} cc es de color {self.color} y tiene {self.puertas} puertas." \
               f"\n\t* Marca de ruedas: {self.ruedas.marca} con un diámetro de {self.ruedas.diametro} pulgadas"
        return info

micoche = Coche(cilindrada=2400, color='Rojo', puertas=4)
print(micoche)