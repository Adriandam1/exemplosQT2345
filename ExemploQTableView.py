import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QListView, QHBoxLayout, QPushButton, QLineEdit, QWidget, \
    QApplication, QTableView, QComboBox, QCheckBox

from ModeloTaboa import ModeloTaboa
from conexionBD import ConexionBD




class ExemploQTableView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplo QTableView")

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
        caixaV = QVBoxLayout()
        self.tvwTaboa = QTableView()
        if datos is None:
            self.modelo = ModeloTaboa()
        else:
            self.modelo = ModeloTaboa (datos)
        self.tvwTaboa.setModel(self.modelo)
        self.tvwTaboa.setSelectionMode (QTableView.SelectionMode.SingleSelection)
        #cabeceira = self.tvwTaboa.horizontalHeader()
        self.seleccion = self.tvwTaboa.selectionModel()
        self.seleccion.selectionChanged.connect (self.on_tvwTaboa_selectionChanged)

        
        caixaV.addWidget(self.tvwTaboa)

        caixaH = QHBoxLayout()
        caixaV.addLayout(caixaH)
        self.txtNome = QLineEdit()
        caixaH.addWidget(self.txtNome)
        self.txtDni = QLineEdit()
        caixaH.addWidget(self.txtDni)
        self.cmbXenero = QComboBox()
        self.cmbXenero.addItems(('Home','Muller', 'Outro'))
        self.cmbXenero.setCurrentIndex(-1)
        caixaH.addWidget(self.cmbXenero)
        self.chkFalecido = QCheckBox('Falecido')
        caixaH.addWidget(self.chkFalecido)

        caixaH2 = QHBoxLayout()
        btnNovo = QPushButton("Novo")
        btnNovo.clicked.connect(self.on_btnNovo_clicked)
        caixaH2.addWidget(btnNovo)
        caixaV.addLayout(caixaH2)

        caixaH3 = QHBoxLayout()
        btnAceptar = QPushButton ("Aceptar")
        btnAceptar.clicked.connect (self.on_btnAceptar_clicked)
        caixaH3.addWidget(btnAceptar)
        btnCancelar = QPushButton ("Cancelar")
        btnCancelar.clicked.connect (self.on_btnCancelar_clicked)
        caixaH3.addWidget(btnCancelar)
        caixaV.addLayout(caixaH3)


        container = QWidget()
        container.setLayout(caixaV)
        self.setCentralWidget(container)
        self.setFixedSize(400, 300)
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
                self.modelo.taboa [indice[0].row()][0] = self.txtNome.text()
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

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = ExemploQTableView()
    aplicacion.exec()
