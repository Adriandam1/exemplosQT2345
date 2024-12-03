import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QListView, QHBoxLayout, QPushButton, QLineEdit, QWidget, \
    QApplication, QTableView, QComboBox, QCheckBox, QGridLayout, QLabel, QFrame

from ModeloTaboa import ModeloTaboa
from conexionBD import ConexionBD

class interfaz (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Interfaz Spartan")

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
        self.tvwTaboa.setSelectionMode (QTableView.SelectionMode.SingleSelection)
        # Minimun size da taboa
        self.tvwTaboa.setMinimumSize(400, 200)
        #cabeceira = self.tvwTaboa.horizontalHeader()
        self.seleccion = self.tvwTaboa.selectionModel()

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
            # Creamos 2 botons novos, modificar Y borrar
        self.btnModificar = QPushButton("Modificar")
        self.btnBorrar = QPushButton("Borrar")


        self.btnAceptar = QPushButton ("Aceptar")
        self.btnCancelar = QPushButton ("Cancelar")


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


        self.show()


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = interfaz()
    aplicacion.exec()
























