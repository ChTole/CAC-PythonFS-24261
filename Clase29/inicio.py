import pprint

from modelos import Docente

# Como instanciar Docente
# docente = Docente("Pedro", "Piecapiedra", '80123456780')
# docente.guardar_db()
# docente2 = Docente("Juan", "Perez", '80876543210')
# print(docente2.apellido)
pp = pprint.PrettyPrinter(indent=4)

# datos = Docente.obtener_todos()
# pp.pprint(datos)

datos2 = Docente.obtener_registro(2)
pp.pprint(datos2)