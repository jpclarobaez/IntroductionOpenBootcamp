"""
Escribe un programa en la consola de python que pida al usuario su peso (en kg) y estatura (en metros), calcule el
índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase Tu índice de masa corporal es
donde es el índice de masa corporal calculado redondeado con dos decimales. Tienes que subir capturas de pantalla en
una carpeta comprimida zip.
"""

peso = float(input('Introduce tu peso en kg:\n\t'))
estatura = float(input('Introduce tu altura en metros:\n\t'))
imc = peso / (estatura)**2
print(f"\n\tCon un peso de {peso} kg y una estatura de {estatura} metros, tu tu IMC es {peso} x {estatura}^2 es: {round(imc,2)}")