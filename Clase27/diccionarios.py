# Diccionarios
# Pares {clave: valor} -> JSON

tareas = {
    "lunes": ["doy clases", "tomo clases"],
    "martes": ["compras", "doy clases"],
    "miércoles": (False, 3.14), 
}

print(type(tareas))
print(tareas["lunes"])

# Propiedades:
# ¿Ordenados? No hay índices => no son ordenados
# print(tareas[0]) # KeyError: 0
print(tareas)
# Heterogeneidad:
# Valores: cualquier objeto
# Claves: sólo objetos inmutables (str, int, float, tuple)
# Mutabilidad: si!
tareas["lunes"] = {24261: True, 24164: True}
print(tareas)

print(tareas["lunes"][24164])
print(tareas["martes"][1][4:])

# print(tareas['sábado']) # KeyError
print(tareas.get('sábado', False))

tareas['jueves'] = "soy una cadena"
print(tareas)

tareas['jueves'] = False
print(tareas)

# Las claves son únicas => "asigno" a una clave que ya existe, sobreescribo el valor
hobbies = {
    "sábado": [],
    "domingo": []
}