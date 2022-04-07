
#Encapsulamiento con "_" -> Si se quiere ser mas restrictivo usar "__" en las variables dentro de la clase.
class Persona:
    def __init__(self, nombre: str, apellido: str, edad: int) -> None:
        self._nombre = nombre
        #self.__apellido = apellido
        self._apellido = apellido
        self._edad = edad
    
    @property # Especificar que es un get (Propiedad de una clase)
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self._nombre = nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido: str):
        self._apellido = apellido
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad: int):
        self._edad = edad
    
    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')

    #Destructor 
    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido}')

# persona1.__nombre
# persona1._nombre
# La diferencia entre _ y __ es que con el _ se espcifica que es privado pero python deja cambiarlo
# Con el __ python no cambia sus valores por fuera de la clase

if __name__ == '__main__':

    persona1 = Persona('Jairo', 'Carrillo', 64)
    persona1.nombre = 'Jairo Ignacio'
    persona1.apellido = 'Carrillo Carreño'
    persona1.mostrar_detalle()
