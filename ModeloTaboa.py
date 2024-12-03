from PyQt6 import QtGui
from PyQt6.QtCore import QAbstractTableModel, Qt

# paxina doc: https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QTableView.html

class ModeloTaboa (QAbstractTableModel):
    def __init__(self, taboa = None):
        super().__init__()
        self.taboa = taboa

    def rowCount (self, indice):
        return len (self.taboa)

    def columnCount(self, indice):
        return len (self.taboa[0]) if len (self.taboa) != 0 else 0

    def data (self, indice, rol):
        if rol == Qt.ItemDataRole.DisplayRole or rol== Qt.ItemDataRole.EditRole:
            valor = self.taboa [indice.row()][indice.column()]
            return valor
        if rol == Qt.ItemDataRole.BackgroundRole:
            if self.taboa[indice.row()][2] == "Home":
                return QtGui.QColor ('pink')
            elif self.taboa [indice.row()][2] == "Muller":
                return QtGui.QColor ('lightblue')
            elif self.taboa [indice.row()][2] == "Outro":
                return QtGui.QColor ("orange")
        if rol == Qt.ItemDataRole.ForegroundRole:
            if self.taboa[indice.row()][3] == True:
                if (indice.column()==3):
                    return QtGui.QColor ("red")

        if rol == Qt.ItemDataRole.DecorationRole:
            if isinstance (self.taboa[indice.row()][indice.column()], bool):
                if self.taboa[indice.row()][indice.column()]:
                    return QtGui.QIcon ('tick.png')

# temos que crear un novo metodo permitiranos facer un cambio na columna nome e columna vivo/morto
# columna 1 = dni
    def flags (self, indice):
        if indice.column() == 1:
            # si es la fila 1(dni) permitimos el item
            # esto seria como has caracteristicas da celda
            return Qt.ItemFlag.ItemIsEnabled
            # si es el resto permitimos que sea editable selectable
        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsSelectable
        # Con esto las columnas que queramos seran editables ( Exemplo QTableView) pero de momento no le hemos dicho al view que lo mande a la base de datos
        # por lo que los cambios no son efectivos, ahora tenemos que buscar cual es el evento que nos permite hacer ese tipo de cambios
