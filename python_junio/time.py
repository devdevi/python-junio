# Importar libreria time
from time import time

# Variables
objetivo = int(input('Escoge un número: '))
# float(input('Escoge una precisión: '))
epsilon =  0.0001
# int(input('Escoge el tiempo máximo de ejecución (en segundos): '))
tiempo_maximo = 120
paso = epsilon**2
respuesta = 0.0
hora_inicio = time()
tiempo_transcurrido = 0.0
iteraciones = 0

# Aproximarse al resultado
while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo and tiempo_maximo > tiempo_transcurrido:
    print(abs(respuesta**2))
    print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso
    iteraciones += 1

#Calcular tiempo de ejecución
tiempo_transcurrido = time() - hora_inicio

# Mostrar resultado
if abs( respuesta**2 - objetivo ) >= epsilon:
	print ( f'No se encontró la raíz cuadrada de {objetivo}.' )
else:
	print ( f'La raíz cuadrada de {objetivo} es {respuesta}.' )

print ( f'La ejecución tardó {tiempo_transcurrido} segundos.' )
print ( f'Fueron necesarias {iteraciones} iteraciones.' )
