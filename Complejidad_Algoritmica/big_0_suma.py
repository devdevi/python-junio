# Ley de la suma

def f(n):
    for i in range(n):
        print(i)

    for i in range(n):
        print(i)

# O(n) + O(n) = O(n+n) = O(2n) = O(n) //Crecimiento lineal
# Loop solo probablemente es lineal
# En big O lo único que nos interesa es el termino mas grande sin coeficiente previo
