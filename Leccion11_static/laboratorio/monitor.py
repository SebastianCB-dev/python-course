class Monitor(object):
    contador_monitores = 0

    def __init__(self, marca: str, tamanho: int) -> None:
        Monitor.contador_monitores += 1
        self._id_monitor = Monitor.contador_monitores
        self._marca = marca
        self._tamanho = tamanho

    def __str__(self):
        return f'ID: {self._id_monitor}, Marca: {self._marca}, Tamanho: {self._tamanho}'


if __name__ == '__main__':
    monitor1 = Monitor("Janus", 15)
    print(monitor1)
    monitor2 = Monitor("Samsung", 27)
    print(monitor2)
