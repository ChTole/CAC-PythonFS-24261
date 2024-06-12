import config_db

class Docente:
    # Atributos de clase
    tabla = 'docente'
    campos = ('nombre', 'apellido', 'cuit')
    conexion = config_db.conexion
    
    # Método constructor
    def __init__(self, nombre, apellido, cuit):
        # Atributo de instancia
        self.nombre = nombre
        self.apellido = apellido
        self.cuit = cuit
        
    def guardar_db(self):
        self.conexion.connect()
        cursor = self.conexion.cursor()
        consulta = f'INSERT INTO {self.tabla} {str(self.campos).replace("'","`")} VALUES (%s, %s, %s)'
        datos = (self.nombre, self.apellido, self.cuit)
        cursor.execute(consulta, datos)
        self.conexion.commit()
        self.conexion.close()
        
    @classmethod
    def obtener_todos(cls):
        cls.conexion.connect()
        cursor = cls.conexion.cursor(dictionary=True)
        consulta = f"SELECT * FROM {cls.tabla}"
        cursor.execute(consulta)
        datos = cursor.fetchall()
        cls.conexion.close()
        return datos
        
    @classmethod
    def obtener_registro(cls, id):
        cls.conexion.connect()
        cursor = cls.conexion.cursor(dictionary=True)
        consulta = f"SELECT * FROM {cls.tabla} WHERE id = %s;"
        cursor.execute(consulta, (id,))
        datos = cursor.fetchall()
        cls.conexion.close()
        return datos
        
    # @classmethod
    # def actualizar(cls, id, nombre, apellido, cuit):
    #     # ...
    #     consulta = f"UPDATE {cls.tabla} WHERE id = %s SET nombre = %s ... ;"
    #     datos = (id, nombre, apellido, cuit)
    #     cursor.execute(consulta.datos)
    #     # ...
