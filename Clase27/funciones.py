# Funciones

# Tiempos de la función: 1° definición 2° invocación
# def saludar():
#     print("Hola")
    
# saludar()

# Parámetros
# def saludar(nombre):
#     print(f"Hola {nombre}")
    
# saludar(["a", "b", "c"])
# saludar("Christian")

# Parámetros y retorno
def saludar(nombre): # el parámetro es de ámbito local
    return f"Hola {nombre}"

saludo = saludar("Christian") # "Hola Christian"

# Ámbitos
# print(nombre) # NameError: name 'nombre' is not defined