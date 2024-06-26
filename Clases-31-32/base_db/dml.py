class Tabla:
    
    # Constructor
    def __init__(self, n_tabla, n_campos, n_conexion):
        self.tabla = n_tabla
        self.campos = n_campos
        self.conexion = n_conexion
    
    # *** CRUD ***
    # Creador/"Constructor" de instancias de subclase
    def crear(self, valores, de_bbdd=False):
        if de_bbdd:
            # del modelo --> args = (valores) # (())
            for campo, valor in zip(self.campos, *valores):
                setattr(self, campo, valor)
        else:
            for campo, valor in zip(self.campos[1:], valores):
                setattr(self, campo, valor)
    
    def guardar_db(self):
        """
        INSERT INTO tabla (n, ..., z) VALUES
            (%s,... %s)
        """
        campos_q = str(self.campos[1:]).replace("'", "`")
        values_q = f"({'%s, ' * (len(self.campos)-2)} %s)"
        consulta = (f"INSERT INTO {self.tabla} {campos_q} "
                    f"VALUES {values_q};")
        datos = tuple(vars(self).values())
        rta_db = self.__conectar(consulta, datos)
        
        if rta_db:
            return 'Creación exitosa.'
        
        return 'No se pudo crear el registro.'
    
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
    def eliminar(cls, id):
        consulta = (f"DELETE FROM {cls.tabla} WHERE id = %s ;")
        rta_db = cls.__conectar(consulta, (id,))
        
        if rta_db:
            return 'Eliminación exitosa.'
            
        return 'No se pudo eliminar el registro.'
    
    # *** Método común en CRUD (encapsulado) ***
    @classmethod
    def __conectar(cls, consulta, datos=None):
        
        try:
            cursor = cls.conexion.cursor()
        except Exception as e:
            cls.conexion.connect()
            cursor = cls.conexion.cursor()
        
        if consulta.startswith('SELECT'):
            
            if datos != None:
                cursor.execute(consulta, datos)
            else:
                cursor.execute(consulta)
            
            rta_db = cursor.fetchall()
            
            if rta_db != []:
                resultado = [cls(registro, de_bbdd=True) \
                                for registro in rta_db]
                
                if len(resultado) == 1:
                    resultado = resultado[0]
                    
            else:
                resultado = False          
            
            cls.conexion.close()
        
        else:
            
            try:
                cursor.execute(consulta, datos)
                cls.conexion.commit()    
                cls.conexion.close()
                resultado = True
            except Exception as e:
                resultado = False
            
        return resultado
    
    
        
        