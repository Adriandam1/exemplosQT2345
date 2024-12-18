import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel, QStackedLayout, QVBoxLayout, \
    QHBoxLayout, QPushButton, QRadioButton, QButtonGroup, QCheckBox, QComboBox

from CaixaCor import CaixaCor
from LayoutBox import LayoutBox


class FiestraPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplo QStackedLayout con Qt")
        caixaV = QVBoxLayout()

        self.stack = QStackedLayout()
        caixaV.addLayout(self.stack)
        self.stack.addWidget(CaixaCor("red"))
        self.stack.addWidget(CaixaCor("blue"))
        self.stack.addWidget(CaixaCor("green"))
        self.stack.addWidget(CaixaCor("orange"))
        self.stack.addWidget(CaixaCor("purple"))
        self.stack.addWidget(CaixaCor("violet")) # 6
        self.stack.addWidget(CaixaCor("aquamarine"))
        self.stack.addWidget(CaixaCor("olive"))
        self.stack.addWidget(CaixaCor("brown")) # 9
        self.stack.addWidget(CaixaCor("lightred"))

        control = QWidget()
        control.setLayout(LayoutBox())
        self.stack.addWidget(control)

        self.stack.setCurrentIndex(2)

        caixaH = QHBoxLayout()
        caixaV.addLayout(caixaH)
        self.botonVermello = QPushButton("Vermello")
        caixaH.addWidget(self.botonVermello)
        self.botonAzul = QPushButton("Azul")
        caixaH.addWidget(self.botonAzul)
        self.botonVerde = QPushButton("Verde")
        caixaH.addWidget(self.botonVerde)
        self.botonLaranxa = QPushButton("Laranxa")
        caixaH.addWidget(self.botonLaranxa)
        self.botonVermello.pressed.connect(self.on_Boton_Vermello)
        self.botonAzul.pressed.connect(self.on_Boton_Azul)
        self.botonVerde.pressed.connect(self.on_Boton_Verde)
        self.botonLaranxa.pressed.connect(self.on_Boton_Laranxa)

        caixaHRButton= QHBoxLayout()
        caixaV.addLayout (caixaHRButton)
        rbtVermello= QRadioButton("Vermello")
        rbtVermello.clicked.connect(self.on_rbtVermello_clicked)
        caixaHRButton.addWidget (rbtVermello)
        rbtVerde = QRadioButton("Verde")
        rbtVerde.clicked.connect(self.on_rbtVerde_clicked)
        caixaHRButton.addWidget(rbtVerde)
        rbtVerde.click()
        rbtAzul = QRadioButton("Azul")
        rbtAzul.clicked.connect(self.on_rbtAzul_clicked)
        caixaHRButton.addWidget(rbtAzul)
        rbtLaranxa = QRadioButton("Laranxa")
        rbtLaranxa.clicked.connect(self.on_rbtLaranxa_clicked)
        caixaHRButton.addWidget(rbtLaranxa)
        rbtGrupo = QButtonGroup()
        rbtGrupo.addButton(rbtVermello)
        rbtGrupo.addButton(rbtVerde)
        rbtGrupo.addButton(rbtAzul)
        rbtGrupo.addButton(rbtLaranxa)

        caixaHCButton = QHBoxLayout()
        caixaV.addLayout(caixaHCButton)
        self.chkVermello = QCheckBox("Vermello")
        caixaHCButton.addWidget(self.chkVermello)
        self.chkVermello.clicked.connect(self.on_chkVermello_clicked)
        self.chkVerde = QCheckBox("Verde")
        caixaHCButton.addWidget(self.chkVerde)
        self.chkVerde.clicked.connect(self.on_chkVerde_clicked)
        self.chkAzul = QCheckBox("Azul")
        caixaHCButton.addWidget(self.chkAzul)
        self.chkAzul.clicked.connect(self.on_chkAzul_clicked)
        self.chkLaranxa = QCheckBox("Laranxa")
        caixaHCButton.addWidget(self.chkLaranxa)

        # aplicamos QComboBox nos permite pasar unha lista cos items addItems
        # enlace: https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QComboBox.html
        # setCurrentIndex da a opcion de ponerlle un indice
        cmbCores = QComboBox()
        cmbCores.addItems(("Vermello","Azul","Verde","Laranxa")) # pasamos como unha lista
        cmbCores.setCurrentIndex(2) # poñemos o indice 2 que é o verde por defecto
        cmbCores.currentIndexChanged.connect(self.on_cmbCores_currentIndexChanged) #hayq eu implementar o metodo
        # Traballar tamen cos cambios de texto
        # SetEditable por defecto e False, polo que a menos que queremos activalo non necesitamos indicalo
        cmbCores.setEditable(False) # se o poñemos editable, facemos que lle podamos cambiar o texto, e engadir un novo elemento na lista
        caixaV.addWidget(cmbCores) # se non fago esto aparece en branco
        # cando cambie o id do elemento selecionado, cuando selecione outro color poñer un sinal quie nos indica que cambia de id por que o que quero e cambiar o color de fondo, para que cando o usuario toque ahi, se desencadene todo e reaccionar

        # Revisar QListView: https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListView.html







        control = QWidget()
        control.setLayout(caixaV)
        self.setCentralWidget(control)
        self.show()

    def on_Boton_Vermello (self):
        self.stack.setCurrentIndex (0)

    def on_Boton_Azul (self):
        self.stack.setCurrentIndex(1)

    def on_Boton_Verde (self):
        self.stack.setCurrentIndex(2)

    def on_Boton_Laranxa (self):
        self.stack.setCurrentIndex(3)

    def on_rbtVermello_clicked (self):
        self.stack.setCurrentIndex(0)

    def on_rbtAzul_clicked (self):
        self.stack.setCurrentIndex(1)

    def on_rbtVerde_clicked (self):
        self.stack.setCurrentIndex(2)

    def on_rbtLaranxa_clicked (self):
        self.stack.setCurrentIndex(3)

    # Izo muchas conbinaciones de botones
    def on_chkVermello_clicked(self):
        # primero cuando se pulsa, comprobar si el resto estan pulsados
        # revisa en fiestraprincipal self.chkVerde,clicked.connect(self.on_chkVerde_clicked)
        #                           self.chkVerde = QCheckBox("Verde")            # comprobamos si los otros estan checkeados comprobamos el valor(numero del color del indice)
        if self.chkVerde.isChecked():  # si el verde esta checkeado la conbinacion da marron
            self.stack.setCurrentIndex(8)  # numero del indice del marron
        elif self.chkAzul.isChecked():  # si el azul esta checkeado la conbionacion da violeta
            self.stack.setCurrentIndex(6)  # numero del indice del violeta
        elif self.chkLaranxa.isChecked():  # si el laranza esta checkeado da vermeranza
            self.stack.setCurrentIndex(9)  # indice laranxa
            """Verdello-verde marron
               verdello-Azul violeta
               verdello-laranxa vermeranxa"""
        #seria o mesmo nos demais
        #######

        print ("Vermello-verde marro")

    def on_chkAzul_clicked (self):
        """Verde-azul AZULOSO
                   vermello-Azul violeta
                   AZUL-laranxa violetapalido???"""
        print ("Mixtura")

    def on_chkVerde_clicked (self):
        """Verde-azul AZULOSO
           verde-vermello verdeamarronado
           verde-laranxa verdelaranxado???"""
    def on_chkLaranxa_clicked (self):
        """Verde-laranxa verdelaranxado
                           vermello-laranxa laranxaforte
                           AZUL-laranxa violetapalido???"""

    #Metodo que atende a sinal de on_cmbCores_currentIndexChanged e ten un parametro asociado
    # enlace wiki: https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QComboBox.html#PySide6.QtWidgets.QComboBox.currentIndexChanged
    def on_cmbCores_currentIndexChanged (self, indice):
        #aqui seria o que seria o noso stack, asignarlle o indice podemos pasarllo directamente
        self.stack.setCurrentIndex(indice)
        print("Cambiou o indice")

    #Poderia traballar co texto en lugar do indice, ambalas duas opcions serian validas, neste caso teriamos que especificar o color
    def on_cmbCores_currentTextChanged (self, texto):
        if texto == "Azul":
            self.stack.setCurrentIndex(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fiestCambioura = FiestraPrincipal()
    app.exec()
