# Conexión con la BBDD MySQL

# Documentación
# https://dev.mysql.com/doc/connector-python/en/connector-python-installation.html

import mysql.connector

# Establezco la conexión
conexion = mysql.connector.connect(user='root',
                                   password='',
                                   host='127.0.0.1',
                                   database='edtech2024')

# Interacción con los datos
cursor = conexion.cursor()

consulta = "SELECT * FROM docente;"
cursor.execute(consulta)

datos = cursor.fetchall()
print(datos)

# SIEMPRE CERRAR LA CONEXIÓN!!!
conexion.close()