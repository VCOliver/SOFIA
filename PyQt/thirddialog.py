# -*- coding: utf-8 -*-


################################### LIBRARIES ###############################################
from PyQt4 import QtCore, QtGui
import parametros
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


################################### UI_thirdDialog  #########################################
class Ui_thirdDialog(object):

    def setupUi(self, thirdDialog):

        thirdDialog.setObjectName(_fromUtf8("thirdDialog"))
        thirdDialog.resize(800, 480)
        #thirdDialog.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        font = QtGui.QFont()
        font.setPointSize(18)
        thirdDialog.setFont(font)
        thirdDialog.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);color: rgb(255,255,255);"))

        self.label_2 = QtGui.QLabel(thirdDialog)
        self.label_2.setGeometry(QtCore.QRect(240, 50, 301, 71))
        self.label_2.setStyleSheet(_fromUtf8("font: 26pt \"Arial\";\n""font-weight:bold;"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.lcdNumber = QtGui.QLCDNumber(thirdDialog)
        self.lcdNumber.setGeometry(QtCore.QRect(80, 200, 121, 81))
        self.lcdNumber.setStyleSheet(_fromUtf8("background-color: blue;color:white;\n"))
        self.lcdNumber.display(parametros.todos['potenciaInicial'])
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))

        self.pushButton = QtGui.QPushButton(thirdDialog)
        self.pushButton.setGeometry(QtCore.QRect(250, 180, 61, 61))
        self.pushButton.setStyleSheet("font-weight:bold;background-color: blue;border-radius: 10px;")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.pushButton_2 = QtGui.QPushButton(thirdDialog)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 250, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.setStyleSheet("font-weight:bold;background-color: blue;border-radius: 10px;")


        self.label_3 = QtGui.QLabel(thirdDialog)
        self.label_3.setGeometry(QtCore.QRect(90, 290, 91, 21))
        self.label_3.setStyleSheet(_fromUtf8("font: 16pt \"Arial\";\n"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        
        self.pushButton_3 = QtGui.QPushButton(thirdDialog)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 180, 61, 61))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.setStyleSheet("font-weight:bold;background-color: blue;border-radius: 10px;")
    


        self.label_4 = QtGui.QLabel(thirdDialog)
        self.label_4.setGeometry(QtCore.QRect(480, 290, 91, 21))
        self.label_4.setStyleSheet(_fromUtf8("font: 16pt \"Arial\";\n"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))


        self.lcdNumber_2 = QtGui.QLCDNumber(thirdDialog)
        self.lcdNumber_2.setGeometry(QtCore.QRect(470, 200, 121, 81))
        self.lcdNumber_2.setStyleSheet(_fromUtf8("border: 2px solid gray;\n""background-color: rgb(0, 0, 0);\n"))
        self.lcdNumber_2.setStyleSheet(_fromUtf8("background-color: blue;color:white"))
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))


        self.lcdNumber_2.display(parametros.todos['potenciaFinal'])

        self.pushButton_4 = QtGui.QPushButton(thirdDialog)
        self.pushButton_4.setGeometry(QtCore.QRect(640, 250, 61, 61))
        self.pushButton_4.setStyleSheet(_fromUtf8("font-weight:bold;background-color: blue;border-radius: 10px;"))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        

        self.pushButton_5 = QtGui.QPushButton(thirdDialog)
        self.pushButton_5.setGeometry(QtCore.QRect(450, 400, 181, 51))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_5.setStyleSheet("font-weight:bold;background-color: green;border-radius: 10px;")
    

        self.label_8 = QtGui.QLabel(thirdDialog)
        self.label_8.setGeometry(QtCore.QRect(210, 280, 40, 13))
        self.label_8.setStyleSheet(_fromUtf8("font: 12pt \"Arial\";\n"))
        self.label_8.setObjectName(_fromUtf8("label_8"))

        self.label_9 = QtGui.QLabel(thirdDialog)
        self.label_9.setGeometry(QtCore.QRect(600, 280, 30, 13))
        self.label_9.setStyleSheet(_fromUtf8("font: 12pt \"Arial\";\n"))
        self.label_9.setObjectName(_fromUtf8("label_9"))

        self.pushButton_off = QtGui.QPushButton(thirdDialog)
        self.pushButton_off.setGeometry(QtCore.QRect(160, 400, 181, 51))
        self.pushButton_off.setStyleSheet(_fromUtf8("font-weight:bold;background-color: red;border-radius: 10px;"))
        self.pushButton_off.setObjectName(_fromUtf8("pushButton_off"))
        
        QtCore.QMetaObject.connectSlotsByName(thirdDialog)

    def retranslateUi(self):
        self.setWindowTitle(_translate("thirdDialog", "Dialog", None))
        self.label_2.setText(_translate("thirdDialog", "POTÊNCIA ", None))
        self.pushButton.setText(_translate("thirdDialog", "+", None))
        self.pushButton_2.setText(_translate("thirdDialog", "-", None))
        self.label_3.setText(_translate("thirdDialog", "Inicial", None))
        self.pushButton_3.setText(_translate("thirdDialog", "+", None))
        self.label_4.setText(_translate("thirdDialog", "Final", None))
        self.pushButton_4.setText(_translate("thirdDialog", "-", None))
        self.pushButton_5.setText(_translate("thirdDialog", "OK", None))
        self.label_8.setText(_translate("thirdDialog", "W", None))
        self.label_9.setText(_translate("thirdDialog", "W", None))
        self.pushButton_off.setText(_translate("thirdDialog", "VOLTAR", None))
       

        QtCore.QObject.connect(self.pushButton , QtCore.SIGNAL("clicked()") , self.initial_button_Plus_click)
        QtCore.QObject.connect(self.pushButton_2 , QtCore.SIGNAL("clicked()") , self.initial_button_Minus_click)
        QtCore.QObject.connect(self.pushButton_3 , QtCore.SIGNAL("clicked()") , self.final_button_Plus_click)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL("clicked()") , self.final_button_Minus_click)
        # QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Timer_Func)
        # QtCore.QObject.connect(self.pushButton_off, QtCore.SIGNAL(_fromUtf8("clicked()")), thirdDialog.close)



        

    def initial_button_Plus_click(self):
        if parametros.todos['potenciaInicial'] >= parametros.todos['potenciaMax']:
            parametros.todos['potenciaInicial'] = parametros.todos['potenciaMax']
        else:
            if parametros.todos['potenciaInicial']>=parametros.todos['potenciaFinal']:
                parametros.todos['potenciaInicial'] = parametros.todos['potenciaFinal']
            else:
                parametros.todos['potenciaInicial'] +=1
        self.lcdNumber.display(parametros.todos['potenciaInicial'])
        parametros.todos['potenciaRT'] = parametros.todos['potenciaInicial']     

    def initial_button_Minus_click(self):
        if parametros.todos['potenciaInicial'] <= parametros.todos['potenciaMin']:
            parametros.todos['potenciaInicial'] = parametros.todos['potenciaMin']
        else:
            parametros.todos['potenciaInicial'] -=1 
        self.lcdNumber.display(parametros.todos['potenciaInicial'])
        parametros.todos['potenciaRT'] = parametros.todos['potenciaInicial']

    def final_button_Plus_click(self):       
        if parametros.todos['potenciaFinal'] >= parametros.todos['potenciaMax']:
            parametros.todos['potenciaFinal'] = parametros.todos['potenciaMax']
        else:
            parametros.todos['potenciaFinal'] +=1
        self.lcdNumber_2.display(parametros.todos['potenciaFinal'])

    def final_button_Minus_click(self):
        if parametros.todos['potenciaFinal'] > parametros.todos['potenciaInicial']:
            parametros.todos['potenciaFinal'] -=1
        self.lcdNumber_2.display(parametros.todos['potenciaFinal'])


#############################################################################################

################################### MAIN ####################################################
# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     thirdDialog = QtGui.QDialog()
#     ui = Ui_thirdDialog()
#     ui.setupUi(thirdDialog)
#     thirdDialog.show()
#     sys.exit(app.exec_())
#############################################################################################


