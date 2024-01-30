from PyQt6 import QtWidgets
from vista.RegistroInmobilario import Ui_RegistroInmobilario
from controlador.ControladorPantallaRegistroClienteContrato import ControladorPantallaRegistroClienteContrato
from PyQt6.QtCore import pyqtSignal
from modelo.manejoDB import ManejoDB

class ControladorPantallaRegistroInmuebleContrato(QtWidgets.QMainWindow):
    datos_inmueble = pyqtSignal(tuple)
    def __init__(self):
        super().__init__()
        self.vista = Ui_RegistroInmobilario()
        self.vista.setupUi(self)
        self.vista.btn_RegistrarInmueble.clicked.connect(self.registrar_inmueble)
        self.vista.btn_CancelarContrato.clicked.connect(self.cancelar)
        self.contrato_cliente = ControladorPantallaRegistroClienteContrato()
        self.actualizar_cmbs()

    def registrar_inmueble(self):
        tipo = self.vista.cmb_TipoAgregarInmbueble.currentText()
        direccion = self.vista.txt_DireccionAgregarInmueble.text()
        ciudad = self.vista.cmb_localizacion_registro_inmuebles.currentText().split('-')[0]
        precio = self.vista.txt_PrecioAgregarInmueble.text()
        pisos = self.vista.txt_PisosAgregarInmueble.text()
        cuartos = self.vista.txt_CuartosAgregarInmueble.text()
        anio_construccion = self.vista.txt_AnioConsAgregarInmueble.text()
        piscina = self.vista.cmb_PiscinaAgregarInmueble.currentIndex()
        if piscina == 0:
            piscina = True
        else:
            piscina = False
            
        area = self.vista.txt_AreaAgregarInmueble.text()
        banios = self.vista.txt_BaniosAgregarInmueble.text()
        parqueadero = self.vista.cmb_EstacionamientoAgregarInmueble.currentIndex()
        if parqueadero == 0:
            parqueadero = True
        else:
            parqueadero = False
        otras_carac = self.vista.txt_OtrasCaracAgregarInmueble.text()
        
        self.datos_inmueble.emit((tipo,direccion,ciudad,precio,pisos,cuartos,anio_construccion,piscina,area,banios,parqueadero,otras_carac))
        self.close()
        self.contrato_cliente.show()
    def actualizar_cmbs(self):
        manejoDB = ManejoDB()
        localiazciones = manejoDB.consultar('SELECT * FROM localizacion')
        for localizacion in localiazciones:
            self.vista.cmb_localizacion_registro_inmuebles.addItem(str(localizacion[0]) + '-' + localizacion[1]+ '-' + localizacion[2])

    def cancelar(self):
        self.close()
