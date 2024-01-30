from PyQt6 import QtWidgets

from modelo.manejoDB import ManejoDB
from modelo.ReportesBienesRaices import reportes_BienesRaices
from vista.ReportesInmobilaria import Ui_MainWindow


class ControladorPantallaReportes (QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.vista = Ui_MainWindow()
        self.vista.setupUi(self)
        self.vista.tabWidget.setCurrentIndex(0)
        self.inicializar_radio_buttons()
        self.ocultar_filtros()
        # Acciones de botones
        self.vista.rbtn_General.toggled.connect(self.actualizar_tabla_agentes_reportes)

        # Botones inicializados
        self.vista.chbx_FiltroTipo.stateChanged.connect(self.mostrar_filtros)
        self.vista.chbx_FiltroLocalizacion.stateChanged.connect(self.mostrar_filtros)
        self.vista.chbx_FiltroPrecio.stateChanged.connect(self.mostrar_filtros)
        self.vista.chbx_FiltroPisos.stateChanged.connect(self.mostrar_filtros)
        self.vista.chbx_FiltroCuartos.stateChanged.connect(self.mostrar_filtros)
        self.vista.chbx_FiltroAnio.stateChanged.connect(self.mostrar_filtros)
        self.vista.chbx_FiltroArea.stateChanged.connect(self.mostrar_filtros)
        self.vista.chbx_FiltroBanios.stateChanged.connect(self.mostrar_filtros)
        self.vista.rbtn_General.clicked.connect(self.mostrar_filtros)
        self.vista.rbtn_ContratosAgente.clicked.connect(self.mostrar_filtros)
        self.vista.rbtn_ContratosExpirarCompras.clicked.connect(self.mostrar_filtros)
        self.vista.rbtn_ContratosExpirarVentas.clicked.connect(self.mostrar_filtros)
        #boton consulta
        self.vista.btn_ConsultarInmueble.clicked.connect(self.actualizar_tabla_inmuebles_tipo)
        #botones clientes
        self.vista.rbtn_ClientesCompra.clicked.connect(self.actualizar_tabla_clientes_compradores_vendedores)
        self.vista.rbtn_ClientesVenden.clicked.connect(self.actualizar_tabla_clientes_compradores_vendedores)
        #botones reportes contratos por expirar
        self.vista.rbtn_ContratosExpirarCompras.clicked.connect(self.actualizar_tabla_contratos_por_expirar_compras)
        self.vista.rbtn_ContratosExpirarVentas.clicked.connect(self.actualizar_tablas_contratos_por_expirar_venta)

        self.actualizar_cmbs_reporte()
        self.inicializar_tablas()

    def mostrar_filtros(self):
        # checkBoxes
        self.vista.lbl_TipoFiltro.setVisible(self.vista.chbx_FiltroTipo.isChecked())
        self.vista.cmb_TipoFiltro.setVisible(self.vista.chbx_FiltroTipo.isChecked())
        self.vista.lbl_localizacionFiltro.setVisible(self.vista.chbx_FiltroLocalizacion.isChecked())
        self.vista.cmb_localizacionFiltro.setVisible(self.vista.chbx_FiltroLocalizacion.isChecked())
        self.vista.lbl_PrecioFiltro.setVisible(self.vista.chbx_FiltroPrecio.isChecked())
        self.vista.txt_PrecioFiltro.setVisible(self.vista.chbx_FiltroPrecio.isChecked())
        self.vista.lbl_NumPisosFiltro.setVisible(self.vista.chbx_FiltroPisos.isChecked())
        self.vista.txt_NumPisosFiltro.setVisible(self.vista.chbx_FiltroPisos.isChecked())
        self.vista.lbl_NumCuartosFiltro.setVisible(self.vista.chbx_FiltroCuartos.isChecked())
        self.vista.txt_NumCuartosFiltro.setVisible(self.vista.chbx_FiltroCuartos.isChecked())
        self.vista.lbl_AnioConstFiltro.setVisible(self.vista.chbx_FiltroAnio.isChecked())
        self.vista.txt_AnioConstruccionFiltro.setVisible(self.vista.chbx_FiltroAnio.isChecked())
        self.vista.lbl_AreaFiltro.setVisible(self.vista.chbx_FiltroArea.isChecked())
        self.vista.txt_AreaFiltro.setVisible(self.vista.chbx_FiltroArea.isChecked())
        self.vista.lbl_NumBaniosFiltro.setVisible(self.vista.chbx_FiltroBanios.isChecked())
        self.vista.txt_NumBaniosFiltro.setVisible(self.vista.chbx_FiltroBanios.isChecked())
        # radioButtons
        self.vista.lblAgenteReporte.setVisible(self.vista.rbtn_ContratosAgente.isChecked())
        self.vista.cmb_agenteSeleccionar.setVisible(self.vista.rbtn_ContratosAgente.isChecked())
        self.vista.tbl_agentesContratos.setVisible(self.vista.rbtn_ContratosAgente.isChecked())
        self.vista.tbl_ContratoVenta.setVisible(self.vista.rbtn_ContratosExpirarVentas.isChecked())

        self.vista.tbl_agentesGeneral.setVisible(self.vista.rbtn_General.isChecked())
        self.vista.tbl_ContratoCompra.setVisible(self.vista.rbtn_ContratosExpirarCompras.isChecked())
        #agente seleccionado ventas
        self.vista.cmb_agenteSeleccionar.currentIndexChanged.connect(self.actualizar_tabla_agentes_contratos)

    def inicializar_radio_buttons(self):
        self.vista.rbtn_General.setChecked(True)
        self.vista.rbtn_ClientesCompra.setChecked(True)
        self.vista.rbtn_ContratosExpirarCompras.setChecked(True)

    def ocultar_filtros(self):
        self.vista.lbl_TipoFiltro.setVisible(False)
        self.vista.cmb_TipoFiltro.setVisible(False)
        self.vista.lbl_localizacionFiltro.setVisible(False)
        self.vista.cmb_localizacionFiltro.setVisible(False)
        self.vista.lbl_PrecioFiltro.setVisible(False)
        self.vista.txt_PrecioFiltro.setVisible(False)
        self.vista.lbl_NumPisosFiltro.setVisible(False)
        self.vista.txt_NumPisosFiltro.setVisible(False)
        self.vista.lbl_NumCuartosFiltro.setVisible(False)
        self.vista.txt_NumCuartosFiltro.setVisible(False)
        self.vista.lbl_AnioConstFiltro.setVisible(False)
        self.vista.txt_AnioConstruccionFiltro.setVisible(False)
        self.vista.lbl_AreaFiltro.setVisible(False)
        self.vista.txt_AreaFiltro.setVisible(False)
        self.vista.lbl_NumBaniosFiltro.setVisible(False)
        self.vista.txt_NumBaniosFiltro.setVisible(False)
        self.vista.lblAgenteReporte.setVisible(False)
        self.vista.cmb_agenteSeleccionar.setVisible(False)
        self.vista.tbl_agentesContratos.setVisible(False)
        self.vista.tbl_ContratoVenta.setVisible(False)

    def actualizar_tabla_agentes_reportes(self): #numero de ventas
        reporteBienesRices = reportes_BienesRaices()
        self.vista.tbl_agentesGeneral.setRowCount(0)
        agentes = reporteBienesRices.agentes_num_ventas_realizadas()
        for agente in agentes:
            rowPosition = self.vista.tbl_agentesGeneral.rowCount()
            self.vista.tbl_agentesGeneral.insertRow(rowPosition)
            self.vista.tbl_agentesGeneral.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(agente[0]))
            self.vista.tbl_agentesGeneral.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(agente[1]))
            self.vista.tbl_agentesGeneral.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(agente[2]))
            self.vista.tbl_agentesGeneral.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(str(agente[3])))



    def actualizar_tabla_agentes_contratos(self):
        reportesBienesRaices = reportes_BienesRaices()
        self.vista.tbl_agentesContratos.setRowCount(0)
        ventas = reportesBienesRaices.ventas_asignadas_agente(self.vista.cmb_agenteSeleccionar.currentText().split(',')[0])
        
        for venta in ventas:
            rowPosition = self.vista.tbl_agentesContratos.rowCount()
            self.vista.tbl_agentesContratos.insertRow(rowPosition)
            self.vista.tbl_agentesContratos.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(venta[0]))
            self.vista.tbl_agentesContratos.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(venta[1]))
            self.vista.tbl_agentesContratos.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(venta[2]))
            self.vista.tbl_agentesContratos.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(str(venta[3])))
            self.vista.tbl_agentesContratos.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(str(venta[4])))
            self.vista.tbl_agentesContratos.setItem(rowPosition, 5, QtWidgets.QTableWidgetItem(venta[5]))
 

    def actualizar_tabla_inmuebles_tipo(self):
        dic_tipo_valor = {}
        if self.vista.chbx_FiltroTipo.isChecked():
            dic_tipo_valor['tipo'] = self.vista.cmb_TipoFiltro.currentText()
        if self.vista.chbx_FiltroLocalizacion.isChecked():
            dic_tipo_valor['localizacion'] = self.vista.cmb_localizacionFiltro.currentText().split('-')[0]
        if self.vista.chbx_FiltroPrecio.isChecked():
            dic_tipo_valor['precio'] = self.vista.txt_PrecioFiltro.text()
        if self.vista.chbx_FiltroPisos.isChecked():
            dic_tipo_valor['num_de_pisos'] = self.vista.txt_NumPisosFiltro.text()
        if self.vista.chbx_FiltroCuartos.isChecked():
            dic_tipo_valor['num_de_cuartos'] = self.vista.txt_NumCuartosFiltro.text()
        if self.vista.chbx_FiltroAnio.isChecked():
            dic_tipo_valor['anio_de_construccion'] = self.vista.txt_AnioConstruccionFiltro.text()
        if self.vista.chbx_FiltroArea.isChecked():
            dic_tipo_valor['area'] = self.vista.txt_AreaFiltro.text()
        if self.vista.chbx_FiltroBanios.isChecked():
            dic_tipo_valor['num_de_banos'] = self.vista.txt_NumBaniosFiltro.text()
        if self.vista.chbx_FiltroPiscina.isChecked():
            dic_tipo_valor['piscina'] = True
        if self.vista.chbx_FiltroParqueadero.isChecked():
            dic_tipo_valor['estacionamiento'] = True
        reportesBienesRaices = reportes_BienesRaices()
        inmuebles = reportes_BienesRaices.listado_inmueble_tipo(dic_tipo_valor)
        self.vista.tbl_inmueblesFiltro.setRowCount(0)
        for inmueble in inmuebles:
            rowPosition = self.vista.tbl_inmueblesFiltro.rowCount()
            self.vista.tbl_inmueblesFiltro.insertRow(rowPosition)
            self.vista.tbl_inmueblesFiltro.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(inmueble[0]))
            self.vista.tbl_inmueblesFiltro.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(inmueble[1])))
            self.vista.tbl_inmueblesFiltro.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(str(inmueble[2])))
            self.vista.tbl_inmueblesFiltro.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(str(inmueble[3])))
            self.vista.tbl_inmueblesFiltro.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(str(inmueble[4])))
            self.vista.tbl_inmueblesFiltro.setItem(rowPosition, 5, QtWidgets.QTableWidgetItem(str(inmueble[5])))
            self.vista.tbl_inmueblesFiltro.setItem(rowPosition, 6, QtWidgets.QTableWidgetItem(str(inmueble[6])))
            self.vista.tbl_inmueblesFiltro.setItem(rowPosition, 7, QtWidgets.QTableWidgetItem(str(inmueble[7])))
            self.vista.tbl_inmueblesFiltro.setItem(rowPosition, 8, QtWidgets.QTableWidgetItem(str(inmueble[8])))

    def actualizar_tabla_clientes_compradores_vendedores(self):
        reportes = reportes_BienesRaices()
        self.vista.tbl_clientesReporte.setRowCount(0)
        if self.vista.rbtn_ClientesCompra.isChecked():
            clientes = reportes.clientes_compradores()
        else:
            clientes = reportes.clientes_vendedores()
        for cliente in clientes:
            rowPosition = self.vista.tbl_clientesReporte.rowCount()
            self.vista.tbl_clientesReporte.insertRow(rowPosition)
            self.vista.tbl_clientesReporte.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(cliente[0]))
            self.vista.tbl_clientesReporte.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(cliente[1]))
            self.vista.tbl_clientesReporte.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(cliente[2]))
            self.vista.tbl_clientesReporte.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(str(cliente[3])))
            self.vista.tbl_clientesReporte.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(cliente[4]))

    def actualizar_tabla_contratos_por_expirar_compras(self):
        reportes = reportes_BienesRaices()
        self.vista.tbl_ContratoCompra.setRowCount(0)
        contratos = reportes.contratos_por_expirar_compras()
        
        for contrato in contratos:
            rowPosition = self.vista.tbl_ContratoCompra.rowCount()
            self.vista.tbl_ContratoCompra.insertRow(rowPosition)
            self.vista.tbl_ContratoCompra.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(contrato[0]))
            self.vista.tbl_ContratoCompra.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(contrato[1].strftime("%d-%m-%Y")))
            self.vista.tbl_ContratoCompra.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(contrato[2].strftime("%d-%m-%Y")))
            self.vista.tbl_ContratoCompra.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(contrato[3]))
            self.vista.tbl_ContratoCompra.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(str(contrato[4])))
            self.vista.tbl_ContratoCompra.setItem(rowPosition, 5, QtWidgets.QTableWidgetItem(contrato[5]))

    def actualizar_tablas_contratos_por_expirar_venta(self):
        reportes = reportes_BienesRaices()
        self.vista.tbl_ContratoVenta.setRowCount(0)
        contratos = reportes.contratos_por_expirar_ventas()
        for contrato in contratos:
            rowPosition = self.vista.tbl_ContratoVenta.rowCount()
            self.vista.tbl_ContratoVenta.insertRow(rowPosition)
            self.vista.tbl_ContratoVenta.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(contrato[0])))
            self.vista.tbl_ContratoVenta.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(contrato[1])))
            self.vista.tbl_ContratoVenta.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(contrato[2].strftime("%d-%m-%Y")))
            self.vista.tbl_ContratoVenta.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(contrato[3].strftime("%d-%m-%Y")))
            self.vista.tbl_ContratoVenta.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(contrato[4]))
            self.vista.tbl_ContratoVenta.setItem(rowPosition, 5, QtWidgets.QTableWidgetItem(contrato[5]))
            self.vista.tbl_ContratoVenta.setItem(rowPosition, 6, QtWidgets.QTableWidgetItem(str(contrato[6])))
            self.vista.tbl_ContratoVenta.setItem(rowPosition, 7, QtWidgets.QTableWidgetItem(str(contrato[7])))  
        


    def actualizar_cmbs_reporte(self):
        manejoDB = ManejoDB()
        nombre_agentes = manejoDB.consultar('SELECT agente.cedula,agente.nombre FROM agente')
        for nombre in nombre_agentes:
            self.vista.cmb_agenteSeleccionar.addItem(str(nombre[0]) + ',' + nombre[1])
        #actualizar localizaciones
        localizaciones = manejoDB.consultar('SELECT * FROM localizacion')
        for localizacion in localizaciones:
            self.vista.cmb_localizacionFiltro.addItem(str(localizacion[0]) + '-' + str(localizacion[1]) + '-' + str(localizacion[2]))
        

    def inicializar_tablas(self):
        self.actualizar_tabla_agentes_reportes()
        self.actualizar_tabla_agentes_contratos()
        self.actualizar_tabla_clientes_compradores_vendedores()
        self.actualizar_tabla_contratos_por_expirar_compras()
        self.actualizar_tablas_contratos_por_expirar_venta()