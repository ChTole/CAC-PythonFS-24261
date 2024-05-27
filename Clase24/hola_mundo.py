# Comentarios
# alt 39 ' <- comilla simple
'''
Esto no es un Comentario,
es una manera de documentar
el código.
'''
# Propiedades del lenguaje
# - Tipado dinámico
# - Fuertemente tipado


# Tipos de datos - simples
# int - enteros
num_entero = 5

# float - decimales
num_decimal = 3.14

# str - cadenas
cadena = "Christian cat's"
otra_cadena = 'Christian dijo "Hola mundo"'
suma_de_cadenas = cadena + otra_cadena
# otra_concatenacion = cadena + num_entero
otra_concatenacion = (cadena + ' ') * num_entero

print(suma_de_cadenas)
print(type(suma_de_cadenas))
print(num_entero, num_decimal)
print(type(num_entero), type(num_decimal))

print(otra_concatenacion)

# bool - Booleanos
mi_verdad = True
algo_falso = False

print(mi_verdad, type(mi_verdad))
