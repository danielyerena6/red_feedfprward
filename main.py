import numpy as np
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5 import uic

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui.ui",self)
        self.neuronas = []
        self.no_capas = 0
        self.max_neuronas = 0
        self.pesos = []
        self.umbrales = []
        self.activacion = []
        self.entrada = [[0, 0], [0, 1], [1, 0], [1, 1]]

        self.xor.clicked.connect(self.Xor)
        self.ejercicio.clicked.connect(self.Ejercicio)
        self.feedforward.clicked.connect(self.entrenamiento)
        
        self.tableWidget=QTableWidget()
        self.flag1=False
       

       



    def sigmoide(self,acumulador):
        return 1 / (1 + np.exp(-acumulador))

    def Ejercicio(self):
        self.flag1=False

        self.neuronas = [2, 2, 2, 2]
        self.no_capas = 4
        self.max_neuronas = max((self.neuronas))
        self.pesos = np.ones((self.no_capas - 1, self.max_neuronas, self.max_neuronas))
        self.umbrales = np.zeros((self.no_capas - 1, self.max_neuronas))
        self.activacion = np.zeros((self.no_capas, self.max_neuronas))

        for i in range(self.no_capas - 1):
            for j in range(self.max_neuronas):
                self.umbrales[i, j] = 0.5

    def Xor(self):
        self.flag1=True

        self.neuronas = [2, 2, 1]
        self.no_capas = 3

        self.max_neuronas = max((self.neuronas))
        self.pesos = np.zeros((self.no_capas - 1, self.max_neuronas, self.max_neuronas))
        self.umbrales = np.zeros((self.no_capas - 1, self.max_neuronas))
        self.activacion = np.zeros((self.no_capas, self.max_neuronas))

        self.pesos[0, 0, 0] = 5.191129
        self.pesos[0, 0, 1] = 2.758669
        self.pesos[0, 1, 0] = 5.473012
        self.pesos[0, 1, 1] = 2.769596
        self.pesos[1, 0, 0] = 5.839709
        self.pesos[1, 1, 0] = -6.186834

        self.umbrales[0, 0] = -1.90289
        self.umbrales[0, 1] = -4.127002
        self.umbrales[1, 0] = -2.570539

    def entrenamiento(self):
        salidas1=[]
        salidas2=[]
        self.listWidget.clear()
        for i in range(len(self.entrada)):
            self.listWidget.addItem("Patron no. {}".format(i))

            self.Feedforward(self.entrada[i])
            print(self.activacion)
            contador =0
            contador1 =1

            for capa in self.activacion:
                contador=0
                self.listWidget.addItem("Capa {}".format(contador1))
                for activacion in capa:
                    self.listWidget.addItem("ac({}) = {}".format(contador,activacion))
                    contador+=1
                contador1 += 1




            salidas1.append(self.activacion[-1,0])
            salidas2.append(self.activacion[-1,1])

        if(self.flag1):
            self.label_10.setText(str(salidas1[0]))
            self.label_11.setText(str(salidas1[1]))
            self.label_12.setText(str(salidas1[2]))
            self.label_13.setText(str(salidas1[3]))

            self.label_14.setText("")
            self.label_15.setText("")
            self.label_16.setText("")
            self.label_17.setText("")

        else:

            self.label_10.setText(str(salidas1[0]))
            self.label_11.setText(str(salidas1[1]))
            self.label_12.setText(str(salidas1[2]))
            self.label_13.setText(str(salidas1[3]))

            self.label_14.setText(str(salidas2[0]))
            self.label_15.setText(str(salidas2[1]))
            self.label_16.setText(str(salidas2[2]))
            self.label_17.setText(str(salidas2[3]))


    def Feedforward(self,enter):


        self.activacion[0, 0] = enter[0]
        self.activacion[0, 1] = enter[1]

        for i in range(self.no_capas - 1):

            for j in range(self.neuronas[i + 1]):
                acumulador = 0
                for k in range(self.neuronas[i]):
                    acumulador += self.activacion[i, k] * self.pesos[i, k, j]
                    print(" {}   {}  ".format(self.activacion[i, k], self.pesos[i, k, j]))

                acumulador += self.umbrales[i, j]
                print("{}  \n".format(self.umbrales[i, j]))

                self.activacion[i + 1, j] = self.sigmoide(acumulador)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI=main()
    GUI.show()

    sys.exit(app.exec_())




