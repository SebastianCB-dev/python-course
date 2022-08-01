from logger_base import log

class Persona:
  def __init__(self, id_person=None, name=None, lastname=None, email=None):
    self._id_person = id_person
    self._name = name
    self._lastname = lastname
    self._email = email

  def __str__(self):
    return f'''
      - Person ID: {self._id_person}
      - Name: {self._name}
      - Lastname: {self._lastname}
      - Email: {self._email}
    '''
  
  @property
  def id_person(self):
    return self._id_person
  
  @id_person.setter
  def id_person(self, newID):
    self._id_person = newID

  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, newName):
    self._name = newName

  @property
  def lastname(self):
    return self._lastname
  
  @lastname.setter
  def lastname(self, newLastname):
    self._lastname = newLastname

  @property
  def email(self):
    return self._email
  
  @email.setter
  def email(self, newEmail):
    self._email = newEmail


if __name__ == '__main__':
  print('NORMAL'.center(60, '#'))
  persona1 = Persona(1, 'Joan', 'Carrillo', 'jcarrillo@gmail.com')
  log.debug(persona1)
  # Simulate an insert
  print('INSERT'.center(60, '#'))
  persona1 = Persona(name='Joan', lastname='Carrillo', email='jcarrillo@gmail.com')
  log.debug(persona1)
  # Simulate an update
  print('UPDATE'.center(60, '#'))
  persona1 = Persona(id_person=1)
  log.debug(persona1)
