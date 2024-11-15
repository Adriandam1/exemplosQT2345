import sys
from PyQt6.QtGui  import QColor, QPalette
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QMainWindow, QBoxLayout, QHBoxLayout, QApplication

from CaixaCor import CaixaCor



class LayoutBox (QHBoxLayout):

    def __init__(self):
        super().__init__()

        caixaV1 = QVBoxLayout()
        caixaV1.addWidget(CaixaCor("blue"))
        caixaV1.addWidget(CaixaCor("green"))
        caixaV1.addWidget(CaixaCor("pink"))

        self.addLayout(caixaV1)
        self.addWidget(CaixaCor("green"))
        caixaV2 = QVBoxLayout()
        caixaV2.addWidget(CaixaCor("yellow"))
        caixaV2.addWidget(CaixaCor("grey"))

        self.addLayout(caixaV2)





