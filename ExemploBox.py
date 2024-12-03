import sys
from PyQt6.QtGui  import QColor, QPalette
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QMainWindow, QBoxLayout, QHBoxLayout, QApplication


class CaixaColor (QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(paleta)


class ExemploBox (QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("ExemploBox ")
        self.setMinimumSize(300, 200)
        self.setMaximumSize(400,300)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("aquaMarine"))
        self.setPalette(paleta)

        caixaH = QHBoxLayout()

        caixaV1 = QVBoxLayout()
        caixaV1.addWidget(CaixaColor("blue"))
        caixaV1.addWidget(CaixaColor("green"))
        caixaV1.addWidget(CaixaColor("pink"))

        caixaH.addLayout(caixaV1)
        caixaH.addWidget(CaixaColor("green"))
        caixaV2 = QVBoxLayout()
        caixaV2.addWidget(CaixaColor("yellow"))
        caixaV2.addWidget(CaixaColor("grey"))

        caixaH.addLayout(caixaV2)


        container = QWidget()
        container.setLayout(caixaH)
        self.setCentralWidget(container)
        self.show()





if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = ExemploBox()
    aplicacion.exec()