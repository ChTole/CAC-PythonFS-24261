def calcular_cuadrado(numero):
    return numero * numero

mi_numero = 5
cuadrado = calcular_cuadrado(mi_numero) # llega a la función el valor del argumento

print(mi_numero)
print(cuadrado)

def calcular_muchos_cuadrados(lista_nros):
    # [2, 3, 4] -> [4, 9, 16]
    for indice in range(len(lista_nros)):
        lista_nros[indice] = lista_nros[indice] * lista_nros[indice]
        
    return lista_nros

mi_lista = [2, 3, 4]
copia = mi_lista
print(calcular_muchos_cuadrados(copia)) # las colecciones llegan como referencia

print(mi_lista)
    