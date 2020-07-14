import random
pasos = 0

def busqueda_binaria(lista, start, end, objetivo):
    global pasos
    pasos += 1

    if start > end:
        return False

    # Division enteros //
    medio = (start + end) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio]< objetivo:
        return busqueda_binaria(lista, medio + 1, end, objetivo)
    else:
        return busqueda_binaria(lista, start , medio-1, objetivo)


if __name__ == "__main__":
    tamano_lista = int(input('De que tamaño es la lista: '))
    objetivo = int(input('Que numero quieres encontrar: '))
    lista = sorted([random.randint(0, tamano_lista) for i in range(tamano_lista)])
    print (lista)
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
    print(f'El elemento {objetivo} {"esta🙂 "  if encontrado else "no esta💆 "} en la lista, Resultado en {pasos} Pasos')
