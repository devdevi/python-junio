# Recursividad Multiple

def fibonacci(n):

    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(8))
#O(2**n) //tiene varias llamadas recursivas y eso hace al algoritmo con un crecimiento exponencial


''' loop = crecimiento lineal
loop adentro de un loop = crecimiento cuadrático
funcion recursiva - genera mas de una llamada recursiva 2 o 3 o 4 = Crecimiento exponencial '''