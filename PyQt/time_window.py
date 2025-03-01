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



################################### UI_FourthDialog #########################################
class Ui_fourthDialog(object):
    def setupUi(self, fourthDialog):
        fourthDialog.setObjectName(_fromUtf8("fourthDialog"))
        fourthDialog.resize(800, 480)
        #fourthDialog.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        fourthDialog.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);color: white"))
        self.label_2 = QtGui.QLabel(fourthDialog)
        self.label_2.setGeometry(QtCore.QRect(220, 50, 341, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("font: 26pt \"Arial\";font-weight:bold;"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.pushButton_5 = QtGui.QPushButton(fourthDialog)
        self.pushButton_5.setGeometry(QtCore.QRect(450, 400, 181, 51))
        self.pushButton_5.setStyleSheet(_fromUtf8("font: 14pt \"Arial\";"))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_5.setStyleSheet("font-weight:bold;background-color: green;border-radius: 10px;")


        self.lcdNumber_2 = QtGui.QLCDNumber(fourthDialog)
        self.lcdNumber_2.setGeometry(QtCore.QRect(310, 190, 151, 101))
        self.lcdNumber_2.setStyleSheet(_fromUtf8("background-color: blue;"))
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))
        self.lcdNumber_2.display(parametros.todos['tempo'])

        self.pushButton_3 = QtGui.QPushButton(fourthDialog)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 200, 81, 81))

        font = QtGui.QFont()
        font.setPointSize(18)

        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.setStyleSheet("font-weight:bold;background-color: blue;border-radius: 10px;")

        self.pushButton_4 = QtGui.QPushButton(fourthDialog)
        self.pushButton_4.setGeometry(QtCore.QRect(140, 200, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.setStyleSheet("font-weight:bold;background-color: blue;border-radius: 10px;")
        
        self.label_12 = QtGui.QLabel(fourthDialog)
        self.label_12.setGeometry(QtCore.QRect(480, 280, 61, 31))
        self.label_12.setStyleSheet(_fromUtf8("font: 75 14pt \"Arial\";"))
        self.label_12.setObjectName(_fromUtf8("label_12"))

        self.pushButton_off = QtGui.QPushButton(fourthDialog)
        self.pushButton_off.setGeometry(QtCore.QRect(160, 400, 181, 51))
        self.pushButton_off.setStyleSheet(_fromUtf8("font-weight:bold;background-color: red;border-radius: 10px;"))
        self.pushButton_off.setObjectName(_fromUtf8("pushButton_off"))

        QtCore.QMetaObject.connectSlotsByName(fourthDialog)

    def retranslateUi(self):
        self.setWindowTitle(_translate("fourthDialog", "Dialog", None))
        self.label_2.setText(_translate("fourthDialog", "TEMPO FINAL", None))
        self.pushButton_5.setText(_translate("fourthDialog", "OK", None))
        self.pushButton_3.setText(_translate("fourthDialog", "+", None))
        self.pushButton_4.setText(_translate("fourthDialog", "-", None))
        self.label_12.setText(_translate("fourthDialog", "min", None))
        self.pushButton_off.setText(_translate("fourthDialog", "VOLTAR", None))
        QtCore.QObject.connect(self.pushButton_3 , QtCore.SIGNAL("clicked()") , self.time_button_Plus_click)
        QtCore.QObject.connect(self.pushButton_4 , QtCore.SIGNAL("clicked()") , self.time_button_Minus_click)

    def time_button_Plus_click(self):
        parametros.todos['tempo'] +=1
        self.lcdNumber_2.display(parametros.todos['tempo'])
        while parametros.todos['tempo'] > 20:
            self.lcdNumber_2.display(20)
            parametros.todos['tempo'] = 20      

    def time_button_Minus_click(self):
        parametros.todos['tempo'] -=1
        self.lcdNumber_2.display(parametros.todos['tempo'])
        while parametros.todos['tempo'] < 5:
            self.lcdNumber_2.display(5)
            parametros.todos['tempo'] = 5   
    
#############################################################################################



################################### MAIN ####################################################
# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     fourthDialog = QtGui.QDialog()
#     ui = Ui_fourthDialog()
#     ui.setupUi(fourthDialog)
#     fourthDialog.show()
#     sys.exit(app.exec_())
#############################################################################################

