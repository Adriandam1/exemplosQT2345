import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QListView, QHBoxLayout, QPushButton, QLineEdit, QWidget, \
    QApplication, QTableView, QComboBox, QCheckBox, QGridLayout, QLabel

from ModeloTaboa import ModeloTaboa
from conexionBD import ConexionBD

# Paxina doc: https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QTableView.html
# grid layout: https://doc.qt.io/qt-6/qgridlayout.html
# qwidget setEnable/disable (activar desactivar botones): https://doc.qt.io/qt-6/qwidget.html#enabled-prop

class ExemploQTableViewHORIZONTAL(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplo QTableView - HORIZONTAL")

        """
        datos =[ ['Nome', 'Dni', 'Xenero', 'Falecido'],
                      ['Ana Pérez', '54321111L', 'Muller', False],
                      ['Paco Porras', '12345679P', 'Home', True],
                      ['Roque Vila', '33333333M', 'Outro', False],
                      ['Lina Saiz', '4444444Q', 'Muller', False]]
        """
        bDatos = ConexionBD("usuarios.bd")
        bDatos.conectaBD()
        bDatos.creaCursor()
        datos = bDatos.consultaSenParametros("SELECT * FROM usuarios")
        print (datos)
        # borramos caixaV y hacermos caixaH
        #caixaH = QVBoxLayout()
        caixaH = QHBoxLayout()
        self.tvwTaboa = QTableView()
        if datos is None:
            self.modelo = ModeloTaboa()
        else:
            self.modelo = ModeloTaboa (datos)
        self.tvwTaboa.setModel(self.modelo)
        # lle asignamos un evento(estamos para que cuando cambiemos manualmente las columnas se guarde)
        # en suspenso no funciona self.tvwTaboa.cellChanged.connect(self.on_tvwTaboa_itemChanged)
        self.tvwTaboa.setSelectionMode (QTableView.SelectionMode.SingleSelection)
        # Minimun size da taboa
        self.tvwTaboa.setMinimumSize(400, 200)
        #cabeceira = self.tvwTaboa.horizontalHeader()
        self.seleccion = self.tvwTaboa.selectionModel()
        self.seleccion.selectionChanged.connect (self.on_tvwTaboa_selectionChanged)

        caixaH.addWidget(self.tvwTaboa)
        caixa = QHBoxLayout()
        caixa.addWidget(self.tvwTaboa)
        # Haciendo cambios para hacer la tabla horizontal
        # vamos a utilizar un grid
        maia = QGridLayout()
        caixaH.addLayout(maia)

        #Creariamos unha etiqueta nome, dni xenero
        self.lblNome = QLabel ("Nome")
        self.txtNome = QLineEdit()

        self.lblDni = QLabel("Dni")
        self.txtDni = QLineEdit()

        self.lblXenero = QLabel("Xenero")
        self.cmbXenero = QComboBox()
        self.cmbXenero.addItems(('Home','Muller', 'Outro'))
        self.cmbXenero.setCurrentIndex(-1)
        self.chkFalecido = QCheckBox('Falecido')

        self.btnNovo = QPushButton("Novo")
        self.btnNovo.clicked.connect(self.on_btnNovo_clicked)
        # Creamos 2 botons novos, modificar Y borrar
        self.btnModificar = QPushButton("Modificar")
        self.btnBorrar = QPushButton("Borrar")


        self.btnAceptar = QPushButton ("Aceptar")
        self.btnAceptar.clicked.connect (self.on_btnAceptar_clicked)
        self.btnCancelar = QPushButton ("Cancelar")
        self.btnCancelar.clicked.connect (self.on_btnCancelar_clicked)

        # COLOCACION dos elementos

        #indicamos onde queremos poñer os widgets(posicion)
        # documentacion: https://doc.qt.io/qt-6/qgridlayout.html
        # os numeros estan marcando a posicion dos widgets
        # fila, columna
        maia.addWidget(self.lblNome, 0, 0, 1, 1)
        maia.addWidget(self.txtNome, 0, 1, 1, 1)
        maia.addWidget(self.lblXenero, 0, 2, 1, 1)
        maia.addWidget(self.cmbXenero, 0, 3, 1, 1)
        maia.addWidget(self.lblDni, 1, 0, 1, 1)
        maia.addWidget(self.txtDni, 1, 1, 1, 1)
        maia.addWidget(self.chkFalecido, 1, 2, 1, 1)

        # Agora serian os botons
        maia.addWidget(self.btnNovo, 2, 0, 1, 4)
        maia.addWidget(self.btnModificar, 3, 0, 1, 2)
        maia.addWidget(self.btnBorrar, 3, 2, 1, 2)

        # Creamos unha caixa para botons aceptar/cancelar
        caixaBotons = QHBoxLayout()
        caixaBotons.addWidget(self.btnAceptar)
        caixaBotons.addWidget(self.btnCancelar)
        maia.addLayout(caixaBotons, 4, 2, 1, 2)

        # maia.addWidget(btnAceptar, 4, 2, 1, 1)
        # maia.addWidget(btnCancelar, 4, 3, 1, 1)

        container = QWidget()
        container.setLayout(caixaH)
        self.setCentralWidget(container)
        # fixar o tamaño da ventana
        self.setFixedSize(850, 300)

        self.bloquearControisEdicion(True)
        self.bloquearBotonsAceptarCancelar(True)

        self.show()

    def on_tvwTaboa_selectionChanged(self):
        indice = self.tvwTaboa.selectedIndexes()
        if indice != []:
            self.txtNome.setText(self.modelo.taboa[indice[0].row()][0])
            self.txtDni.setText(self.modelo.taboa[indice[0].row()][1])
            for i in range (self.cmbXenero.count()):

                if self.modelo.taboa [indice[0].row()][2] == self.cmbXenero.itemData(i,Qt.ItemDataRole.DisplayRole):
                    self.cmbXenero.setCurrentIndex(i)

            if self.modelo.taboa [indice[0].row()][3]:
                self.chkFalecido.setChecked(True)
            else:
                self.chkFalecido.setChecked(False)
    def on_btnNovo_clicked (self):
        #desbloquear controles edicion
        self.bloquearControisEdicion(False)
        self.bloquearBotonsAceptarCancelar(False)
        self.bloquearBotonsProcesos(False)

        if self.txtNome.text() == '' or self.txtDni.text() == '' or self.cmbXenero.currentIndex() == -1:
            print("Faltan datos")
        else:
            novo = (self.txtNome.text(),self.txtDni.text(),self.cmbXenero.currentText(), True if self.chkFalecido.isChecked() else False)
            self.modelo.taboa.append( novo )
            bDatos = ConexionBD("usuarios.bd")
            bDatos.conectaBD()
            bDatos.creaCursor()
            print (novo)
            bDatos.consultaConParametros("""Insert into usuarios Values (?,?,?,?)""", novo[0], novo[1], novo[2],1 if novo[3] else 0)
            datos = bDatos.consultaSenParametros("SELECT * FROM usuarios")
            print (datos)
            bDatos.conexion.commit()
            bDatos.pechaBD()


            self.modelo.layoutChanged.emit()
            self.txtNome.clear()
            self.txtDni.clear()
            self.cmbXenero.setCurrentIndex(-1)
            self.chkFalecido.setChecked(False)

    def on_btnAceptar_clicked(self):
        indice = self.tvwTaboa.selectedIndexes()
        if indice != []:

            if self.txtNome.text() == '' or self.txtDni.text() == '' or self.cmbXenero.currentIndex() == -1:
                print ("Faltan datos")
            else:
                self.modelo.taboa[indice[0].row()][0] = self.txtNome.text()
                self.modelo.taboa[indice[0].row()][1] = self.txtDni.text()
                self.modelo.taboa[indice[0].row()][2] = self.cmbXenero.currentText()
                self.modelo.taboa[indice[0].row()][3] = True if self.chkFalecido.isChecked() else False
                self.modelo.layoutChanged.emit()
                self.txtNome.clear()
                self.txtDni.clear()
                self.cmbXenero.setCurrentIndex(-1)
                self.chkFalecido.setChecked(False)

    def on_btnCancelar_clicked(self):
        self.txtNome.clear()
        self.txtDni.clear()
        self.cmbXenero.setCurrentIndex (-1)
        self.chkFalecido.setChecked(False)

        # bloqueo / desbloqueo dos controis
        self.bloquearControisEdicion(True)
        self.bloquearBotonsAceptarCancelar(True)
        self.bloquearBotonsProcesos(False)

# funciones para bloquear/desbloquear botones con un boolean

    def bloquearControisEdicion(self, estado):
        self.lblNome.setDisabled(estado)
        self.txtNome.setDisabled(estado)
        self.lblXenero.setDisabled(estado)
        self.cmbXenero.setDisabled(estado)
        self.lblDni.setDisabled(estado)
        self.txtDni.setDisabled(estado)
        self.chkFalecido.setDisabled(estado)
        print("controles edicion bloqueados "+str(estado))

    def bloquearBotonsAceptarCancelar(self, estado):
        self.btnAceptar.setDisabled(estado)
        self.btnCancelar.setDisabled(estado)
        print("botons aceptar/cancelar bloqueados " + str(estado))

    def bloquearBotonsProcesos(self, estado):
        self.btnModificar.setDisabled(estado)
        self.btnNovo.setDisabled(estado)
        self.btnBorrar.setDisabled(estado)
        print("botons procesos bloqueados " + str(estado))




if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = ExemploQTableViewHORIZONTAL()
    aplicacion.exec()
