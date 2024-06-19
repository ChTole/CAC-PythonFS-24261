from componentes.config_db import conexion

def obtener_datos():
    datos =  {"mensaje": 'Sin conexión a la BBDD!'}
    con = conexion
    
    try:
        cursor = con.cursor(dictionary=True)
        print('conectada!')
    except Exception as e:
        print(type(e))
        con.connect()
        cursor = con.cursor(dictionary=True)
        print('reconectada!')
    
    consulta = "SELECT * FROM test;"
    cursor.execute(consulta)
    datos = cursor.fetchall()
    con.close()
    
    return datos        