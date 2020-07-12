class Coordenada:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otra_cordenada):
        x_diff = (self.x -otra_cordenada.x)**2
        y_diff = (self.y -otra_cordenada.y)**2
        # Elevamos al 0.5 para ver la raíz cuadrada
        return (x_diff + y_diff)**0.5

# Entry point , si este archivo se ejecuta directamente de la terminal, nosotros lo podemos correr
if __name__ == "__main__":
    coor_1 = Coordenada(3, 30)
    coor_2 = Coordenada(4, 8)
    print(coor_1.distancia(coor_2))
    # Cordenada es instancia de Coordenada
    print(isinstance(coor_2, Coordenada))
    # Cordenada NO es instancia de Coordenada
    print(isinstance('HOLA', Coordenada))
