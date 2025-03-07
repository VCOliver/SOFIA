# -*- coding: utf-8 -*-

import os
import sys
from PyQt4.QtCore import pyqtSignal, QTimer
from PyQt4.QtGui import QApplication, QMainWindow, QPushButton
from PyQt4.QtGui import QLabel, QVBoxLayout, QWidget, QMessageBox, QDialog
from PyQt4 import QtCore, QtGui

current_dir = os.path.dirname(__file__)
codigo_dir = os.path.abspath(os.path.join(current_dir, '..'))
if codigo_dir not in sys.path:
        sys.path.insert(0, codigo_dir)

from mainwindow import Ui_MainWindow
from choosingScreen import Ui_SecDialog
from help_box import Ui_Dialog
from thirddialog import Ui_thirdDialog
from time_window import Ui_fourthDialog
from fifdialog import Ui_fifDialog
from step_configure import Ui_stepDialog
from temperature import Ui_temperatureDialog
from verification import Ui_VerifyWindow
from monidialog import Ui_moniDialog
from confirm_exit import Ui_Form
from error_window import Ui_errorDialog
from calibrationMenu import Ui_CalibrationDialog
from calibracao_v3 import  Ui_autoDialog
from calibracao_manual import Ui_manualDialog
import imagens2
import pylab_plot
import parametros

startProc = None
#RPI_ON = True 
RPI_ON = False



if RPI_ON:
    from serial_setup import Vera_Communication
    vera_connect = Vera_Communication()
else:
    vera_connect = None

# Classe da tela de iniciação do SOFIA


class LoadingWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.setOffsetVoltage()
        self.setupUi(self)
        self.retranslateUi(self)
        QTimer.singleShot(5000, self.newWindow)

    def setOffsetVoltage(self):
        if(RPI_ON):
            import smbus
            bus = smbus.SMBus(1)
            bus.write_byte_data(0x49, 0x44, 0) 

    def newWindow(self):
        self.close()
        self.mainwindow2 = OperationMode(self)
        self.mainwindow2.show()
        


# Mode of Operation
class OperationMode (QMainWindow, Ui_SecDialog):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self,vera_connect)
        self.retranslateUi()
        self.pushButton_2.clicked.connect(self.questionBox)
        self.pushButton_3.clicked.connect(self.help)
        self.pushButton_6.clicked.connect(self.power)
        self.pushButton_5.clicked.connect(self.auto)
        self.pushButton_calibra.clicked.connect(self.calibration)

    def questionBox(self):
        self.exit = Exit(self)
        self.exit.show()

    def help(self):
        self.otherwindow = Help(self)
        self.otherwindow.show()

    def power(self):  # Manual Mode
        parametros.flag['manualMode'] = True
        self.timer.stop()  # Stop LED from blinking
        self.close()
        self.power = PowerSetup(self)
        self.power.show()

    def auto(self):  # Automatic Mode
        parametros.flag['manualMode'] = False
        self.timer.stop()  # Stop LED from blinking
        self.close()
        self.automatic = Automatic(self)
        self.automatic.show()

    def calibration(self):  # Calibration Mode
        self.close()
        self.choosingCalibrate = SetCalibration(self)
        self.choosingCalibrate.show()


# Exit
class Exit(QDialog, Ui_Form):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.retranslateUi()
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.closeAll)

    def retranslateUi(self):
        self.label.setText("Tem certeza que deseja sair?")
        self.pushButton.setText("Sim")
        self.pushButton_2.setText("Cancelar")

    def closeAll(self):
        self.close()
        mainwindow2 = OperationMode(self)
        mainwindow2.close()
        os.system("sudo halt")


