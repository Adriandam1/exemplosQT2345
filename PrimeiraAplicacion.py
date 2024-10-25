import sys

from PyQt6.QtGui import QColor
#Paxina documentacion: https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMainWindow.html
#QPushButton Class: https://doc.qt.io/qt-6/qpushbutton.html
#QLabel: https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QLabel.html

#A importacion de widgets va crecendo segun añadimos componentes
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QFrame)
# QmainWindow seria la fiestra principal donde creariamos os obxetoc, teremos que engadir controles etc etc
# Para poder interaccionar co sistema operativo tamen temos que utilizar QApplication

from PyQt6.QtGui import QColor, QPalette
from PyQt6.uic.Compiler.qtproxies import QtWidgets


#-------------------------------------------

# Declaramos unha clase que vai a ser heredeira de esta QMainWindow
class PrimeiraFiestra (QMainWindow):

    def __init__(self):
        # aqui vamos a inicializar a ventana orixinal y eso...
        super().__init__()

        #Modificar o titulo:
        self.setWindowTitle("A miña primeira fiestra con Qt")
        #Tamaño minimo da ventana:
        self.setMinimumSize(500, 300)
        #Tamaño maximo da ventana:
        self.setMaximumSize(1000,600)
        #Cambiar de fondo a miña fiestra:
        paleta = self.palette() # collo el palete # turquoise , red , blue, aquamarine
        paleta.setColor(QPalette.ColorRole.Window, QColor("turquoise")) #Ya cambio o colo da propiedade
        self.setPalette(paleta) # yo pongo por este

        #O mais simple que temos e os obxetos box:
        caixaV = QVBoxLayout()

        #Vamos a poñer primero un boton:
        btnSaudo = QPushButton("Saúdo")

        #Damoslle funcionalidad o boton
        btnSaudo.clicked.connect(self.on_btnSaudo_clicked) #lle vamos a pasar a direccion do metodo da funcion, e voy idea poñer no nome da funcion o boton e a funcion que imos realizar

        #Metemos o boton na caixa:
        caixaV.addWidget(btnSaudo)

        #QLabel
        label = QLabel(self)
        label.setText("Primeira liña do QLabel\nSegunda liña do label")
        label.adjustSize() # hago que el label se ajuste al tamaño que requiere



        # Caixa non é widget, é layout e eu necesito un widget polo que teño que facer a conversion
        container = QWidget()
        container.setLayout(caixaV) #lle dou como layout a caixa principal

        #Metemos a caixa na ventana:
        self.setCentralWidget(container)

        #mostramos a ventana
        self.show()

    #Tódo o de arriba era vista, os metodos que pongamos agora serán os controladores
    #Vease __init__ vista e as funcions controlador VC vista controlador
    def on_btnSaudo_clicked(self):
        print("Ola usuarioaria")





#Detectar que isto e a libreria principal,
# conectamos o que seria a aplicacion coa miña ventana
# e lanzo o que seria a aplicacion
if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = PrimeiraFiestra()
    aplicacion.exec()
















