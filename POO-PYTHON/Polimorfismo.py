class Persona:

    def __init__(self, name):
         self.name = name

    def avanza(self):
        print(f'{self.name}: Ando caminando')

""" ciclista extiende Persona """
class  Ciclista(Persona):

    def __init__(self, name):
        super().__init__(name)

    """ Cuando un ciclista avanza no avanza
        de la misma forma que una persona """
    def avanza(self):
        """ return super().avanza() """
        print(f'{self.name}: Ando moviéndome en la bicicleta')

""" Si este archivo se ejecuta directamente
    desde la terminal este es el punto de entrada
"""

def main():
    persona = Persona('David')
    persona.avanza()

    ciclista = Ciclista('Visaka')
    ciclista.avanza()

if __name__ == "__main__":
    main()