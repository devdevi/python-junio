objetivo = int(input('Escoje un numero: '))
epsilon = 0
paso = epsilon**2
res= 0.0

while abs(res**2 - objetivo) >= epsilon and res <= objetivo:
    print(res)
    res += paso

if abs(res**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz del {objetivo}')
else:
    print(f'La RAIZ CUADRADA DEL OBJETIVO {objetivo} ES {res}')
