# Entrada y salida por consola
print("Soy una cadena", True, 3.14, -5)

# entrada = input("Ingrese un dato: ") # SIEMPRE DEVUELVE UNA CADENA
# print("Se ingresó ", entrada, " el dato es: ", type(entrada))

# Operar con datos de entrada
# num_1 = input("Ingrese un número: ")
# num_2 = input("Ingrese otro número: ")
# producto = float(num_2) * float(num_1)
# print("El producto de ", num_1, "por ", num_2, "es ", producto)

# Control de flujo
# 1 - Condicionales
num_1 = input("Ingrese un número: ")

if num_1.isdigit(): # devuelve True si la cadena sólo contiene dígitos
    print('Ingresó un número') # la tabulación es sintaxis!
    
print('Continúa mi algoritmo!')

edad = input("Ingrese su edad: ")

if edad.isdigit() and int(edad) in range(121): # range(121) = 0, 1 ... 120
    # anidar otra condición
    if int(edad) >= 18 :
        print('Sos mayor de edad.')
    else:
        print('Sos menor de edad.')
else:
    print("Dato no válido como edad.")

print('Continúa mi algoritmo...')


# 2 - Repetitiva indeterminada

# 3 - Repetitiva determinada

