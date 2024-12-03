import sys
from os import O_TRUNC

from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit)
from PyQt6.QtGui import QColor, QPalette


class OutraFiestra(QMainWindow):

    def __init__(self, fiestraPrincipal):
        super().__init__()
        self.fiestraPrincipal = fiestraPrincipal
        self.setWindowTitle("Outra fiestra ")
        self.setMinimumSize(300, 200)
        self.setMaximumSize(1000, 800)

        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("beige"))
        self.setPalette(paleta)

        caixaV = QVBoxLayout()

        self.lblEtiqueta = QLabel("Outra Fiestra")
        caixaV.addWidget(self.lblEtiqueta)

        btnFiestraPrincipal = QPushButton("Fiestra principal")
        btnFiestraPrincipal.clicked.connect(self.on_btnFiestraPrincipal_clicked)
        caixaV.addWidget(btnFiestraPrincipal)

        container = QWidget()
        container.setLayout(caixaV)
        self.setCentralWidget(container)
        self.show()

    def on_btnFiestraPrincipal_clicked(self):
        self.fiestraPrincipal.show()
        self.hide()




class DuasFiestras (QMainWindow):

    def __init__(self):
        super().__init__()
        self.outraFiestra = None
        self.setWindowTitle("Primeira fiestra ")
        self.setMinimumSize(300, 200)
        self.setMaximumSize(400,300)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("aquaMarine"))
        self.setPalette(paleta)

        caixaV = QVBoxLayout()

        self.lblEtiqueta = QLabel("Fiestra principal")
        caixaV.addWidget(self.lblEtiqueta)

        btnOutraFiestra = QPushButton("Outra fiestra")
        btnOutraFiestra.clicked.connect(self.on_btnOutraFiestra_clicked)
        caixaV.addWidget(btnOutraFiestra)

        container = QWidget()
        container.setLayout(caixaV)
        self.setCentralWidget(container)
        self.show()

    def on_btnOutraFiestra_clicked(self):
        self.outraFiestra= OutraFiestra(self)
        self.hide()

        """if self.outraFiestra == None:
            self.outraFiestra = OutraFiestra(self)
        else:
            self.outraFiestra.show()
"""



if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = DuasFiestras()
    aplicacion.exec()