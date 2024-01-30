from modelo.manejoDB import ManejoDB
from modelo.ReportesBienesRaices import reportes_BienesRaices

class manejoBienesRaices():

    @staticmethod
    def generar_contrato_compra(datos):
        acceso_base = ManejoDB()
        reportesDB = reportes_BienesRaices()
        #verificar que el cliente que compra no sea el mismo que vende
        #primero vemos a que cliente le pertence el inmueble
        #si el id del cliente que compra es igual al id del cliente que vende, entonces no se puede realizar la compra
        
        id_inmueble = datos[3]
        
        sql = f"""SELECT contrato_venta.cliente_vendedor
                FROM contrato_venta
                WHERE contrato_venta.id_inmueble = id_inmueble;"""
        duenio_inmueble = acceso_base.consultar(sql)[0][0]
        disponibles = [inm[0] for inm in reportesDB.listado_inmuebles_disponibles()]
        if(duenio_inmueble == datos[2] or id_inmueble not in disponibles):
            return "Ingreso invalido"
        else:
            acceso_base.insertar_en('contrato_compra',('fecha_inicio','fecha_fin','cliente_comprador','id_inmueble'),datos)
            return "Se ha generado el contrato de compra"
    @staticmethod
    def generar_contrato_venta(datos):
        acceso_base = ManejoDB()
        sql_inmuebles_en_venta = f"""SELECT contrato_venta.id_inmueble
                                    FROM contrato_venta;"""
        inmuebles_en_venta = [inm[0] for inm in acceso_base.consultar(sql_inmuebles_en_venta)]
        inmueble = datos[6]
        if(inmueble in inmuebles_en_venta):
            return "Ingreso invalido"
        else:
            acceso_base.insertar_en('contrato_venta',('asesor','fecha_inicio','fecha_fin','cliente_vendedor','tipo','comision','id_inmueble'),datos)
            return "Se ha generado el contrato de venta"
 
    
    
    
    
        