class Orden(object):
    contador_ordenes = 0

    def __init__(self, computadoras) -> None:
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._computadoras = computadoras

    def agregar_computadora(self, computadora):
        self._computadoras.append(computadora)

    