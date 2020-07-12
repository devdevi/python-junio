""" Superclase """
class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

""" Subclase, reutiliza la Superclase
La clase cuadrado extiende al Rectangulo """
class Cuadrado(Rectangulo):

    def __init__(self, lado):
        """ Obtenemos referencias al Rectángulo que espera dos parametros
            para ello le decimos que tanto la base por altura es igual a lado """
        super().__init__(lado, lado)


if __name__ == "__main__":

    rectangulo = Rectangulo(4, 16)
    print(rectangulo.area())

    cuadrado = Cuadrado(4)
    print(cuadrado.area())
