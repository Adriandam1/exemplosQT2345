import sys
from ModeloListaTarefas import ModeloTarefas

from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QListView, QHBoxLayout, QPushButton, QLineEdit, QWidget, \
    QApplication


class ExemploQListView (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplo QListView")
        listaTarefas = [(True, 'Ir al gimnasio'),(False,"hacer la compra")]
        self.modelo = ModeloTarefas(listaTarefas)

        caixaV = QVBoxLayout()

        self.lstTarefas = QListView()
        self.lstTarefas.setModel(self.modelo)
        self.lstTarefas.setSelectionMode(QListView.SelectionMode.MultiSelection)
        caixaV.addWidget(self.lstTarefas)

        caixaHBotons = QHBoxLayout()
        btnborrar = QPushButton("Borrar")
        btnborrar.pressed.connect(self.on_btnBorrar_pressed)

        btnFeito = QPushButton('Feito')
        btnFeito.pressed.connect(self.on_btnFeito_pressed)

        caixaHBotons.addWidget(btnborrar)
        caixaHBotons.addWidget(btnFeito)
        caixaV.addLayout(caixaHBotons)

        self.txtTarefa = QLineEdit()
        caixaV.addWidget(self.txtTarefa)

        btnEngadirTarefa = QPushButton("Engadir Tarefa")
        btnEngadirTarefa.pressed.connect(self.on_btnEngadirTarefa_pressed)
        caixaV.addWidget(btnEngadirTarefa)

        container = QWidget()
        container.setLayout(caixaV)
        self.setCentralWidget(container)
        self.setFixedSize(400, 300)
        self.show()

    def on_btnEngadirTarefa_pressed(self):
        texto = self.txtTarefa.text().strip()
        if texto:
            self.modelo.tarefas.append((False, texto))
            self.modelo.layoutChanged.emit()
            self.txtTarefa.clear()

    def on_btnBorrar_pressed(self):
        indices = self.lstTarefas.selectedIndexes()
        if indices:
            for indice in sorted (indices, reverse = True):
                print (indice.row())
                del self.modelo.tarefas [indice.row()]

            self.modelo.layoutChanged.emit()
            self.lstTarefas.clearSelection()

    def on_btnFeito_pressed(self):
        indices = self.lstTarefas.selectedIndexes()
        if indices:
            for indice in indices:
                _ , texto = self.modelo.tarefas [indice.row()]
                self.modelo.tarefas [indice.row()] = (True, texto)
            self.modelo.dataChanged.emit(indice,indice)
            self.lstTarefas.clearSelection()


if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    ventana = ExemploQListView()
    aplicacion.exec()