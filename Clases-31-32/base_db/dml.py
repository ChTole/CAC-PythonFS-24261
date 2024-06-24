class Tabla:
    
    # Constructor
    def __init__(self, n_tabla, n_campos, n_conexion):
        self.tabla = n_tabla
        self.campos = n_campos
        self.conexion = n_conexion
    
    # *** CRUD ***
    # Creador/"Constructor" de instancias de subclase
    def crear(self, valores):
        for campo, valor in zip(self.campos, valores):
            setattr(self, campo, valor)
    
    def guardar_db(self):
        pass
    
    # Lectura
    @classmethod 
    def obtener(cls, campo=None, valor=None):
        
        if campo == None or valor == None:
            consulta = f"SELECT * FROM {cls.tabla};"
            return cls.__conectar(consulta)
        else:
            consulta = (f"SELECT * FROM {cls.tabla} "
                        f"WHERE {campo} = %s;")
            return cls.__conectar(consulta, (valor,))
    
    # Modificación
    @classmethod 
    def actualizar(cls):
        pass
    
    # Eliminación
    @classmethod 
    def eliminar(cls):
        pass
    
    # *** Método común en CRUD (encapsulado) ***
    @classmethod
    def __conectar(cls, consulta, datos=None):
        
        try:
            cursor = cls.conexion.cursor()
        except Exception as e:
            cls.conexion.connect()
            cursor = cls.conexion.cursor()
        
        if datos == None:
            cursor.execute(consulta)
        else:
            cursor.execute(consulta, datos)
            
        datos = cursor.fetchall() # [(),()]
        
        if len(datos) == 1:
            resultado = cls(datos[0]) # [()]
        else:
            # lista por comprehensión
            resultado = [cls(dato) for dato in datos] # [(),(),...,()]

        cls.conexion.close()
        return resultado # Tarea: cls.conexion.commit()
    
    
        
        