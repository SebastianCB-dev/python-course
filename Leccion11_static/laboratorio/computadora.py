
from monitor import Monitor
from teclado import Teclado
from raton import Raton

class Computadora:
    contador_computadoras = 0

    def __init__(self, nombre: str, monitor: Monitor, teclado: Teclado, raton: Raton) -> None:
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton
        
    def __str__(self):
        return f'''
        {self._nombre}: {self._id_computadora}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}
        '''
if __name__ == '__main__':

    teclado1 = Teclado('Logitech', 'Bluetooth')
    raton1 = Raton('Delux', 'Bluetooth')
    monitor1 = Monitor('Janus', 25)
    computadora1 = Computadora('Gamer Sebas', monitor1, teclado1, raton1)

    print(computadora1)