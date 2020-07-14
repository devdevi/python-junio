# Ley de la suma

def f(n):
    for i in range(n):
        for j in range(n):
            print(i, j)


f(5)
# O(n) * O(n) = O(n * n) = O(n^2) = Crecimiento cuadrático
# Loop dentro de otro loop , Probablemente es cuadrático
