
def listarTerminos(nombre, *nombres, **kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

listarTerminos(IDE='Integrated Development Environment', PK='Primary Key')
listarTerminos(DBMS='DataBase Management System')
