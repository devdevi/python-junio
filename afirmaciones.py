def primera_letra(lista_de_palabras):
    primeras_letras = []

    for palabra in lista_de_palabras:
        assert type(palabra) == str, f'{palabra} no es un str'
        assert len(palabra) > 0, 'No se permiten str vacios'

        primeras_letras.append(palabra[0].upper())

    return primeras_letras

if __name__ == "__main__":
    lista = ['Hola', 'Como', 'andas']
    result = primera_letra(lista)
    print(result)
    '''
    lista = ['Hola', 'Como', 1]
    assert type(palabra) == str, f'{palabra} no es un str'
    AssertionError: 1 no es un str '''