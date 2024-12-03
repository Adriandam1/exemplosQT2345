import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel, QStackedLayout, QVBoxLayout, \
    QHBoxLayout, QPushButton, QTabWidget, QComboBox

from CaixaCor import CaixaCor
from LayoutBox import LayoutBox


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplo QTabWidget con Qt")

        caixaV = QVBoxLayout()

        self.clasificador = QTabWidget()
        caixaV.addWidget(self.clasificador)
        self.clasificador.setTabPosition(QTabWidget.TabPosition.West)

        self.clasificador.addTab (CaixaCor("red"),"Vermello")
        self.clasificador.addTab (CaixaCor ("blue"), "Azul")
        self.clasificador.addTab(CaixaCor("green"),"Verde")
        widgetBox = QWidget()
        widgetBox.setLayout(LayoutBox())
        self.clasificador.addTab(widgetBox, "Formulario con box")

        cmbCores = QComboBox()
        cmbCores.addItems(("Vermello", "Azul", "Verde","Formulario"))
        cmbCores.currentIndexChanged.connect(self.on_cmbCores_currentIndexChanged)
        caixaV.addWidget(cmbCores)

        control = QWidget()
        control.setLayout(caixaV)
        self.setCentralWidget(control)
        self.show()

    def on_cmbCores_currentIndexChanged(self, i):
        self.clasificador.setCurrentIndex(i)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    app.exec()
