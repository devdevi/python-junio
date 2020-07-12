class CasillaDeVotacion:

    def __init__(self, identificador, pais, name):

        self._identificador = identificador
        self._pais = pais
        self._region = None
        self.name = name

    @property
    def region(self):
        return self._region

    @region.setter
    def set_region(self, region):
        print(region in self._pais)
        if region in self._pais:
            self._region = region
            return
        raise ValueError(f'La region {region} no es valida en {self._pais}')

casilla = CasillaDeVotacion(123, ['Cancun', 'Morelos', 'Chiapas'], 'Jaipur')

casilla.set_region = 'Morelos'
print(casilla.name)
""" casilla.set_region = 'Monterrey' """
