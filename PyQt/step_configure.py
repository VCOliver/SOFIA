# -*- coding: utf-8 -*-

################################### LIBRARIES ###############################################
from __future__ import division
from PyQt4 import QtCore, QtGui
from verification import Ui_VerifyWindow
import parametros
#############################################################################################



################################### GLOBAL VARIABLES ########################################
step = 2
checked = False
#############################################################################################



################################### ERROR TREATMENT #########################################
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
#############################################################################################



################################### UI_STEPDIALOG  ##########################################
class Ui_stepDialog(object):
    def setupUi(self, stepDialog):
        stepDialog.setObjectName(_fromUtf8("stepDialog"))
        stepDialog.resize(800, 480)
        #stepDialog.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        font = QtGui.QFont()
        font.setPointSize(18)
        stepDialog.setFont(font)
        stepDialog.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);color: rgb(255,255,255);"))


        self.lcdNumber_2 = QtGui.QLCDNumber(stepDialog)
        self.lcdNumber_2.setGeometry(QtCore.QRect(450, 190, 141, 101))
        self.lcdNumber_2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.lcdNumber_2.setStyleSheet(_fromUtf8("border: 2px solid gray;\n""background-color: rgb(0, 0, 0);\n"))
        self.lcdNumber_2.setStyleSheet(_fromUtf8("background-color: blue;color:white"))
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))
        self.lcdNumber_2.display(2)

        self.pushButton_3 = QtGui.QPushButton(stepDialog)    # pushButton para incrementar os passos
        self.pushButton_3.setGeometry(QtCore.QRect(620, 170, 61, 61))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.setStyleSheet("font-weight:bold;background-color: blue;border-radius: 10px;")


        self.pushButton_4 = QtGui.QPushButton(stepDialog) # pushButton para decrementar os passos
        self.pushButton_4.setGeometry(QtCore.QRect(620, 240, 61, 61))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.setStyleSheet("font-weight:bold;background-color: blue;border-radius: 10px;")

        self.pushButton_OK = QtGui.QPushButton(stepDialog)
        self.pushButton_OK.setGeometry(QtCore.QRect(450, 400, 181, 51))
        self.pushButton_OK.setObjectName(_fromUtf8("pushButton_OK"))
        self.pushButton_OK.setStyleSheet("font-weight:bold;background-color: green;border-radius: 10px;")
        
        self.pushButton_BACK = QtGui.QPushButton(stepDialog)
        self.pushButton_BACK.setGeometry(QtCore.QRect(160, 400, 181, 51))
        self.pushButton_BACK.setObjectName(_fromUtf8("pushButton_BACK"))
        self.pushButton_BACK.setStyleSheet("font-weight:bold;background-color:red;border-radius: 10px;")

        
        self.checkBox = QtGui.QCheckBox(stepDialog)
        self.checkBox.setGeometry(QtCore.QRect(380, 320, 400, 41))
        self.checkBox.setFont(font)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox.setStyleSheet(_fromUtf8("font: 12pt;\n""font-weight:bold;"))
        

        self.label = QtGui.QLabel(stepDialog)
        self.label.setGeometry(QtCore.QRect(50, 130, 310, 230))
        self.label.setObjectName(_fromUtf8("label"))
        self.label.setStyleSheet(_fromUtf8("font: 26pt \"Arial\";\n""font-weight:bold;"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label_2"))
        
        self.label_2 = QtGui.QLabel(stepDialog)
        self.label_2.setGeometry(QtCore.QRect(240, 30, 301, 71))
        self.label_2.setStyleSheet(_fromUtf8("font: 26pt \"Arial\";\n""font-weight:bold;"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        QtCore.QMetaObject.connectSlotsByName(stepDialog)

    def retranslateUi(self):
        self.setWindowTitle(_translate("stepDialog", "Dialog", None))
        self.pushButton_3.setText(_translate("stepDialog", "+", None))
        self.pushButton_4.setText(_translate("stepDialog", "-", None))
        self.pushButton_OK.setText(_translate("stepDialog", "OK", None))
        self.pushButton_BACK.setText(_translate("stepDialog", "VOLTAR", None))
        self.checkBox.setText(_translate("stepDialog", "Mostrar: Passo de Potência/Passo de Tempo", None))
        self.label_2.setText(_translate("stepDialog", "Iterações", None))        
        self.label.setText(_translate("stepDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Insira ao lado as iterações que deseja <br> para o Tempo e Potência <br>setados anteriormente</span></p></body></html>", None))
        self.calculateSteps()
        QtCore.QObject.connect(self.pushButton_3 , QtCore.SIGNAL("clicked()") , self.Plus_click)
        QtCore.QObject.connect(self.pushButton_4 , QtCore.SIGNAL("clicked()") , self.Minus_click)
        QtCore.QObject.connect(self.pushButton_OK , QtCore.SIGNAL("clicked()") , self.Reset_check)
        QtCore.QObject.connect(self.pushButton_BACK , QtCore.SIGNAL("clicked()") , self.Reset_check)
        QtCore.QObject.connect(self.checkBox , QtCore.SIGNAL("clicked()") , self.state_changed)

    def Reset_check(self):
        global checked
        checked = False

    def Plus_click(self):
        global step,checked
        step +=1
        if step > 10: # Até 10 passos
            step = 10
        self.lcdNumber_2.display(step)
        self.calculateSteps()
        self.showInfo(checked)

    def Minus_click(self):     #decrementa step
        global step,checked
        step -=1
        if step < 2: #Ao menos 2 passos
            step = 2
        self.lcdNumber_2.display(step)
        self.calculateSteps()
        self.showInfo(checked)

    def state_changed(self):
        global step, checked
        checked = not checked
        self.showInfo(checked)

    def showInfo(self,checked):
        self.calculateSteps()
        #True = checked
        if(checked):
            self.label.setText(_translate("stepDialog","<html><head/><body><p align=\"left\"><span style= font-size:16pt;>Passo: %d  </span></p><p align=\"left\"><span style= font-size:16pt;>Passo de Potência [W]: %.2f </span></p><p align=\"left\"><span style= font-size:16pt;>Passo de Tempo [min]: %.2f </span></p></body></html>" %(step, parametros.todos['potenciaStep'],parametros.todos['tempoStep']), None))

        #False = not checked
        else:
            self.label.setText(_translate("stepDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Insira ao lado as iterações que deseja <br> para o Tempo e Potência <br>setados anteriormente</span></p></body></html>", None))        

    def calculateSteps(self):
        Delta_Pot = parametros.todos ['potenciaFinal'] - parametros.todos ['potenciaInicial'] 
        parametros.todos['potenciaStep'] = Delta_Pot/step
        parametros.todos['tempoStep'] = parametros.todos['tempo']/step
#############################################################################################



################################### MAIN ####################################################
# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     stepDialog = QtGui.QDialog()
#     ui = Ui_stepDialog()
#     ui.setupUi(stepDialog)
#     stepDialog.show()
#     sys.exit(app.exec_())
#############################################################################################

