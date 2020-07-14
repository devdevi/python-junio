# Ley de la suma

def f(n):
    for i in range(n):
        print(i)

    for i in range(n*n):
        print(i)

# O(n) + O(n*n) = O(n+n) = O(n + n^2) = O(n^2)  Crecimiento EXPONENCIAL
# En big O lo único que nos interesa es el termino mas grande sin coeficiente previo
