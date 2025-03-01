# -*- coding: utf-8 -*-

################################### LIBRARIES ###############################################
from PyQt4 import QtCore, QtGui
import parametros                                                           
#############################################################################################



################################### ERROR TREATMENT #########################################
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
#############################################################################################




##############################  UI_TEMPERATUREDIALOG  #######################################
class Ui_temperatureDialog(object):
    def setupUi(self):
        self.setObjectName(_fromUtf8("self"))
        self.resize(800, 480)
        #self.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.setFont(font)
        self.setStyleSheet(_fromUtf8("background-color: black;"))

        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 0, 711, 111))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))

        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(210, 120, 371, 41))
        self.label_2.setStyleSheet(_fromUtf8("font: 26pt \"Arial\";\n""color:white;"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.pushButton_3 = QtGui.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(630, 240, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color: blue;\n""border-radius: 5px;\n""color: white;"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.lcdNumber = QtGui.QLCDNumber(self)
        self.lcdNumber.setGeometry(QtCore.QRect(320, 220, 141, 101))
        self.lcdNumber.setStyleSheet(_fromUtf8("background-color: blue;color:white"))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.lcdNumber.display(parametros.todos['temperaturaMax'])
        
        self.pushButton_4 = QtGui.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 240, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(_fromUtf8("background-color: blue;\n""border-radius: 5px;\n""color: white;"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        
        self.pushButton_5 = QtGui.QPushButton(self)
        self.pushButton_5.setGeometry(QtCore.QRect(450, 400, 161, 51))
        self.pushButton_5.setStyleSheet(_fromUtf8("font: 14pt \"MS Shell Dlg 2\";\n""background-color: green;\n""border-radius: 5px;\n""color: white;"))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        
        self.label_9 = QtGui.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(490, 290, 71, 31))
        self.label_9.setStyleSheet(_fromUtf8("font: 75 16pt \"Arial\";\n""color:white;"))
        self.label_9.setObjectName(_fromUtf8("label_9"))

        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(190, 400, 161, 51))
        self.pushButton.setStyleSheet(_fromUtf8("font: 14pt \"Arial\";\n""background-color: red;\n""border-radius: 5px;\n""color: white;"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QtGui.QApplication.translate("self", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("self", "TEMPERATURA LIMITE", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("self", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("self", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("self", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("self", "°C", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("self", "VOLTAR", None, QtGui.QApplication.UnicodeUTF8))

        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buttonPlusClick)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buttonMinusClick)


    def buttonPlusClick(self):

        if parametros.todos['temperaturaMax']< parametros.todos['temperaturaLimSup']:
            parametros.todos['temperaturaMax'] +=1
            self.lcdNumber.display(parametros.todos['temperaturaMax'])


    def buttonMinusClick(self):
        if parametros.todos['temperaturaMax'] > parametros.todos['temperaturaLimInf']:
            parametros.todos['temperaturaMax'] -=1
            self.lcdNumber.display(parametros.todos['temperaturaMax'])


