class Persona:
    def __init__(this, nombre: str, apellido: str, edad: int, *args, **kwargs): # double underscore dunder
        this.nombre = nombre
        this.apellido = apellido
        this.edad = edad

# No es obligatorio nombrarle con self, pero es lo recomendado
    def show_details(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')
    #pass -> Crear dato pero sin contenido

persona1 = Persona('Sebastian','Carrix', '20')
print(f'Objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')

#persona1.nombre = 'Joan Sebastian'
#persona1.apellido = 'Carrillo Baron'
#persona1.edad = 21
persona1.show_details()
persona1.genero = 'Masculino'
#Persona.show_details(persona1)


persona2 = Persona('Karla', 'Gomez', 30)
print(f'Objeto Persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')
persona2.nombre = 'Maria Jose'
persona2.apellido = 'Aranguren Velasquez'
persona2.edad = 21
# persona2.genero -> ERROR NOT DEFINED GENERO
# persona2.show_details()


