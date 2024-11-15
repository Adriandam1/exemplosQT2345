import sys

from PyQt6.QtGui import QColor
#Paxina documentacion: https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMainWindow.html
#QPushButton Class: https://doc.qt.io/qt-6/qpushbutton.html
#QLabel: https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QLabel.html

#A importacion de widgets va crecendo segun añadimos componentes
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QFrame, QCheckBox)
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

        #Creamos etiqueta:
        self.lblSaudo = QLabel("Poder ter texto inicial")
        #A engadimos a caixa:
        caixaV.addWidget(self.lblSaudo)

        #Vamos a poñer primero un boton:
        btnSaudo = QPushButton("Saúdo")

        #Damoslle funcionalidad o boton
        btnSaudo.clicked.connect(self.on_btnSaudo_clicked) #lle vamos a pasar a direccion do metodo da funcion, e voy idea poñer no nome da funcion o boton e a funcion que imos realizar

        #Metemos o boton na caixa:
        caixaV.addWidget(btnSaudo)

        '''
        #QLabel
        label = QLabel(self)
        label.setText("Primeira liña do QLabel\nSegunda liña do label")
        label.adjustSize() # hago que el label se ajuste al tamaño que requiere
        '''


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
        self.lblSaudo.setText("Ola ola")

###### editado reciente
# Izo muchas conbinaciones de botones
    def on_chkVerdello_clicked (self):
        # primero cuando se pulsa, comprobar si el resto estan pulsados
        # revisa en fiestraprincipal self.chkVerde,clicked.connect(self.on_chkVerde_clicked)
        #                           self.chkVerde = QCheckBox("Verde")
        # comprobamos si los otros estan checkeados comprobamos el valor(numero del color del indice)
        if self.chkVerde.isChecked(): # si el verde esta checkeado la conbinacion da marron
            self.stack.setCurrentIndex(8) # numero del indice del marron
        elif self.chkAzul.isChecked(): # si el azul esta checkeado la conbionacion da violeta
            self.stack.setCurrentIndex(6) # numero del indice del violeta
        elif self.chkLaranxa.isChecked(): # si el laranza esta checkeado da vermeranza
            self.stack.setCurrentIndex(9) #indice laranxa
        """Verdello-verde marron
           verdello-Azul violeta
           verdello-laranxa vermeranxa"""
#######



#Detectar que isto e a libreria principal,
# conectamos o que seria a aplicacion coa miña ventana
# e lanzo o que seria a aplicacion
if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = PrimeiraFiestra()
    aplicacion.exec()
















