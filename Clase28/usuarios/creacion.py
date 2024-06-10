# Función que crea usuari@s - Sólo la definición
def validar_nombre(dato_str):
    
    if dato_str.isalpha():
        return True
    
    return False

def crear_usuario():
    nombre = input("Ingrese su nombre: ")
    
    if validar_nombre(nombre):
        print(f"Se creó el usuari@: {nombre}")
    else:        
        print("Dato inválido como nombre!!!")

def guardar_db():
    pass