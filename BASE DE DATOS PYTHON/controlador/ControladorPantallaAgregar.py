from PyQt6 import QtWidgets
from vista.RegistroAgentes import Ui_RegistroInmobilaria
from modelo.manejoDB import ManejoDB


class ControladorPantallaAgregar(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.vista = Ui_RegistroInmobilaria()
        self.vista.setupUi(self)
        self.vista.tabWidget.setCurrentIndex(0)
        self.vista.btn_RegistrarAgregarAgente.clicked.connect(self.agregar_agente)
        self.vista.btn_ModificarCliente.clicked.connect(self.modificar_cliente)
        self.vista.btn_ModificarInmueble.clicked.connect(self.modificar_inmueble)
        self.vista.btn_Regresar.clicked.connect(self.regresar)
        self.vista.cmb_CedulaModificarCliente.currentTextChanged.connect(self.cargar_datos_modificar_cliente)
        self.actualizar_tabla_agentes()
        self.actualizar_tabla_clientes()
        self.actualizar_tabla_inmuebles()
        self.actualizar_cmbs()

    def agregar_agente(self):
        manejoDB = ManejoDB()
        cedula = self.vista.txt_CedulaAgregarAgente.text()
        nombre = self.vista.txt_NombreAgregarAgente.text()
        apellido = self.vista.txt_ApellidoAgregarAgente.text()
        localizacion = self.vista.cmb_localizacion_registro_agentes.currentText().split('-')[0]
        direccion = self.vista.txt_DireccionAgregarAgente.text()
        telefono = self.vista.txt_TelefonoAgregarAgente.text()
        email = self.vista.txt_EmailAgregarAgente.text()
        manejoDB.insertar_en('agente',('cedula','nombre','apellido','localizacion','direccion','telefono','email'),(cedula,nombre,apellido,localizacion,direccion,telefono,email))
        self.actualizar_tabla_agentes()

    # def cargar_datos_modificar(self):
    #     try:
    #         self.vista.txt_NombreModificarCliente.setText(#Aqui va el nombre del clientxe )
    #         self.vista.txt_ApellidoModificarCliente.setText(self.manejo_laboratorios.contenedor_laboratorios[self.ui.cmb_LaboratorioModificar.currentText().split(" : ")[0]].capacidad)
    #         self.vista.txt_CiudadModificarCliente.setText(self.manejo_laboratorios.contenedor_laboratorios[self.ui.cmb_LaboratorioModificar.currentText().split(" : ")[0]].software)
    #         self.vista.txt_CiudadModificarInmueble.setCurrentText(self.manejo_laboratorios.contenedor_laboratorios[self.ui.cmb_LaboratorioModificar.currentText().split(" : ")[0]].campus)
    #         self.vista.txt_DireccionModificarCliente.setText(self.manejo_laboratorios.contenedor_laboratorios[self.ui.cmb_LaboratorioModificar.currentText().split(" : ")[0]].precio)
    #         self.vista.txt_TelefonoModificarCliente.setText(self.manejo_laboratorios.contenedor_laboratorios[self.ui.cmb_LaboratorioModificar.currentText().split(" : ")[0]].pisos)
    #         self.vista.txt_EmailModificarCliente.setText(self.manejo_laboratorios.contenedor_laboratorios[self.ui.cmb_LaboratorioModificar.currentText().split(" : ")[0]].cuartos)
    #     except KeyError:
    #         return

    def modificar_cliente(self):
        manejoDB = ManejoDB()
        cedula = self.vista.cmb_CedulaModificarCliente.currentText()
        nombre = self.vista.txt_NombreModificarCliente.text()
        apellido = self.vista.txt_ApellidoModificarCliente.text()
        localizacion = self.vista.cmb_localizacion_mod_cliente.currentText().split('-')[0]
        direccion = self.vista.txt_DireccionModificarCliente.text()
        telefono = self.vista.txt_TelefonoModificarCliente.text()
        email = self.vista.txt_EmailModificarCliente.text()
        manejoDB.actualizar_en('cliente',('nombre','apellido','localizacion','direccion','telefono','email'),(nombre,apellido,localizacion,direccion,telefono,email),f'{self.vista.cmb_CedulaModificarCliente.currentText()}')
        self.actualizar_tabla_clientes()

    def modificar_inmueble(self):
        
        manejoDB = ManejoDB()
        tipo = self.vista.cmb_TipoModificarInmbueble.currentText()
        direccion = self.vista.txt_DireccionModificarInmueble.text()
        localizacion = self.vista.cmb_localizacion_mod_inmueble.currentText().split('-')[0]
        precio = self.vista.txt_PrecioModificarInmueble.text()
        pisos = self.vista.txt_PisosModificarInmueble.text()
        cuartos = self.vista.txt_CuartosModificarInmueble.text()
        anio_construccion = self.vista.txt_AnioConsModificarInmueble.text()
        piscina = self.vista.cmb_PiscinaModificarInmueble.currentIndex()
        if piscina == 0:
            piscina = True
        else:
            piscina = False
        area = self.vista.txt_AreaModificarInmueble.text()
        banios = self.vista.txt_BaniosModificarInmueble.text()
        parqueadero = self.vista.cmb_EstacionamientoModificarInmueble.currentIndex()
        if parqueadero == 0:
            parqueadero = True
        else:
            parqueadero = False
        otras_Carac = self.vista.txt_OtrasCaracModificarInmueble.text()
        manejoDB.actualizar_en('inmueble',('tipo','direccion','localizacion','precio','num_de_pisos','num_de_cuartos','anio_de_construccion','piscina','area','num_de_banos','estacionamiento','descripcion'),(tipo,direccion,localizacion,precio,pisos,cuartos,anio_construccion,piscina,area,banios,parqueadero,otras_Carac),f'{self.vista.cmb_IDModificarInmbueble.currentText()}')
        print(localizacion)
        self.actualizar_tabla_inmuebles()

    def actualizar_tabla_agentes(self):
        try:
            manejoDB = ManejoDB()
            self.vista.tbl_agentes.setRowCount(0)
            agentes = manejoDB.consulta_general('agente','*')
            for agente in agentes:
                rowPosition = self.vista.tbl_agentes.rowCount()
                self.vista.tbl_agentes.insertRow(rowPosition)
                self.vista.tbl_agentes.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(agente[0]))
                self.vista.tbl_agentes.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(agente[1]))
                self.vista.tbl_agentes.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(agente[2]))
                localizacion = manejoDB.consultar(f"SELECT * FROM localizacion WHERE id = '{agente[3]}'")
                self.vista.tbl_agentes.setItem(rowPosition , 3, QtWidgets.QTableWidgetItem(localizacion[0][1] + '-' + localizacion[0][2]))
                self.vista.tbl_agentes.setItem(rowPosition , 4, QtWidgets.QTableWidgetItem(agente[4]))
                self.vista.tbl_agentes.setItem(rowPosition , 5, QtWidgets.QTableWidgetItem(agente[5]))
                self.vista.tbl_agentes.setItem(rowPosition , 6, QtWidgets.QTableWidgetItem(agente[6]))
            manejoDB.cerrar_conexion()
        except Exception as e:
            print(e)
    
    def actualizar_tabla_clientes(self):
        try:
            manejoDB = ManejoDB()
            self.vista.tbl_clientes_general.setRowCount(0)
            clientes = manejoDB.consulta_general('cliente','*')
            for cliente in clientes:
                rowPosition = self.vista.tbl_clientes_general.rowCount()
                self.vista.tbl_clientes_general.insertRow(rowPosition)
                self.vista.tbl_clientes_general.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(cliente[0]))
                self.vista.tbl_clientes_general.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(cliente[1]))
                self.vista.tbl_clientes_general.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(cliente[2]))
                localizacion = manejoDB.consultar(f"SELECT * FROM localizacion WHERE id = '{cliente[3]}'")
                self.vista.tbl_clientes_general.setItem(rowPosition , 3, QtWidgets.QTableWidgetItem(localizacion[0][1] + '-' + localizacion[0][2]))
                self.vista.tbl_clientes_general.setItem(rowPosition , 4, QtWidgets.QTableWidgetItem(cliente[4]))
                self.vista.tbl_clientes_general.setItem(rowPosition , 5, QtWidgets.QTableWidgetItem(cliente[5]))
                self.vista.tbl_clientes_general.setItem(rowPosition , 6, QtWidgets.QTableWidgetItem(cliente[6]))
            manejoDB.cerrar_conexion()
        except Exception as e:
            print(e)
    
    def actualizar_tabla_inmuebles(self):
        try:
            manejoDB = ManejoDB()
            self.vista.tbl_inmuebles.setRowCount(0)
            inmuebles = manejoDB.consultar('SELECT * FROM inmueble JOIN localizacion ON inmueble.localizacion = localizacion.id')
            for inmueble in inmuebles:
                rowPosition = self.vista.tbl_inmuebles.rowCount()
                self.vista.tbl_inmuebles.insertRow(rowPosition)
                self.vista.tbl_inmuebles.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(str(inmueble[0])))
                self.vista.tbl_inmuebles.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(inmueble[1]))
                self.vista.tbl_inmuebles.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(inmueble[2]))
                self.vista.tbl_inmuebles.setItem(rowPosition , 3, QtWidgets.QTableWidgetItem(inmueble[14] + '-' + inmueble[15]))
                self.vista.tbl_inmuebles.setItem(rowPosition , 4, QtWidgets.QTableWidgetItem(str(inmueble[4])))
                self.vista.tbl_inmuebles.setItem(rowPosition , 5, QtWidgets.QTableWidgetItem(inmueble[5]))
                self.vista.tbl_inmuebles.setItem(rowPosition , 6, QtWidgets.QTableWidgetItem(str(inmueble[6])))
                self.vista.tbl_inmuebles.setItem(rowPosition , 7, QtWidgets.QTableWidgetItem(str(inmueble[7])))
                self.vista.tbl_inmuebles.setItem(rowPosition , 8, QtWidgets.QTableWidgetItem(str(inmueble[8])))
                self.vista.tbl_inmuebles.setItem(rowPosition , 9, QtWidgets.QTableWidgetItem(str(inmueble[9])))
                self.vista.tbl_inmuebles.setItem(rowPosition , 10, QtWidgets.QTableWidgetItem(str(inmueble[10])))
                self.vista.tbl_inmuebles.setItem(rowPosition , 11, QtWidgets.QTableWidgetItem(str(inmueble[11])))
                self.vista.tbl_inmuebles.setItem(rowPosition , 12, QtWidgets.QTableWidgetItem(str(inmueble[12])))
        except Exception as e:
            print(e)
    def actualizar_cmbs(self):
        #actualizar localizaciones
        manejoDB = ManejoDB()
        localizaciones = manejoDB.consultar('SELECT * FROM localizacion')
        for localizacion in localizaciones:
            self.vista.cmb_localizacion_mod_inmueble.addItem(str(localizacion[0]) + '-' + localizacion[1] + '-' + localizacion[2])
            self.vista.cmb_localizacion_registro_agentes.addItem(str(localizacion[0]) + '-' + localizacion[1] + '-' + localizacion[2])
            self.vista.cmb_localizacion_mod_cliente.addItem(str(localizacion[0]) + '-' + localizacion[1] + '-' + localizacion[2])
        inmuebles = manejoDB.consultar('SELECT inmueble.id FROM inmueble')
        for inmueble in inmuebles:
            self.vista.cmb_IDModificarInmbueble.addItem(str(inmueble[0]))
        #actualizar cedulas
        clientes = manejoDB.consultar('SELECT cliente.id FROM cliente')
        for cliente in clientes:
            self.vista.cmb_CedulaModificarCliente.addItem(str(cliente[0]))
        manejoDB.cerrar_conexion()

    def cargar_datos_modificar_cliente(self):
        manejoDB = ManejoDB()
        cedula = self.vista.cmb_CedulaModificarCliente.currentText()
        datos_cliente = manejoDB.consultar(f"SELECT * FROM cliente WHERE id = '{cedula}'")
        localizacion = manejoDB.consultar(f"SELECT * FROM localizacion WHERE id = '{datos_cliente[0][3]}'")
        self.vista.txt_NombreModificarCliente.setText(datos_cliente[0][1])
        self.vista.txt_ApellidoModificarCliente.setText(datos_cliente[0][2])

        self.vista.cmb_localizacion_mod_cliente.setCurrentText(str(localizacion[0][0]) + '-' + localizacion[0][1] + '-' + localizacion[0][2])
        self.vista.txt_DireccionModificarCliente.setText(datos_cliente[0][4])
        self.vista.txt_TelefonoModificarCliente.setText(datos_cliente[0][5])
        self.vista.txt_EmailModificarCliente.setText(datos_cliente[0][6])

       
    
    def regresar(self):
        self.close()
