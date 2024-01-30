import psycopg2


class ManejoDB:
    def __init__(self):
        try:
            self.conexion = psycopg2.connect(
                host = "localhost",
                dbname = "BienesRaicesDB",
                user="postgres",
                password="Estudiante@22",
                port = "5432")
            self.cursor = self.conexion.cursor()
            print("Conexión exitosa a la base de datos")
        except Exception as e:
            print(e)
            print("Error al conectarse a la base de datos")
    
    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()
        print("Se ha cerrado la conexión a la base de datos") 
    
    def consultar(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall() 
    
    def consulta_general(self,tabla,columna,num_filas = 5):
        sql = f"""SELECT {columna} FROM {tabla} LIMIT {num_filas};"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def consulta_existencia(self,tabla,columna,id):
        try:
            sql = f"""SELECT {columna} FROM {tabla} WHERE {columna} = '{id}'"""
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return "Error al consultar la existencia del registro", e
    def insertar_en(self, tabla, columnas, datos):
        try:
            columnas_str = ', '.join(columnas)
            placeholders = ', '.join(['%s'] * len(datos))
            sql = f"""INSERT INTO {tabla} ({columnas_str}) VALUES ({placeholders});"""
            self.cursor.execute(sql, datos)
            self.conexion.commit()
            return "Se ha insertado correctamente en la tabla"
        except Exception as e:
            print(e)
            return "Error al insertar en la tabla", e   
    
    def actualizar_en(self, tabla, columnas, datos, id):
        try:
            set_clause = ', '.join(f"{col} = %s" for col in columnas)
            sql = f"""UPDATE {tabla} SET {set_clause} WHERE id = %s;"""
            self.cursor.execute(sql, (*datos, id))
            self.conexion.commit()
            return "Se ha actualizado correctamente en la tabla"
        except Exception as e:
            print(e)
            return "Error al actualizar en la tabla", e
    def eliminar_de(self,tabla,condicion):
        sql = f"""DELETE FROM {tabla} WHERE {condicion};"""
        self.cursor.execute(sql)
        self.conexion.commit()
        print("Se ha eliminado el registro de la tabla")
    def ultima_secuencia(self, table_name, column_name):
        try:
            sql = f"SELECT MAX({column_name}) FROM {table_name};"
            self.cursor.execute(sql)
            self.conexion.commit()
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return "Error synchronizing sequence", e