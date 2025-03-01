# -*- coding: utf-8 -*-

################################### LIBRARIES ###############################################
from PyQt4 import QtCore, QtGui
import icons_sofia_software_rc
#############################################################################################



##################################  Error Treatment #########################################
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

############################################################################################

################################### UI_FORM ##############################################
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 133)
        qr2 = Form.frameGeometry()
        cp2 = QtGui.QDesktopWidget().availableGeometry().center()
        qr2.moveCenter(cp2)
        Form.move(qr2.topLeft())
        Form.setStyleSheet(_fromUtf8("font-weight:bold;background-color: gray;color: black"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 10, 221, 81))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(270, 90, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.setStyleSheet(_fromUtf8("font-weight:bold;font: \"Arial\";\n""background-color: rgb(40, 255, 0);color:white;\n""border-radius: 5px;"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 90, 99, 27))
        self.pushButton_2.setStyleSheet(_fromUtf8("font-weight:bold;font:\"Arial\";\n""background-color: red;color:white;\n""border-radius: 5px;"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 141, 101))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/general_icons/ask.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        QtCore.QMetaObject.connectSlotsByName(Form)

        

#############################################################################################

################################### MAIN ####################################################

# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     Form = QtGui.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())
#############################################################################################
