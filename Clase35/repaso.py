# Conectar front y back

# API-REST - Lo más utilizado por su eficiencia

# Patrón MVT ó MCV
# Model - View - Template
# Modelo - Controlador - Vista
# Tabla BBDD - Back - HTML

# Tipos de datos - Tipos de objetos!!!
# Datos simples
# str - bool - int - float
# Colecciones
# tuple, list, dict
# Orden, heterogeneidad, mutabilidad


# Python dict -> Object JS -> JSON

diccionario = {
    "hoy": 'Lunes'
}

# Valores y referencias

lista = [1, 2, 3]
nva_lista = lista # NO ES UNA COPIA, ES UNA REFERENCIA

print(lista is nva_lista) # Identidad
print(id(lista))
print(id(nva_lista))

copia = lista.copy()
print(id(copia))

# Buscar copia profunda
import copy

copia_de_verdad = copy.deepcopy(lista)
print(id(copia_de_verdad))

lista.append('a')

print(lista)
print(nva_lista)
print(copia)
print(copia_de_verdad)