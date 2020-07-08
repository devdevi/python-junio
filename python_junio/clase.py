class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

''' 1 Forma '''
estudiante = Persona('visaka', 'devi')
print(estudiante.__dict__)
''' {'nombre': 'visaka', 'apellido': 'devi'} '''
''' 2 Forma '''
estudiante2 = Persona({ nombre: 'Erika',  } )
estudiante2.nombre = 'erika'
estudiante2.apellido = 'it'

print(estudiante2)
