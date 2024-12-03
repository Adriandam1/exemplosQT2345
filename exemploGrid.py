import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel

from CaixaCor import CaixaCor
from LayoutBox import LayoutBox


class FiestraPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplo Grid Layout con Qt")

        maia = QGridLayout()
        maia.addWidget(CaixaCor("red"))
        maia.addWidget(CaixaCor("blue"), 0, 1, 1, 2)
        maia.addWidget (CaixaCor("green"), 1,0, 2, 1)
        maia.addWidget(CaixaCor ("pink"), 1,1,1,2)
        maia.addWidget (CaixaCor ("orange"), 2, 1, 1, 1)
        maia.addWidget(CaixaCor ("yellow"), 2, 2, 1,1)
        maia.addLayout(LayoutBox(), 3,0, 3, 3)

        control = QWidget()
        control.setLayout(maia)
        self.setCentralWidget(control)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    app.exec()
