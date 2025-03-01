# -*- coding: utf-8 -*-


################################### LIBRARIES ###############################################
from PyQt4 import QtCore, QtGui
import subprocess
import icons_sofia_software_rc
import os
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



################################### UI_Dialog ##############################################
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(466, 390)
        #Dialog.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        qr1 = Dialog.frameGeometry()
        cp1 = QtGui.QDesktopWidget().availableGeometry().center()
        qr1.moveCenter(cp1)
        Dialog.move(qr1.topLeft())
        Dialog.setStyleSheet(_fromUtf8("background-color: gray;color: black"))
        self.label_logolab = QtGui.QLabel(Dialog)
        self.label_logolab.setGeometry(QtCore.QRect(120, -20, 231, 181))
        self.label_logolab.setText(_fromUtf8(""))
        self.label_logolab.setPixmap(QtGui.QPixmap(_fromUtf8(":/logos_sofia/rsz_logo_lab.png")))
        self.label_logolab.setObjectName(_fromUtf8("label_logolab"))
        self.label_config_infos = QtGui.QLabel(Dialog)
        self.label_config_infos.setGeometry(QtCore.QRect(10, 140, 441, 231))
        self.label_config_infos.setObjectName(_fromUtf8("label_config_infos"))
        self.pushButton_5 = QtGui.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(185, 330, 100, 50))
        self.pushButton_5.setStyleSheet(_fromUtf8("font: 14pt \"Arial\";"))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_5.setStyleSheet("color: white;font-weight:bold;background-color: red;border-radius: 10px;")
        QtCore.QMetaObject.connectSlotsByName(Dialog)

       
    def retranslateUi(self):
        self.pushButton_5.setText(_translate("Dialog", "OK", None))
        self.setWindowTitle(_translate("Informações", "Informações", None))
        self.label_config_infos.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Gerador de Rádio Frequência </span><span style=\" font-size:12pt; font-style:italic;\">Sofia 2000</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Modelo xx - 000 Fabricado em 2016</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Frequência de Operação 500 kHz</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Potência de Saída (50 </span><span style=\" font-family:\'arial,sans-serif\'; font-size:12pt;\">Ω) : 50 W</span></p><p align=\"center\"><a> Para maiores informações sobre o Sofia 2000, veja <a href = /home/pedro/Desktop/DivisorTensaoCorrente.pdf>Manual Sofia</a></a><br/></p></body></html>", None))


    # def Open_Manual(self): 
    #     os.system("xpdf DivisorTensaoCorrente.pdf")
##############################################################################################

