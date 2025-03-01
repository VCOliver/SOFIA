# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'help_box.ui'
#
# Created: Wed Mar 16 10:29:20 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import icons_sofia_software_rc


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

class Ui_errorDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(466, 390)
        #Dialog.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        qr = Dialog.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        Dialog.move(qr.topLeft())
        Dialog.setStyleSheet(_fromUtf8("background-color: gray;color: black"))
        self.label_logolab = QtGui.QLabel(Dialog)
        self.label_logolab.setGeometry(QtCore.QRect(120, 10, 231, 181))
        self.label_logolab.setText(_fromUtf8(""))
        self.label_logolab.setPixmap(QtGui.QPixmap(_fromUtf8(":/logos_sofia/rsz_logo_lab.png")))
        self.label_logolab.setObjectName(_fromUtf8("label_logolab"))
        self.label_config_infos = QtGui.QLabel(Dialog)
        self.label_config_infos.setGeometry(QtCore.QRect(10, 140, 441, 231))
        self.label_config_infos.setObjectName(_fromUtf8("label_config_infos"))
        self.label_config_infos.setStyleSheet("font-weight:bold;")
        self.pushButton_5 = QtGui.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(185, 300, 100, 50))
        self.pushButton_5.setStyleSheet(_fromUtf8("font: 14pt \"Arial\";"))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_5.setStyleSheet("color: white;font-weight:bold;background-color: red;border-radius: 10px;")

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self):
        self.pushButton_5.setText(_translate("Dialog", "OK", None))
        self.setWindowTitle(_translate("Atenção Erro", "Atenção", None))
        self.label_config_infos.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Atenção!!</span><p align=\"center\"><span style=\" font-size:12pt;\">Falha no Sistema!!</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Por favor, procure uma de nossas <br> assistências técnicas</span></p><p align=\"center\"><br/></p></body></html>", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_errorDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
