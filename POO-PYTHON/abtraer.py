class Lavadora:
    def __init__(self):
       #No hay cuerpo en ese codigo pass
        pass

    # Metedo 📢
    def lavar(self, temperatura='Caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_de_agua(self, temperatura):
        print(f'1. 🕙 Llenando el tanque con agua {temperatura}')

    def _anadir_jabon(self):
        print('2. 🕙 Añadiendo jabón')

    def _lavar(self):
        print('3. 🕙 Lavando la ropa')

    def _centrifugar(self):
        print('4. Centrifugando la ropa 👕 ')

''' Si el archivo se ejecuta directamente este el el punto de partida '''
if __name__ == "__main__":

    lavadora = Lavadora()
    lavadora.lavar()