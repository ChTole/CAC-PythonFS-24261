# Otra manera de codear listas

una_lista = [
    [2, 4, 6], 
    [8, 10, 12]
]

# El str es inmutable
palabra = "Python"
print(palabra)
# palabra[1] = "i" # TypeError: 'str' object does not support item assignment

palabra = palabra[0] + "i" + palabra[2:] # reasignación
print(palabra)