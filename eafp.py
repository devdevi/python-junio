'''
Easier to ask for forgiveness than permission
EAFP
 '''
def busca_pais(paises, pais):
    """
    Paises es un diccionario. País es la llave.
    Codigo con el principio EAFP.
    """
    try:
        return paises[pais]
    except KeyError:
        return None

'''
// Javascript

/**
* Paises es un objeto. Pais es la llave.
* Codigo con el principio LBYL.
*/
function buscaPais(paises, pais) {
  if(!Object.keys(paises).includes(pais)) {
    return null;
  }

  return paises[pais];
} '''

'''
Como puedes ver, el código de Python accede directamente a la llave y únicamente
si dicho acceso falla, entonces se captura la excepción y se provee el código
necesario. En el caso de JavaScript, se verifica primero que la llave exista
en el objeto y únicamente con posterioridad se accede.

Es importante resaltar que ambos estilos pueden utilizarse en Python, pero el
estilo EAFP es mucho más “pythonico”.

  '''

anime = {
    'Shounen': 'Naruto',
    'Mecha': 'Zoids',
    'Vampiros': 'Hellsing',
    'Espacio': 'Terra formars',
    'Demonios': 'Kimetsu no Yaiba',
    'Deportes': 'Capitan Tsubasa',
    'Comedia': 'Ranma 1/2',
    'Romance': 'Kimi no na wa',
}

def buscar_en_diccionario(diccionario,llave):
    try:
        return print(diccionario[llave])
    except KeyError as e:
        print(e)
        return (f'{llave} no se encontro en el diccionario')

def actualizar_genero_diccionario(diccionario,llave,valor):
    diccionario.update({llave:valor})
    return print(f'El diccionario ha sido actualizado \nLos generos son: {diccionario.keys()}')

def eliminar_valor_de_un_genero(diccionario,llave):
    try:
        diccionario_temp = {k:('Sin valor de llave'if diccionario.get(llave)==v else v) for k,v in diccionario.items()}
        diccionario.update(diccionario_temp)
        return print(f'Hola {diccionario.values()}')
    except NameError as e:
        print(e)
        return print(f'{llave} incorrecta')

def manipular_dict(diccionario):
    print(f'Animes disponibles: {diccionario.values()}')
    print('Menu \n1. Buscar genero \n2. Actualizar Genero y anime \n3. Eliminar una anime')
    seleccion_menu = int(input('Seleccione un número del menu: '))
    if seleccion_menu == 1:
        if seleccion_menu == 1:
        llave = str(input('Seleccione genero que desea buscar: '))
        llamar_funcion = buscar_en_diccionario(diccionario,llave)
        return manipular_dict(diccionario)
    elif seleccion_menu ==2:
        llave = str(input('Seleccione genero que desea agregar: '))
        valor = str(input('Seleccione anime que desea agregar al genero: '))
        llamar_funcion = actualizar_genero_diccionario(diccionario,llave,valor)
        return manipular_dict(diccionario)
    elif seleccion_menu == 3:
        llave = str(input('Seleccione genero del anime que desea eliminar: '))
        llamar_funcion = eliminar_valor_de_un_genero(diccionario,llave)
        return manipular_dict(diccionario)
    else:
            print('No se encontró número en el menu')
            return manipular_dict(diccionario)


x = manipular_dict(anime)