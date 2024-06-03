# Bucles indetermidados
# contador = 0

# while contador < 4:
#     print("Dentro del bucle!")
#     contador += 1 # contador = contador + 1

# Sentencias break, continue y else
cumplido = False
contador = 0
entrada = ''
print("Ingrese 3 números pares")

# while True: # No recomendable
while not cumplido:
    entrada = input("Ingrese dato: ")
    
    if entrada.isdigit() and int(entrada) % 2 == 0:
        contador += 1
    elif entrada.isdigit() and int(entrada) % 3 == 0:
        print("Se rompió el bucle!")
        break # NO SE EJECUTA EL ELSE!!!
    
    if contador < 3:
        continue
    else:
        cumplido = True
        
else: # Cuando la condición devuelve False
    print("Se recibieron los 3 números pares solicitados.")