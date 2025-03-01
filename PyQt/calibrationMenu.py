# -*- coding: utf-8 -*-

################################### LIBRARIES ###############################################
from PyQt4 import QtCore, QtGui
import parametros
import icons_sofia_software_rc



# from vera_problems import Ui_Form
# import sys
#############################################################################################

################################### GLOBAL VARIABLES ########################################

#############################################################################################

##################################  Error Treatment #########################################
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
#############################################################################################



####################################   Ui_CalibrationDialog  ########################################
class Ui_CalibrationDialog(object):
    def setupUi(self, CalibrationDialog):
        CalibrationDialog.setObjectName(_fromUtf8("CalibrationDialog"))
        CalibrationDialog.resize(800, 480)
        CalibrationDialog.setStyleSheet(_fromUtf8("background-color: black;"))
        self.label_2 = QtGui.QLabel(CalibrationDialog)
        self.label_2.setGeometry(QtCore.QRect(190, 20, 400, 40))
        self.label_2.setStyleSheet(_fromUtf8("font: 26pt \"Arial\";\n""color:rgb(255, 255, 255)"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(CalibrationDialog)
        self.label_3.setGeometry(QtCore.QRect(70, 80, 191, 31))
        self.label_3.setStyleSheet(_fromUtf8("font: 18pt \"Arial\";\n""color: white;"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(CalibrationDialog)
        self.label_4.setGeometry(QtCore.QRect(70, 250, 191, 31))
        self.label_4.setStyleSheet(_fromUtf8("font: 18pt \"Arial\";\n""color: white;"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(CalibrationDialog)
        self.label_5.setGeometry(QtCore.QRect(310, 180, 191, 31))
        self.label_5.setStyleSheet(_fromUtf8("font: 18pt \"Arial\";\n""color: white;"))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        
        self.textBrowser = QtGui.QTextBrowser(CalibrationDialog)
        self.textBrowser.setGeometry(QtCore.QRect(380, 120, 371, 250))
        self.textBrowser.setStyleSheet(_fromUtf8("border-style: outset;\n""border-width: 1px;\n""border-color: gray;"))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))


        self.pushButton_5 = QtGui.QPushButton(CalibrationDialog) # "Auto" Button 
        self.pushButton_5.setGeometry(QtCore.QRect(60, 120, 211, 91))
        self.pushButton_5.setStyleSheet(_fromUtf8("font: 18pt \"Arial\";\n""background-color: blue;\n""border-radius: 5px;"))
        self.pushButton_5.setText(_fromUtf8(""))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        icon_auto = QtGui.QIcon()
        icon_auto.addPixmap(QtGui.QPixmap(_fromUtf8(":/operation_mode/clock.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon_auto)
        self.pushButton_5.setIconSize(QtCore.QSize(65,65))

        self.pushButton_6 = QtGui.QPushButton(CalibrationDialog)  # "Manual" Button 
        self.pushButton_6.setGeometry(QtCore.QRect(60, 290, 211, 91))
        self.pushButton_6.setStyleSheet(_fromUtf8("font: 18pt \"Arial\";\n""background-color: green;\n""border-radius: 5px;"))
        self.pushButton_6.setText(_fromUtf8(""))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        icon_manual = QtGui.QIcon()
        icon_manual.addPixmap(QtGui.QPixmap(_fromUtf8(":/operation_mode/set.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon_manual)
        self.pushButton_6.setIconSize(QtCore.QSize(65,65))

        self.pushButton_back = QtGui.QPushButton(CalibrationDialog)
        self.pushButton_back.setGeometry(QtCore.QRect(550, 400, 161, 51))
        self.pushButton_back.setStyleSheet(_fromUtf8("font: 14pt \"MS Shell Dlg 2\";\n""background-color: red;\n""border-radius: 5px;\n""color: white;"))
        self.pushButton_back.setObjectName(_fromUtf8("pushButton_back"))


        QtCore.QMetaObject.connectSlotsByName(CalibrationDialog)
        self.retranslateUi()
        

    def retranslateUi(self):
        # self.setWindowTitle(QtGui.QApplication.translate("CalibrationDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CalibrationDialog", "Modos de Calibração", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("CalibrationDialog", "AUTOMÁTICO", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("CalibrationDialog", "MANUAL", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_back.setText(QtGui.QApplication.translate("self", "VOLTAR", None, QtGui.QApplication.UnicodeUTF8))

        self.textBrowser.setHtml(QtGui.QApplication.translate("SecDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.Helvetica Neue DeskInterface\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Para que este procedimento seja feito adequadamente, consulte nossos técnicos ou o manual do Sofia</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Automático - Os incrementos na tensão de referência serão ajustados via software.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Manual -  Insira a tensão de referência que desejar.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        

#############################################################################################




####################################   Main  ################################################
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    CalibrationDialog = QtGui.QDialog()
    ui = Ui_CalibrationDialog()
    ui.setupUi(CalibrationDialog)
    CalibrationDialog.show()
    sys.exit(app.exec_())
#############################################################################################
