from modelo.manejoDB import ManejoDB


class reportes_BienesRaices:
    @staticmethod
    def listado_inmuebles_disponibles_en_alquiler():
        reportesDB = ManejoDB()
        sql = """SELECT inmueble.id
                FROM inmueble
                JOIN contrato_venta ON inmueble.id = contrato_venta.id_inmueble
                WHERE contrato_venta.id_inmueble NOT IN 
                (SELECT inmueble.id 
                    FROM inmueble
                    JOIN contrato_compra ON inmueble.id = contrato_compra.id_inmueble
                ) AND contrato_venta.tipo = 'Alquiler'"""
        return reportesDB.consultar(sql)
    @staticmethod
    def listado_inmuebles_disponibles_en_venta():
        reportesDB = ManejoDB()
        sql = """SELECT inmueble.id
                FROM inmueble
                JOIN contrato_venta ON inmueble.id = contrato_venta.id_inmueble
                WHERE contrato_venta.id_inmueble NOT IN 
                (SELECT inmueble.id 
                    FROM inmueble
                    JOIN contrato_compra ON inmueble.id = contrato_compra.id_inmueble
                ) AND contrato_venta.tipo = 'Venta'"""
        return reportesDB.consultar(sql)

    @staticmethod
    def listado_inmuebles_disponibles():
        reportesDB = ManejoDB()
        sql = """SELECT inmueble.id
                FROM inmueble
                JOIN contrato_venta ON inmueble.id = contrato_venta.id_inmueble
                WHERE contrato_venta.id_inmueble NOT IN 
                (SELECT inmueble.id 
                    FROM inmueble
                    JOIN contrato_compra ON inmueble.id = contrato_compra.id_inmueble
                )"""
        return reportesDB.consultar(sql)

    @staticmethod
    def listado_inmueble_tipo(tipos):
        reportesDB = ManejoDB()
        sqldisponibles = """SELECT inmueble.tipo,inmueble.localizacion,inmueble.precio,inmueble.num_de_pisos,inmueble.anio_de_construccion,inmueble.piscina,inmueble.area,inmueble.num_de_banos,inmueble.estacionamiento
                FROM inmueble
                JOIN contrato_venta ON inmueble.id = contrato_venta.id_inmueble
                WHERE contrato_venta.id_inmueble NOT IN 
                (SELECT inmueble.id 
                    FROM inmueble
                    JOIN contrato_compra ON inmueble.id = contrato_compra.id_inmueble
                )"""
        for tipo,asignado in tipos.items():
            if(tipo == 'precio' or tipo == 'area'):
                sqldisponibles += f" AND inmueble.{tipo} <= '{asignado}'"
            else:
                sqldisponibles += f" AND inmueble.{tipo} = '{asignado}'"
        return reportesDB.consultar(sqldisponibles)
    
    @staticmethod
    def contratos_por_expirar_compras():
        reportesDB = ManejoDB()
        sql ="""SELECT * FROM(	
	                SELECT contrato_compra.id,contrato_compra.fecha_inicio,contrato_compra.fecha_fin,contrato_compra.cliente_comprador,contrato_compra.id_inmueble,(contrato_compra.fecha_fin - CURRENT_DATE) as tiempo_restante
	                FROM contrato_compra) as sub
                WHERE sub.tiempo_restante <0 or (sub.tiempo_restante>0 and sub.tiempo_restante<10);
            """
        return reportesDB.consultar(sql)

    @staticmethod
    def contratos_por_expirar_ventas():
        reportesDB = ManejoDB()
        sql ="""SELECT * FROM(	
                    SELECT contrato_venta.id,contrato_venta.asesor,contrato_venta.fecha_inicio,contrato_venta.fecha_fin,contrato_venta.cliente_vendedor,contrato_venta.tipo,contrato_venta.comision,contrato_venta.id_inmueble,(contrato_venta.fecha_fin - CURRENT_DATE) as tiempo_restante
                    FROM contrato_venta) as sub
                WHERE sub.tiempo_restante <0 or (sub.tiempo_restante>0 and sub.tiempo_restante<10);
            """
        return reportesDB.consultar(sql)
    
    @staticmethod
    def ventas_asignadas_agente(id_agente):
        reportesDB = ManejoDB()
        sql = f"""SELECT agente.cedula,agente.nombre,agente.apellido,contrato_venta.id,inmueble.id,inmueble.descripcion
                FROM agente
                JOIN contrato_venta ON agente.cedula = contrato_venta.asesor
                JOIN inmueble ON contrato_venta.id_inmueble = inmueble.id 
                WHERE agente.cedula = '{id_agente}'
                """
        return reportesDB.consultar(sql)
    @staticmethod
    def clientes_compradores():
        reportesDB = ManejoDB()
        sql = """ SELECT contrato_compra.cliente_comprador,cliente.nombre,cliente.apellido,inmueble.id,inmueble.descripcion
                    FROM contrato_compra
                    JOIN cliente ON contrato_compra.cliente_comprador = cliente.id
                    JOIN inmueble ON contrato_compra.id_inmueble = inmueble.id
              """
        return reportesDB.consultar(sql)
    @staticmethod
    def clientes_vendedores():
        reportesDB = ManejoDB()
        sql ="""SELECT contrato_venta.cliente_vendedor,cliente.nombre,cliente.apellido,inmueble.id,inmueble.descripcion
                FROM contrato_venta
                JOIN cliente ON contrato_venta.cliente_vendedor = cliente.id
                JOIN inmueble ON contrato_venta.id_inmueble = inmueble.id 
            """
        return reportesDB.consultar(sql)
    @staticmethod
    def agentes_num_ventas_realizadas():
        reportesDB = ManejoDB()
        sql = """SELECT agente.cedula,agente.nombre,agente.apellido, COUNT(contrato_compra.id) as ventas
                FROM agente
                JOIN contrato_venta ON agente.cedula = contrato_venta.asesor
                JOIN contrato_compra ON contrato_venta.id_inmueble = contrato_compra.id_inmueble
                GROUP BY agente.cedula,agente.nombre,agente.apellido"""
        return reportesDB.consultar(sql)
    @staticmethod
    def ventas_realizadas():
        reportesDB = ManejoDB()
        sql = """SELECT contrato_venta.id,c_vendedor.apellido,contrato_venta.asesor,contrato_venta.id_inmueble,c_comprador.apellido
                FROM contrato_venta
                JOIN contrato_compra ON contrato_venta.id_inmueble = contrato_compra.id_inmueble
                JOIN inmueble ON contrato_venta.id_inmueble = inmueble.id
                JOIN cliente AS c_vendedor ON contrato_venta.cliente_vendedor = c_vendedor.id
                JOIN cliente AS c_comprador ON contrato_compra.cliente_comprador = c_comprador.id
                """
        return reportesDB.consultar(sql)

    
        
    
    
    
    
    