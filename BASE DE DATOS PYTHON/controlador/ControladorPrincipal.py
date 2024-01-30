from PyQt6 import QtWidgets
from vista.menuPrincipal import Ui_MainWindowInmobilaria
from controlador.ControladorPantallaContratos import ControladorPantallaContratos
from controlador.ControladorPantallaAgregar import ControladorPantallaAgregar
from controlador.ControladorPantallaReportes import ControladorPantallaReportes


class ControladorPrincipal(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.vista = Ui_MainWindowInmobilaria()
        self.vista.setupUi(self)
        self.vista.actionAgregar.triggered.connect(self.agregar_agente)
        self.vista.actionContratos.triggered.connect(self.contratos)
        self.vista.actionReportes.triggered.connect(self.reportes)
        self.vista.actionSalir.triggered.connect(self.salir)

    def agregar_agente(self):
        self.controlador_agregar = ControladorPantallaAgregar()
        self.controlador_agregar.show()

    def contratos(self):
        self.controlador_contratos = ControladorPantallaContratos()
        self.controlador_contratos.show()

    def reportes(self):
        self.controlador_reportes = ControladorPantallaReportes()
        self.controlador_reportes.show()

    def salir(self):
        self.close()
