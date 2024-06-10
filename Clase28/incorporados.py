# Módulos
# Docu https://docs.python.org/es/3/py-modindex.html
import datetime

# Funciones
# Docu https://docs.python.org/es/3/library/functions.html
sumatoria = sum([15, 4, -2.5])
print(sumatoria)

print(max([15, 4, -2.5]))
print(min([15, 4, -2.5]))

usuario = {
    "nombre": "Christian",
    "creación": datetime.date.today() # hoy!
}

# Diccionarios "ordenados"
print(usuario.keys())
print(usuario.values())
print(usuario.items())