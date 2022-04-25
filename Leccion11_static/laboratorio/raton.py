from dispositivo_entrada import DispositivoEntrada

class Raton(DispositivoEntrada):

    contador_ratones = 0

    def __init__(self, marca: str, tipo_entrada: str) -> None:
        Raton.contador_ratones += 1
        self._id_raton = Raton.contador_ratones
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'ID: {self._id_raton}, Marca: {self._marca}, Tipo_entrada: {self._tipo_entrada}'

if __name__ == '__main__':
    raton1 = Raton('HP', 'USB')
    raton2 = Raton('Logitech', 'Bluetooth')
    print(raton1)
    print(raton2)


    
