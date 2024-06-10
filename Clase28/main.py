# Módulos
# Fundamento - creación

# import usuario
# from usuario import crear_usuario
# 1ra opción
# from usuarios.creacion import crear_usuario
# 2da opción
import usuarios.creacion as uc
# from paquete.modulo import función
from usuarios.logueo import iniciar_sesion

opcion = ''
menu = """
** Menú **
1 - Crear usuari@
2 - Iniciar sesión
3 - Salir
"""

while opcion != "3":
    print(menu)
    opcion = input("Ingrese su opción: ")
    
    if opcion == "1":
        # print("Creación en construcción")
        # usuario.crear_usuario()
        # 1ra opción
        # crear_usuario()
        # 2da opción
        uc.crear_usuario()
    elif opcion == "2":
        # print("Logueo en construcción")
        saludo = iniciar_sesion()
        print(saludo)
    elif opcion == "3":
        print("Adiós!!!")
    else:
        print("Opción incorrecta!")