from PyQt6 import QtWidgets
from vista.RegistroClienteContrato import Ui_RegistroClienteContrato
from modelo.manejoDB import ManejoDB
from PyQt6.QtCore import pyqtSignal


class ControladorPantallaRegistroClienteContrato(QtWidgets.QMainWindow):
    datos_clientes_confirmados = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()
        self.vista = Ui_RegistroClienteContrato()
        self.vista.setupUi(self)
        self.ocultar_clientes_cmb()
        self.vista.btn_ConfirmarContrato.clicked.connect(self.confirmar_contrato)
        self.vista.btn_CancelarContrato.clicked.connect(self.cancelar)
        self.vista.chb_ActivarClientesRegistrados.stateChanged.connect(self.boton_check_activado)
        self.vista.cmb_ClienteSeleccionar.currentIndexChanged.connect(self.llenar_campos_cliente)
        self.actualizar_cmbs()

    def confirmar_contrato(self):
        cedula = self.vista.txt_CedulaAgregarCliente.text()
        nombre = self.vista.txt_NombreAgregarCliente.text()
        apellido = self.vista.txt_ApellidoAgregarCliente.text()
        localizacion = self.vista.cmb_localizacion_registro_clientes.currentText().split('-')[0]
        direccion = self.vista.txt_DireccionAgregarCliente.text()
        telefono = self.vista.txt_TelefonoAgregarCliente.text()
        email = self.vista.txt_EmailAgregarCliente.text()
        self.datos_clientes_confirmados.emit((cedula,nombre,apellido,localizacion,direccion,telefono,email))
        self.close()

    def boton_check_activado(self):
        if(self.vista.chb_ActivarClientesRegistrados.isChecked()):
            self.vista.lbl_Cliente.setVisible(self.vista.chb_ActivarClientesRegistrados.isChecked())
            self.vista.cmb_ClienteSeleccionar.setVisible(self.vista.chb_ActivarClientesRegistrados.isChecked())
            self.vista.txt_CedulaAgregarCliente.setEnabled(False)
            self.vista.txt_NombreAgregarCliente.setEnabled(False)
            self.vista.txt_ApellidoAgregarCliente.setEnabled(False)
            self.vista.cmb_localizacion_registro_clientes.setEnabled(False)
            self.vista.txt_DireccionAgregarCliente.setEnabled(False)
            self.vista.txt_TelefonoAgregarCliente.setEnabled(False)
            self.vista.txt_EmailAgregarCliente.setEnabled(False)
        else:
            self.vista.lbl_Cliente.setVisible(False)
            self.vista.cmb_ClienteSeleccionar.setVisible(False)
            self.vista.txt_CedulaAgregarCliente.setEnabled(True)
            self.vista.txt_NombreAgregarCliente.setEnabled(True)
            self.vista.txt_ApellidoAgregarCliente.setEnabled(True)
            self.vista.cmb_localizacion_registro_clientes.setEnabled(True)
            self.vista.txt_DireccionAgregarCliente.setEnabled(True)
            self.vista.txt_TelefonoAgregarCliente.setEnabled(True)
            self.vista.txt_EmailAgregarCliente.setEnabled(True)
    
    def actualizar_cmbs(self):
        manejoDB = ManejoDB()
        localizaciones = manejoDB.consultar('SELECT * FROM localizacion;')
        for localizacion in localizaciones:
            self.vista.cmb_localizacion_registro_clientes.addItem(str(localizacion[0]) + '-' +localizacion[1] + ' - ' + localizacion[2])
        clientes = manejoDB.consultar('SELECT cliente.id FROM cliente;')
        for cliente in clientes:
            self.vista.cmb_ClienteSeleccionar.addItem(str(cliente[0]))

    def llenar_campos_cliente(self):
        manejoDB = ManejoDB()
        id_cliente = self.vista.cmb_ClienteSeleccionar.currentText()
        cliente = manejoDB.consultar(f"SELECT * FROM cliente WHERE id = '{id_cliente}';")[0]
        self.vista.txt_CedulaAgregarCliente.setText(cliente[0])
        self.vista.txt_NombreAgregarCliente.setText(cliente[1])
        self.vista.txt_ApellidoAgregarCliente.setText(cliente[2])
        localizacion = cliente[3]
        localizacion = manejoDB.consultar(f"SELECT * FROM localizacion WHERE id = '{localizacion}';")[0]
        self.vista.cmb_localizacion_registro_clientes.setCurrentText(str(localizacion[0]) + '-' +localizacion[1] + ' - ' + localizacion[2])
        self.vista.txt_DireccionAgregarCliente.setText(cliente[4])
        self.vista.txt_TelefonoAgregarCliente.setText(cliente[5])
        self.vista.txt_EmailAgregarCliente.setText(cliente[6])


        manejoDB.cerrar_conexion()
    def ocultar_clientes_cmb(self):
        self.vista.cmb_ClienteSeleccionar.setVisible(False)
        self.vista.lbl_Cliente.setVisible(False)

    def cancelar(self):
        self.close()
