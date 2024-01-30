from PyQt6 import QtWidgets
from vista.ContratosInmuebles import Ui_MainWindow
from controlador.ControladorPantallaRegistroClienteContrato import ControladorPantallaRegistroClienteContrato
from controlador.ControladorPantallaRegistroInmuebleContrato import ControladorPantallaRegistroInmuebleContrato
from modelo.manejoDB import ManejoDB
from modelo.ReportesBienesRaices import reportes_BienesRaices


class ControladorPantallaContratos(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.vista = Ui_MainWindow()
        self.vista.setupUi(self)
        self.vista.btn_RegistrarContratoCompra.clicked.connect(self.registrar_contrato_compra)
        self.vista.btn_RegistrarContratoVenta.clicked.connect(self.registrar_contrato_venta)
        self.vista.btn_Regresar.clicked.connect(self.regresar)
        self.vista.chb_ActivarAlquilerCompra.stateChanged.connect(self.activar_alquiler_compra)
        self.vista.dt_FechafinalContratoCompra.setEnabled(False)
        self.actualizar_tabla_contratos_compra()
        self.actualizar_tabla_contratos_venta()
        self.activar_alquiler_compra(False)
        self.actualizar_cmbs()
    def registrar_contrato_compra(self):
        self.controlador_Cliente = ControladorPantallaRegistroClienteContrato()
        self.controlador_Cliente.show()
        self.controlador_Cliente.datos_clientes_confirmados.connect(self.registrar_en_base_compra)
        
    def registrar_contrato_venta(self):
        self.controlador_Inmueble = ControladorPantallaRegistroInmuebleContrato()
        self.controlador_Inmueble.show()
        self.controlador_Inmueble.datos_inmueble.connect(self.inmueble_en_buffer)
        self.controlador_Inmueble.contrato_cliente.datos_clientes_confirmados.connect(self.registrar_en_base_venta)
        
    
    def inmueble_en_buffer(self,tuple):
        self.inmueble_buffer = tuple
        
        
        
    def registrar_en_base_compra(self,tuple):
        manejoDB = ManejoDB()
        fecha_inicio = self.vista.dt_FechaInicioContratoCompra.date().toString("yyyy-MM-dd")
        fecha_final = self.vista.dt_FechafinalContratoCompra.date().toString("yyyy-MM-dd")
        id_inmueble = self.vista.cmb_InmuebleContratoCompra.currentText()
        id = manejoDB.ultima_secuencia('contrato_compra','id')[0][0] + 1
        if(manejoDB.consulta_existencia('cliente','id',tuple[0]) == []):#no existe el cliente
            manejoDB.insertar_en('cliente',('id','nombre','apellido','localizacion','direccion','telefono','email'),tuple)
        if(self.vista.chb_ActivarAlquilerCompra.isChecked()): #esta alquilando por lo que debe tener fecha fin
            manejoDB.insertar_en('contrato_compra',('id','fecha_inicio','fecha_fin','cliente_comprador','id_inmueble'),(id,fecha_inicio,fecha_final,tuple[0],id_inmueble))
        else:
            manejoDB.insertar_en('contrato_compra',('id','fecha_inicio','cliente_comprador','id_inmueble'),(id,fecha_inicio,tuple[0],id_inmueble))

        self.actualizar_tabla_contratos_compra()
    
    def registrar_en_base_venta(self,tuple_cliente):
        agente = self.vista.cmb_AgenteContratoVenta.currentText()
        fecha_inicio = self.vista.dt_FechaInicioContratoVenta.date().toString("yyyy-MM-dd")
        fecha_final = self.vista.dt_FechafinalContratoVenta.date().toString("yyyy-MM-dd")
        tipo = self.vista.cmb_TipoContratoVenta.currentText()
        comision = self.vista.txt_ComisionContratoVenta.text()
        manejoDB = ManejoDB()
        id_venta = manejoDB.ultima_secuencia('contrato_venta','id')[0][0] + 1
        id_inmueble = manejoDB.ultima_secuencia('inmueble','id')[0][0] + 1
        self.inmueble_buffer = (id_inmueble,) + self.inmueble_buffer
        if(manejoDB.consulta_existencia('cliente','id',tuple_cliente[0]) == []):#no existe el cliente
            manejoDB.insertar_en('cliente',('id','nombre','apellido','localizacion','direccion','telefono','email'),tuple_cliente)
        manejoDB.insertar_en('inmueble',('id','tipo','direccion','localizacion','precio','num_de_pisos','num_de_cuartos','anio_de_construccion','piscina','area','num_de_banos','estacionamiento','descripcion'),self.inmueble_buffer)
        # manejoDB.insertar_en('contrato_venta',('id','fecha_inicio','fecha_fin','cliente_vendedor','id_inmueble','asesor','tipo','comision'),(id_venta,fecha_inicio,fecha_final,tuple_cliente[0],id_inmueble,'1',tipo,comision))
        manejoDB.insertar_en('contrato_venta',('id','fecha_inicio','fecha_fin','cliente_vendedor','id_inmueble','asesor','tipo','comision'),(id_venta,fecha_inicio,fecha_final,tuple_cliente[0],id_inmueble,agente,tipo,comision))

        self.inmueble_buffer = None
        self.actualizar_tabla_contratos_venta()
    
    def actualizar_tabla_contratos_compra(self):
        manejoDB = ManejoDB()
        contratos_compras = manejoDB.consultar('SELECT * FROM contrato_compra;')
        self.vista.tbl_ContratoCompra.setRowCount(0)
        for contrato in contratos_compras:
            row_position = self.vista.tbl_ContratoCompra.rowCount()
            self.vista.tbl_ContratoCompra.insertRow(row_position)
            self.vista.tbl_ContratoCompra.setItem(row_position , 0, QtWidgets.QTableWidgetItem(str(contrato[0])))
            self.vista.tbl_ContratoCompra.setItem(row_position , 1, QtWidgets.QTableWidgetItem(contrato[1].strftime("%d-%m-%Y")))
            if(contrato[2] == None):
                self.vista.tbl_ContratoCompra.setItem(row_position , 2, QtWidgets.QTableWidgetItem(''))
            else:
                self.vista.tbl_ContratoCompra.setItem(row_position , 2, QtWidgets.QTableWidgetItem(contrato[2].strftime("%d-%m-%Y")))
            self.vista.tbl_ContratoCompra.setItem(row_position , 3, QtWidgets.QTableWidgetItem(str(contrato[3])))
            self.vista.tbl_ContratoCompra.setItem(row_position , 4, QtWidgets.QTableWidgetItem(str(contrato[4])))
    def actualizar_tabla_contratos_venta(self):
        manejoDB = ManejoDB()
        contratos_ventas = manejoDB.consultar('SELECT * FROM contrato_venta;')
        self.vista.tbl_ContratoVenta.setRowCount(0)
        for contrato in contratos_ventas:
            row_position = self.vista.tbl_ContratoVenta.rowCount()
            self.vista.tbl_ContratoVenta.insertRow(row_position)
            self.vista.tbl_ContratoVenta.setItem(row_position , 0, QtWidgets.QTableWidgetItem(str(contrato[0])))
            self.vista.tbl_ContratoVenta.setItem(row_position , 1, QtWidgets.QTableWidgetItem(contrato[1]))
            if(contrato[2] == None):
                self.vista.tbl_ContratoVenta.setItem(row_position , 2, QtWidgets.QTableWidgetItem(''))
            else:
                self.vista.tbl_ContratoVenta.setItem(row_position , 2, QtWidgets.QTableWidgetItem(contrato[2].strftime("%d-%m-%Y")))
                self.vista.tbl_ContratoVenta.setItem(row_position , 3, QtWidgets.QTableWidgetItem(contrato[3].strftime("%d-%m-%Y")))
                self.vista.tbl_ContratoVenta.setItem(row_position , 4, QtWidgets.QTableWidgetItem(str(contrato[4])))
                self.vista.tbl_ContratoVenta.setItem(row_position , 5, QtWidgets.QTableWidgetItem(str(contrato[5])))
                self.vista.tbl_ContratoVenta.setItem(row_position , 6, QtWidgets.QTableWidgetItem(str(contrato[6])))
                self.vista.tbl_ContratoVenta.setItem(row_position , 7, QtWidgets.QTableWidgetItem(str(contrato[7])))

    def actualizar_cmbs(self):
        manejoDB = ManejoDB()
        self.vista.cmb_AgenteContratoVenta.clear()
        self.vista.cmb_InmuebleContratoCompra.clear()
        agentes = manejoDB.consultar('SELECT * FROM agente;')
        for agente in agentes:
            self.vista.cmb_AgenteContratoVenta.addItem(str(agente[0]))

        manejoDB.cerrar_conexion()
             
    

    def activar_alquiler_compra(self, estado):
        self.vista.dt_FechafinalContratoCompra.setEnabled(estado == 2)
        reportes = reportes_BienesRaices()
        if(self.vista.chb_ActivarAlquilerCompra.isChecked()):
            inmuebles = reportes.listado_inmuebles_disponibles_en_alquiler()
        else:
            inmuebles = reportes.listado_inmuebles_disponibles_en_venta()
        self.vista.cmb_InmuebleContratoCompra.clear()
        for inmueble in inmuebles:
            self.vista.cmb_InmuebleContratoCompra.addItem(str(inmueble[0]))
        

    def activar_alquiler_venta(self, estado):
        self.vista.dt_FechafinalContratoVenta.setEnabled(estado == 2)

    def regresar(self):
        self.close()
