# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'verification.ui'
#
# Created: Thu Apr 14 22:52:41 2016
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import parametros
import icons_sofia_software_rc

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_VerifyWindow(object):
    def setupUi(self, verifyWindow):
        verifyWindow.setObjectName(_fromUtf8("verifyWindow"))
        verifyWindow.resize(800, 480)
        #verifyWindow.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        verifyWindow.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);"))
        self.centralwidget = QtGui.QWidget(verifyWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 60, 211, 311))
        self.frame.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.lcdNumber = QtGui.QLCDNumber(self.frame)
        self.lcdNumber.setGeometry(QtCore.QRect(100, 60, 101, 91))
        self.lcdNumber.setStyleSheet(_fromUtf8("background-color:green;\n""color:white;"))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.lcdNumber.display(parametros.todos['tempo'])
        self.lcdNumber_2 = QtGui.QLCDNumber(self.frame)
        self.lcdNumber_2.setGeometry(QtCore.QRect(100, 210, 101, 91))
        self.lcdNumber_2.setStyleSheet(_fromUtf8("background-color:orange;\n""color:white;"))
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))
        self.lcdNumber_2.display(parametros.todos['temperaturaMax'])
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 180, 31))
        self.label_2.setStyleSheet(_fromUtf8("color:white;\n""font: 16pt \"Arial\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 160, 171, 51))
        self.label_3.setStyleSheet(_fromUtf8("color:white;\n""font: 16pt \"Arial\";"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_8 = QtGui.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(25, 70, 55, 71))
        self.label_8.setText(_fromUtf8(""))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        pixmap = QtGui.QPixmap(_fromUtf8(":/verify_icons/time.png"))
        pixmap = pixmap.scaled(60, 60, QtCore.Qt.KeepAspectRatio)
        self.label_8.setPixmap(pixmap)

        self.label_9 = QtGui.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(40, 220, 55, 71))
        self.label_9.setText(_fromUtf8(""))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        pixmap_2 = QtGui.QPixmap(_fromUtf8(":/verify_icons/tempMax.png"))
        pixmap_2 = pixmap_2.scaled(70, 70, QtCore.Qt.KeepAspectRatio)
        self.label_9.setPixmap(pixmap_2)

        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(300, 60, 211, 311))
        self.frame_2.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);"))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.lcdNumber_3 = QtGui.QLCDNumber(self.frame_2)
        self.lcdNumber_3.setGeometry(QtCore.QRect(100, 60, 101, 91))
        self.lcdNumber_3.setStyleSheet(_fromUtf8("background-color:blue;\n""color:white;"))
        self.lcdNumber_3.setObjectName(_fromUtf8("lcdNumber_3"))
        self.lcdNumber_3.display(parametros.todos['potenciaInicial'])
        self.lcdNumber_4 = QtGui.QLCDNumber(self.frame_2)
        self.lcdNumber_4.setGeometry(QtCore.QRect(100, 210, 101, 91))
        self.lcdNumber_4.setStyleSheet(_fromUtf8("background-color:blue;\n""color:white;"))
        self.lcdNumber_4.setObjectName(_fromUtf8("lcdNumber_4"))
        self.lcdNumber_4.display(parametros.todos['potenciaFinal'])
        self.label_4 = QtGui.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 150, 50))
        self.label_4.setStyleSheet(_fromUtf8("color:white;\n""font: 16pt \"Arial\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(20, 160, 190, 51))
        self.label_5.setStyleSheet(_fromUtf8("color:white;\n""font: 16pt \"Arial\";"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_10 = QtGui.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(20, 220, 71, 71))
        self.label_10.setText(_fromUtf8(""))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        pixmap_4 = QtGui.QPixmap(_fromUtf8(":/verify_icons/finpot.png"))
        pixmap_4 = pixmap_4.scaled(60, 60, QtCore.Qt.KeepAspectRatio)
        self.label_10.setPixmap(pixmap_4)

        self.label_11 = QtGui.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(20, 70, 71, 71))
        self.label_11.setText(_fromUtf8(""))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        pixmap_3 = QtGui.QPixmap(_fromUtf8(":/verify_icons/init_pot.png"))
        pixmap_3 = pixmap_3.scaled(60, 60, QtCore.Qt.KeepAspectRatio)
        self.label_11.setPixmap(pixmap_3)

        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(560, 60, 211, 311))
        self.frame_3.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);"))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.lcdNumber_5 = QtGui.QLCDNumber(self.frame_3)
        self.lcdNumber_5.setGeometry(QtCore.QRect(100, 60, 101, 91))
        self.lcdNumber_5.setStyleSheet(_fromUtf8("background-color:purple;\n""color:white;"))
        self.lcdNumber_5.setObjectName(_fromUtf8("lcdNumber_5"))
        self.lcdNumber_5.display(parametros.todos['potenciaStep'])
        self.lcdNumber_6 = QtGui.QLCDNumber(self.frame_3)
        self.lcdNumber_6.setGeometry(QtCore.QRect(100, 210, 101, 91))
        self.lcdNumber_6.setStyleSheet(_fromUtf8("background-color:purple;\n""color:white;"))
        self.lcdNumber_6.setObjectName(_fromUtf8("lcdNumber_6"))
        self.lcdNumber_6.display(parametros.todos['tempoStep'])
        self.label_6 = QtGui.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(10, 5, 180, 51))
        self.label_6.setStyleSheet(_fromUtf8("color:white;\n""font: 16pt \"Arial\";"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(10, 160, 180, 50))
        self.label_7.setStyleSheet(_fromUtf8("color:white;\n""font: 16pt \"Arial\";"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_12 = QtGui.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(20, 70, 71, 71))
        self.label_12.setText(_fromUtf8(""))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        pixmap_5 = QtGui.QPixmap(_fromUtf8(":/verify_icons/powerScale.png"))
        pixmap_5 = pixmap_5.scaled(60, 60, QtCore.Qt.KeepAspectRatio)
        self.label_12.setPixmap(pixmap_5)

        self.label_13 = QtGui.QLabel(self.frame_3)
        self.label_13.setGeometry(QtCore.QRect(20, 220, 71, 71))
        self.label_13.setText(_fromUtf8(""))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        pixmap_6 = QtGui.QPixmap(_fromUtf8(":/verify_icons/timeScale.png"))
        pixmap_6 = pixmap_6.scaled(60, 60, QtCore.Qt.KeepAspectRatio)
        self.label_13.setPixmap(pixmap_6)

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 0, 360, 40))
        self.label.setStyleSheet(_fromUtf8("color:white;\n""font: 24pt \"Arial\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 400, 161, 51))
        self.pushButton.setStyleSheet(_fromUtf8("background-color:green;\n""color:white;\n""border-radius: 10px;"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 400, 161, 51))
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color:red;\n""color:white;\n""border-radius: 10px;"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        verifyWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(verifyWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        verifyWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(verifyWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        verifyWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(verifyWindow)

    def retranslateUi(self):
        self.label_2.setText(QtGui.QApplication.translate("verifyWindow", "DURAÇÃO (MIN)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("verifyWindow", "<html>TEMPERATURA <br>LIMITE (°C)</html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("verifyWindow", "<html>POTÊNCIA <br>INICIAL (W)<html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("verifyWindow", "<html>POTÊNCIA <br>FINAL (W)<html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("verifyWindow", "<html>PASSO DE<br> POTÊNCIA (W)<html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("verifyWindow", "<html>PASSO DE<br>TEMPO (MIN)<html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("verifyWindow", "TELA DE VERIFICAÇÃO", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("verifyWindow", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("verifyWindow", "VOLTAR", None, QtGui.QApplication.UnicodeUTF8))



################################### MAIN ####################################################
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    verifyWindow = QtGui.QMainWindow()
    ui = Ui_VerifyWindow()
    ui.setupUi(verifyWindow)
    verifyWindow.show()
    sys.exit(app.exec_())
#############################################################################################