# Help
class Help(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.retranslateUi()
        self.pushButton_5.clicked.connect(self.close)


# Power Setup
class PowerSetup(QMainWindow, Ui_thirdDialog):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.retranslateUi()
        self.pushButton_off.clicked.connect(self.goBack)
        self.pushButton_5.clicked.connect(self.goTimer)

    def goBack(self):
        self.close()
        self.operationMode = OperationMode(self)
        self.operationMode.show()

    def goTimer(self):
        self.close()
        self.timerConfig = TimerSetup(self)
        self.timerConfig.show()


# Timer Setup
class TimerSetup(QMainWindow, Ui_fourthDialog):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.retranslateUi()
        self.pushButton_off.clicked.connect(self.goBack)
        self.pushButton_5.clicked.connect(self.goStep)

    def goBack(self):
        self.close()
        self.power = PowerSetup(self)
        self.power.show()

    def goStep(self):
        self.close()
        self.stepConfig = StepSetup(self)
        self.stepConfig.show()


# Step Setup
class StepSetup(QMainWindow, Ui_stepDialog):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.retranslateUi()
        self.pushButton_BACK.clicked.connect(self.goBack)
        self.pushButton_OK.clicked.connect(self.goTemperature)

    def goBack(self):
        self.close()
        self.timerConfig = TimerSetup(self)
        self.timerConfig.show()

    def goTemperature(self):
        self.close()
        self.temperatureMode = TemperatureSetup(self)
        self.temperatureMode.show()


# Temperature Setup
class TemperatureSetup(QMainWindow, Ui_temperatureDialog):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi()
        self.retranslateUi()
        self.pushButton.clicked.connect(self.goBack)
        self.pushButton_5.clicked.connect(self.goVerify)

    def goBack(self):
        if (parametros.flag['manualMode']):  # If in Manual Mode
            self.close()
            self.stepConfig = StepSetup(self)
            self.stepConfig.show()
        else:  # in Auto Mode
            self.close()
            self.automatic = Automatic(self)
            self.automatic.show()

    def goVerify(self):
        self.close()
        self.verifyMode = Verification(self)
        self.verifyMode.show()


# Verification Setup
class Verification(QMainWindow, Ui_VerifyWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.retranslateUi()
        self.pushButton_3.clicked.connect(self.goBack)
        self.pushButton.clicked.connect(self.goStart)

    def goBack(self):
        self.close()
        self.temperatureMode = TemperatureSetup(self)
        self.temperatureMode.show()

    def goStart(self):
        global startProc
        self.close()
        startProc = StartProcedure(self)
        startProc.show()


# Automatic Mode
class Automatic(QMainWindow, Ui_fifDialog):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.retranslateUi()
        self.pushButton_7.clicked.connect(self.goBack)
        self.pushButton_6.clicked.connect(self.goTemperature)

    def goBack(self):
        self.exit = ExitProcedure(self)
        self.exit.show()
        self.close()
        self.operationMode = OperationMode(self)
        self.operationMode.show()

    def goTemperature(self):
        self.close()
        self.temperatureMode = TemperatureSetup(self)
        self.temperatureMode.show()

class SetCalibration(QMainWindow, Ui_CalibrationDialog):
  def __init__(self, parent=None):
      QMainWindow.__init__(self, parent)
      self.setupUi(self)
      self.retranslateUi()
      self.pushButton_6.clicked.connect(self.goManualCalibrate)
      self.pushButton_5.clicked.connect(self.goAutoCalibrate)
      self.pushButton_back.clicked.connect(self.goBack)

  def goManualCalibrate(self):
      # self.close()
      # self.manualCalibrate = ManualCalibration(self)
      # self.manualCalibrate.show()
      os.system("sudo /usr/bin/python /home/pi/PyQt/calibracao_teste_filtro.py")

  def goAutoCalibrate(self):
      self.close()
      self.autoCalibrate = AutoCalibration(self)
      self.autoCalibrate.show()

  def goBack(self):
      self.close()
      self.operationMode = OperationMode(self)
      self.operationMode.show()


class AutoCalibration(QMainWindow, Ui_autoDialog):
  def __init__(self,parent=None):
      QMainWindow.__init__(self, parent)
      self.setupUi(self)
      self.retranslateUi(self)
      self.pushButton_2.clicked.connect(self.goBack)

  def goBack(self):
      self.close()
      self.choosingCalibrate = SetCalibration(self)
      self.choosingCalibrate.show()

class ManualCalibration(QMainWindow, Ui_manualDialog):
  def __init__(self, parent=None):
      QMainWindow.__init__(self, parent)
      self.setupUi(self)
      self.retranslateUi(self)
      self.pushButton_back.clicked.connect(self.goBack)

  def goBack(self):
      self.close()
      self.choosingCalibrate = SetCalibration(self)
      self.choosingCalibrate.show()


class StartProcedure(QMainWindow, Ui_moniDialog):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self,vera_connect)
        self.retranslateUi()
        self.pushButton_8.clicked.connect(self.goBack)  # Desligar

    def goBack(self):
        self.exitOp = ExitProcedure(self)   # Abrir janela de verificação
        self.exitOp.show()  # Mostrar janela

    def goError(self):
        self.timer.stop()  # para a função de controle
        self.resetParameters()  # Resetar parametros
        self.error = ErrorWindow(self)
        self.error.show()

    def goEnd(self):
        self.timer.stop()  # para a função de controle
        self.resetParameters()  # Resetar parametros
        end = EndWindow(self)
        end.show()


class ErrorWindow(QMainWindow, Ui_errorDialog):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.retranslateUi()
        self.pushButton_5.clicked.connect(self.closeAll)  # OK

    def closeAll(self):
        self.close()
        goOperational = OperationMode(self)
        goOperational.show()
        # os.system("sudo halt")


# Exit Procedure
class ExitProcedure(QMainWindow, Ui_Form):
    global startProc

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.retranslateUi()
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.closeAll)

    def retranslateUi(self):
        self.label.setText("<html>Tem certeza que deseja finalizar<br> o procedimento?<\html>")
        self.pushButton.setText("Sim")
        self.pushButton_2.setText("Cancelar")

    def closeAll(self):
        self.close()  # Fecha a janela de confirmação
        # mainwindow2 = StartProcedure(self)
        startProc.timer.stop()  # para a função de controle
        startProc.resetParameters()  # Resetar parametros
        startProc.close()   # Fecha a janela de procedimento
        self.mainwindow2 = OperationMode(self)
        self.mainwindow2.show()  # Mostra a janela de escolha do modo de op.


class EndWindow(QMainWindow, Ui_errorDialog):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.retranslateUi()
        self.pushButton_5.clicked.connect(self.closeAll)  # OK

    def retranslateUi(self):
        try:
            _encoding = QApplication.UnicodeUTF8

            def _translate(context, text, disambig):
                return QApplication.translate(
                    context, text, disambig, _encoding)
        except AttributeError:
            def _translate(context, text, disambig):
                return QApplication.translate(context, text, disambig)
        self.pushButton_5.setText(_translate("Dialog", "OK", None))
        self.setWindowTitle(_translate("Atenção Erro", "Atenção", None))
        if parametros.flag['endOfOperation']:
            self.label_config_infos.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"\OPERAÇÃO FINALIZADA!!</span><p align=\"center\"><span style=\" font-size:12pt;\">O tempo de operação chegou ao fim!!</span></p></body></html>", None))
        else:
            self.label_config_infos.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">OPERAÇÃO FINALIZADA!!</span><p align=\"center\"><span style=\" font-size:12pt;\">O sistema reconheceu temperatura máxima <br>durante o procedimento de ablação!!</span></p></body></html>", None))

    def closeAll(self):
        self.close()
        opMode = OperationMode(self)
        opMode.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = LoadingWindow()
    ui.show()
    sys.exit(app.exec_())