objetivo = int(input('Escoje un entero: '))
res=0
while res**2 < objetivo:
    print(res)
    print(1*1)
    res += 1
if res**2 == objetivo:
    print(f'la raiz cuadrada de {objetivo} es {res}')
else:
    print(f'{objetivo} no tiene raiz cuadrada exacta {res}')
