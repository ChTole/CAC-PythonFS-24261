# Colecciones
# - Listas (array)
# - Tuplas (simil array)
# - Diccionarios (JSON)
# - Conjuntos (set) y frozenset

# Listas
mi_lista = ["cadena", -5.5, True]

# Propiedades: 
print(mi_lista[1]) 
# Tienen índices => son ordenadas

# Aceptan distintos objetos => son heterogéneas
for elemento in mi_lista:
    print(f"elemento: {elemento} - clase: {type(elemento)}")

# Mutabilidad => son mutables, puedo modificar, agregar y quitar
mi_lista[0] = ["a", "b", "c"]
print(mi_lista)

mi_lista.pop() # elimino el último
print(mi_lista)

mi_lista.append(False) # agrego al final
print(mi_lista)

del mi_lista[1]
print(mi_lista)

# print(mi_lista[1.0]) # TypeError: list indices must be integers or slices, not float

# Tuplas
# Son ordenadas, heterogéneas e INMUTABLES.

mi_tupla = (1, True, ["a", "b"])
otra_tupla = 1, 2, 3

for valor in mi_tupla:
    print(f"elemento: {valor} - clase: {type(elemento)}")
    
# otra_tupla[0] = "a" # TypeError: 'tuple' object does not support item assignment

mi_tupla[2].append("c")
print(mi_tupla)

otra_tupla = "cadena"