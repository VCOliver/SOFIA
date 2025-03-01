# -*- coding: utf-8 -*-

################################### LIBRARIES ###############################################
from PyQt4 import QtCore, QtGui
import parametros
import icons_sofia_software_rc



# from vera_problems import Ui_Form
# import sys
#############################################################################################

################################### GLOBAL VARIABLES ########################################
Led_on = True
SERIAL_ON= True    
#############################################################################################

##################################  Error Treatment #########################################
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
#############################################################################################



####################################   Ui_SecDialog  ########################################
class Ui_SecDialog(object):
    def setupUi(self, SecDialog, vera_connect):
        self.vera_connect = vera_connect
        SecDialog.setObjectName(_fromUtf8("SecDialog"))
        SecDialog.resize(800, 480)
        SecDialog.setStyleSheet(_fromUtf8("background-color: black;"))
        #SecDialog.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.label_2 = QtGui.QLabel(SecDialog)
        self.label_2.setGeometry(QtCore.QRect(190, 20, 400, 40))
        self.label_2.setStyleSheet(_fromUtf8("font: 26pt \"Arial\";\n""color:rgb(255, 255, 255)"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(SecDialog)
        self.label_3.setGeometry(QtCore.QRect(70, 80, 191, 31))
        self.label_3.setStyleSheet(_fromUtf8("font: 18pt \"Arial\";\n""color: white;"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(SecDialog)
        self.label_4.setGeometry(QtCore.QRect(540, 80, 191, 31))
        self.label_4.setStyleSheet(_fromUtf8("font: 18pt \"Arial\";\n""color: white;"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(SecDialog)
        self.label_5.setGeometry(QtCore.QRect(310, 180, 191, 31))
        self.label_5.setStyleSheet(_fromUtf8("font: 18pt \"Arial\";\n""color: white;"))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.textBrowser = QtGui.QTextBrowser(SecDialog)
        self.textBrowser.setGeometry(QtCore.QRect(110, 370, 571, 81))
        self.textBrowser.setStyleSheet(_fromUtf8("border-style: outset;\n""border-width: 1px;\n""border-color: gray;"))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        self.label = QtGui.QLabel(SecDialog)
        self.label.setGeometry(QtCore.QRect(110, 345, 16, 16))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/leds/led_off_16x16.png")))
        self.label.setObjectName(_fromUtf8("label"))
        
        self.pushButton_Vera = QtGui.QPushButton(SecDialog)        # "Vera" comunication 
        self.pushButton_Vera.setGeometry(QtCore.QRect(130, 340, 120, 25))
        self.pushButton_Vera.setObjectName(_fromUtf8("pushButton_Vera"))
        self.pushButton_Vera.setStyleSheet(_fromUtf8("font: 16pt \"Arial\";\n""background-color: blue;color:white;\n""border-radius: 5px;"))

        self.pushButton_2 = QtGui.QPushButton(SecDialog) # "Power" Button 
        self.pushButton_2.setGeometry(QtCore.QRect(20, 400, 61, 51))
        self.pushButton_2.setStyleSheet(_fromUtf8("font: 20pt \"Arial\";\n""background-color: red;color:bla;\n""border-radius: 5px;"))
        self.pushButton_2.setText(_fromUtf8(""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        icon_power = QtGui.QIcon()
        icon_power.addPixmap(QtGui.QPixmap(_fromUtf8(":/operation_mode/power.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon_power)
        self.pushButton_2.setIconSize(QtCore.QSize(35, 35))

        self.pushButton_3 = QtGui.QPushButton("",SecDialog) # "?" Button 
        self.pushButton_3.setGeometry(QtCore.QRect(710, 400, 61, 51))
        self.pushButton_3.setStyleSheet(_fromUtf8("font: 34pt \"Arial\";\n""background-color: gray;color:bla;\n""border-radius: 5px;"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.pushButton_calibra = QtGui.QPushButton("",SecDialog) # "Calibracao" Button 
        self.pushButton_calibra.setGeometry(QtCore.QRect(710, 340, 61, 51))
        self.pushButton_calibra.setStyleSheet(_fromUtf8("font: 34pt \"Arial\";\n""background-color: gray;color:bla;\n""border-radius: 5px;"))
        self.pushButton_calibra.setObjectName(_fromUtf8("pushButton_calibra"))
        icon_calibration = QtGui.QIcon()
        icon_calibration.addPixmap(QtGui.QPixmap(_fromUtf8(":/operation_mode/calibration_mode.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_calibra.setIcon(icon_calibration)
        
        self.pushButton_calibra.setIconSize(QtCore.QSize(40,40))
        
        self.pushButton_4 = QtGui.QPushButton(SecDialog)  # "PreClinico" Button 
        self.pushButton_4.setGeometry(QtCore.QRect(290, 220, 221, 91))
        self.pushButton_4.setStyleSheet(_fromUtf8("font: 24pt \"Arial\";\n""background-color: purple;\n""border-radius: 5px;"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        icon_preclinico = QtGui.QIcon()
        icon_preclinico.addPixmap(QtGui.QPixmap(_fromUtf8(":/operation_mode/people.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon_preclinico)
        
        self.pushButton_4.setIconSize(QtCore.QSize(65,65))


        self.pushButton_5 = QtGui.QPushButton(SecDialog) # "Auto" Button 
        self.pushButton_5.setGeometry(QtCore.QRect(60, 120, 211, 91))
        self.pushButton_5.setStyleSheet(_fromUtf8("font: 18pt \"Arial\";\n""background-color: blue;\n""border-radius: 5px;"))
        self.pushButton_5.setText(_fromUtf8(""))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        icon_auto = QtGui.QIcon()
        icon_auto.addPixmap(QtGui.QPixmap(_fromUtf8(":/operation_mode/clock.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon_auto)
        self.pushButton_5.setIconSize(QtCore.QSize(65,65))

        self.pushButton_6 = QtGui.QPushButton(SecDialog)  # "Manual" Button 
        self.pushButton_6.setGeometry(QtCore.QRect(530, 120, 211, 91))
        self.pushButton_6.setStyleSheet(_fromUtf8("font: 18pt \"Arial\";\n""background-color: green;\n""border-radius: 5px;"))
        self.pushButton_6.setText(_fromUtf8(""))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        icon_manual = QtGui.QIcon()
        icon_manual.addPixmap(QtGui.QPixmap(_fromUtf8(":/operation_mode/set.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon_manual)
        self.pushButton_6.setIconSize(QtCore.QSize(65,65))

        self.timer = QtCore.QTimer(SecDialog)
        self.timer.timeout.connect(self.blink)
        self.timer.start(500)
        QtCore.QMetaObject.connectSlotsByName(SecDialog)
        self.retranslateUi()
        
        

    def retranslateUi(self):
        # self.setWindowTitle(QtGui.QApplication.translate("SecDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SecDialog", "MENU", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("SecDialog", "AUTOMÁTICO", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("SecDialog", "MANUAL", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("SecDialog", "PRÉ-CLÍNICO", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("SecDialog", "?", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Vera.setText(QtGui.QApplication.translate("SecDialog", "Vera", None, QtGui.QApplication.UnicodeUTF8))
        # self.pushButton_calibra.setText(QtGui.QApplication.translate("SecDialog", "C", None, QtGui.QApplication.UnicodeUTF8))

        self.textBrowser.setHtml(QtGui.QApplication.translate("SecDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.Helvetica Neue DeskInterface\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Automático - Escolha dentre as opções o modo dejesado para o procedimento de ablação.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Manual: Ajuste seus próprios parâmetros para o procedimento.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Pré-clínico: Entre com os dados médicos do paciente.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

        teste = QtCore.QObject.connect(self.pushButton_Vera, QtCore.SIGNAL("clicked()") , self.try_connect)


    def blink(self):
        if parametros.flag['veraFlag']:
            self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/leds/led_green_16x16.png")))
        else:
            self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/leds/led_red_16x16.png")))

    def try_connect(self):
        if (SERIAL_ON):
            print "Tentando conectar com o vera"
            self.vera_connect.serial_setup()
            connect = self.vera_connect.connect()
            if connect:
                print "Vera Conectado"
                self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/leds/led_green_16x16.png")))
                parametros.flag['veraFlag'] = True
                self.textBrowser.setHtml(QtGui.QApplication.translate("SecDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'.Helvetica Neue DeskInterface\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Vera Conectado!</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
                self.timer.stop()
            else:
                print "Vera Desconectado"
                parametros.flag['veraFlag'] = False
                self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/leds/led_red_16x16.png")))
                self.textBrowser.setHtml(QtGui.QApplication.translate("SecDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'.Helvetica Neue DeskInterface\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Problemas com a conexão com o Equipamento Vera.</span></p>\n", None, QtGui.QApplication.UnicodeUTF8))
                self.timer.stop()
            
        

#############################################################################################




####################################   Main  ################################################
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SecDialog = QtGui.QDialog()
    ui = Ui_SecDialog()
    ui.setupUi(SecDialog, None)
    SecDialog.show()
    sys.exit(app.exec_())
#############################################################################################
