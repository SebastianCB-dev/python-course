from dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):

    # Static attribute
    contador_teclados = 0

    def __init__(self, marca: str, tipo_entrada: str) -> None:
        Teclado.contador_teclados += 1
        self._id_teclado = Teclado.contador_teclados
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'ID: {self._id_teclado}, Marca: {self._marca}, Tipo_entrada: {self._tipo_entrada}'

if __name__ == '__main__':
    teclado1 = Teclado('Logitech', 'Bluetooth')
    print(teclado1)
    teclado2 = Teclado('Reddragon', 'USB')   
    print(teclado2)     


