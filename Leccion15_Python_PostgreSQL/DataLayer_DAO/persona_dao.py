from Persona import Persona
from conexion import Conexion
from logger_base import log

class PersonaDAO:
  '''
  DAO (Data Access Object)
  CRUD (Create, Read, Update, Delete)
  '''

  _SELECCIONAR  = 'SELECT * FROM people ORDER BY person_id'
  _INSERTAR     = 'INSERT INTO people(name, last_name, email) VALUES(%s, %s, %s)'
  _ACTUALIZAR   = 'UPDATE people SET name=%s, last_name=%s, email=%s WHERE person_id=%s'
  _DELETE       = 'DELETE FROM people WHERE person_id=%s'

  @classmethod
  def seleccionar(cls):
    with Conexion.obtenerCursor() as cursor: 
      cursor.execute(cls._SELECCIONAR)
      response = cursor.fetchall()
      personaList = []
      for registro in response:
        persona = Persona(registro[0], registro[1], registro[2], registro[3])
        personaList.append(persona)
      return personaList

  @classmethod
  def insertar(cls, persona: Persona):
    with Conexion.obtenerConexion():
      with Conexion.obtenerCursor() as cursor:
        valores = (persona.name, persona.lastname, persona.email)
        cursor.execute(cls._INSERTAR, valores)
        log.debug(f'Persona insertada: {persona}')
        return cursor.rowcount

  @classmethod
  def actualizar(cls, persona: Persona):
    with Conexion.obtenerConexion():
      with Conexion.obtenerCursor() as cursor:
        valores = (persona.name, persona.lastname, persona.email, persona.id_person)
        cursor.execute(cls._ACTUALIZAR, valores)
        log.debug(f'Persona actualizada: {persona}')
        return cursor.rowcount

  @classmethod
  def eliminar(cls, persona: Persona):
    with Conexion.obtenerConexion():
      with Conexion.obtenerCursor() as cursor:
        valores = (persona.id_person,)
        cursor.execute(cls._DELETE, valores)
        log.debug(f'Eliminada la persona con el ID: {persona.id_person}')
        return cursor.rowcount
if __name__ == '__main__':
  # Insertar un registro
  # persona1 = Persona(name='Juan', lastname='Perez', email='jperez@mail.com')
  # personas_insertadas = PersonaDAO.insertar(persona1)
  # log.debug(f'Personas insertadas: {personas_insertadas}')

  # Actualizar un Registro
  # persona1 = Persona(id_person=1, name='Juan Carlos', lastname='Juarez', email='jcjuarez@mail.com')
  # personas_actualizadas = PersonaDAO.actualizar(persona1)
  # log.debug(f'Personas actualizadas: {personas_actualizadas}')

  # Eliminar un registro
  persona1 = Persona(id_person=1)
  personas_eliminadas = PersonaDAO.eliminar(persona1)
  log.debug(f'Se eliminaron {personas_eliminadas} registros')

  # Listar
  personas = PersonaDAO.seleccionar()
  for persona in personas:
    log.debug(persona)