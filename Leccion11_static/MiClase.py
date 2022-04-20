class MiClase:

    variable_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
    
    @staticmethod
    def metodo_estatico():
        # Un metodo estático no recibe self
        print(MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

print(MiClase.variable_clase)
mi_clase = MiClase('Valor variable instancia')
print(mi_clase.variable_instancia)

MiClase.variable_clase2 = 'Valor variable clase2'

print(MiClase.variable_clase2)


