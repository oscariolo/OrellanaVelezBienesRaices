from modelo.manejoDB import ManejoDB
from modelo.ReportesBienesRaices import reportes_BienesRaices
from modelo.manejoBienesRaices import manejoBienesRaices
from controlador.ControladorPantallaAgregar import ControladorPantallaAgregar
import sys
from PyQt6 import QtWidgets
from controlador.ControladorPrincipal import ControladorPrincipal

if '__main__' == __name__:
    app = QtWidgets.QApplication(sys.argv)
    controlador = ControladorPrincipal()
    controlador.show()
    app.exec()
 
    
    
    
    
    

    
    
    
    


