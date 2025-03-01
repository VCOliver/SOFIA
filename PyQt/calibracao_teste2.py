# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'thirddialog.ui'
#
# Created: Wed Feb 24 15:04:30 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from xlwt import Workbook
import parametros
import math, time
import thread
from threading import Thread, Lock
import ctypes
import numpy as np 
#from scipy import signal
from numpy import convolve

var0 = 2

wb1 = Workbook()
sheet1 = wb1.add_sheet('sheet1')
voltage_save = 0
current_save = 0
voltage_filter = 0
current_filter = 0

RPI_ON = True
if (RPI_ON):
    import RPi.GPIO as GPIO
    import smbus
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Pino de interrupção
    RELE_PIN1 = 23
    RELE_PIN2 = 24
    GPIO.setup(RELE_PIN1, GPIO.OUT) #Relé de Segurança
    GPIO.setup(RELE_PIN2, GPIO.OUT) #Relé de Segurança
    GPIO.output(RELE_PIN1, 0)       #ajusta os reles (nível alto) - Fechando relés
    GPIO.output(RELE_PIN2, 0)       #ajusta os reles (nível alto) - Fechando relés
    bus = smbus.SMBus(1)
    address1 = 0x48
    address2 = 0x49

    #Teste controle AGC
    #Entrada de controle
    GPIO.setup(16,GPIO.OUT)
    GPIO.setup(20,GPIO.OUT)
    GPIO.setup(21,GPIO.OUT)
    #TESTE PRELIMINAR COM AGC FIXO EM 50 ohms
    GPIO.output(16,0) #LSB
    GPIO.output(20,1)
    GPIO.output(21,1) #MSB

for index in range(5):
    sheet1.col(index).width = 7000
sheet1.write(0,0,"Tabela de Calibracao")
sheet1.write(1,0,"Pot(Ref)")
sheet1.write(1,1,"Tensao")
sheet1.write(1,2,"Corrente")
sheet1.write(1,3,"Tensao Filtrada")
sheet1.write(1,4,"Corrente Filtrada")    


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

class Ui_manualDialog(object):

    def setupUi(self, thirdDialog):
        global voltage_input
        thirdDialog.setObjectName(_fromUtf8("thirdDialog"))
        thirdDialog.resize(800, 480)
        font = QtGui.QFont()
        font.setPointSize(18)
        thirdDialog.setFont(font)
        thirdDialog.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);color: rgb(255,255,255);"))


        self.label_2 = QtGui.QLabel(thirdDialog)
        self.label_2.setGeometry(QtCore.QRect(240, 10, 301, 71))
        self.label_2.setStyleSheet(_fromUtf8("font: 26pt \"Arial\";\n""font-weight:bold;"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.lcdNumber = QtGui.QLCDNumber(thirdDialog)
        self.lcdNumber.setGeometry(QtCore.QRect(80, 200, 121, 81))
        self.lcdNumber.setStyleSheet(_fromUtf8("border: 2px solid gray;\n""background-color: rgb(0, 0, 0);\n"))
        voltage_input = 0
        if (RPI_ON):
            try:
                bus.write_byte_data(address1, 0x44, voltage_input)     #1.0 V
            except Exception, e:
                raise e
        self.lcdNumber.display(voltage_input)
        self.lcdNumber.setStyleSheet(_fromUtf8("background-color: blue;color:white"))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))

        self.lcdVoltage = QtGui.QLCDNumber(thirdDialog)
        self.lcdVoltage.setGeometry(QtCore.QRect(380, 110, 121, 81))
        self.lcdVoltage.setStyleSheet(_fromUtf8("background-color: blue;color:white"))

        self.lcdCurrent = QtGui.QLCDNumber(thirdDialog)
        self.lcdCurrent.setGeometry(QtCore.QRect(380, 250, 121, 81))
        self.lcdCurrent.setStyleSheet(_fromUtf8("background-color: blue;color:white"))

        self.lcdNumber.setStyleSheet(_fromUtf8("background-color: blue;color:white"))
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
        # self.pushButton_2.setStyleSheet(_fromUtf8("border: 2px solid gray;\n""background-color: rgb(0, 0, 0);\n""color: rgb(0, 255, 0);\n""font: 30pt \"Arial\";"))
        self.pushButton_2.setStyleSheet("font-weight:bold;background-color: blue;border-radius: 10px;")


        self.label_3 = QtGui.QLabel(thirdDialog)
        self.label_3.setGeometry(QtCore.QRect(90, 290, 120, 21))
        # self.label_3.setStyleSheet(_fromUtf8("font: 16pt \"Times New Roman\";"))
        self.label_3.setStyleSheet(_fromUtf8("font: 16pt \"Arial\";\n"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.label_4 = QtGui.QLabel(thirdDialog)
        self.label_4.setGeometry(QtCore.QRect(650, 290, 91, 21))
        # self.label_4.setStyleSheet(_fromUtf8("font: 16pt \"Times New Roman\";"))
        self.label_4.setStyleSheet(_fromUtf8("font: 16pt \"Arial\";\n"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))


        self.lcdNumber_2 = QtGui.QLCDNumber(thirdDialog)
        self.lcdNumber_2.setGeometry(QtCore.QRect(620, 110, 121, 81))
        self.lcdNumber_2.setStyleSheet(_fromUtf8("border: 2px solid gray;\n""background-color: rgb(0, 0, 0);\n"))
        self.lcdNumber_2.setStyleSheet(_fromUtf8("background-color: blue;color:white"))
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))

        self.lcdNumber_2.display(voltage_input)

        self.pushButton_6 = QtGui.QPushButton(thirdDialog)
        self.pushButton_6.setGeometry(QtCore.QRect(450, 350, 151, 71))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_6.setStyleSheet("font-weight:bold;background-color: red; border-radius: 10px;")

        self.pushButton_7 = QtGui.QPushButton(thirdDialog) #x,y,w,h
        self.pushButton_7.setGeometry(QtCore.QRect(200, 350, 151, 71))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_7.setStyleSheet("font-weight:bold;background-color: green; border-radius: 10px;")        

        self.label_8 = QtGui.QLabel(thirdDialog)
        self.label_8.setGeometry(QtCore.QRect(620, 70, 120, 40))
        self.label_8.setStyleSheet(_fromUtf8("font: 13pt \"Arial\";\n"))
        self.label_8.setObjectName(_fromUtf8("label_8"))

        self.label_9 = QtGui.QLabel(thirdDialog)
        self.label_9.setGeometry(QtCore.QRect(390, 215, 100, 30))
        self.label_9.setStyleSheet(_fromUtf8("font: 16pt \"Arial\";\n"))
        self.label_9.setObjectName(_fromUtf8("label_9"))

        self.label_V = QtGui.QLabel(thirdDialog)
        self.label_V.setGeometry(QtCore.QRect(390, 70, 100, 40))
        self.label_V.setStyleSheet(_fromUtf8("font: 16pt \"Arial\";\n"))
        self.label_V.setObjectName(_fromUtf8("label_V"))

        self.lcdTemp = QtGui.QLCDNumber(thirdDialog)
        self.lcdTemp.setGeometry(QtCore.QRect(620, 250, 121, 81))
        self.lcdTemp.setStyleSheet(_fromUtf8("background-color: blue;color:white"))

        self.label_temp = QtGui.QLabel(thirdDialog)
        self.label_temp.setGeometry(QtCore.QRect(620, 215, 120, 30))
        self.label_temp.setStyleSheet(_fromUtf8("font: 13pt \"Arial\";\n"))
        self.label_temp.setObjectName(_fromUtf8("label_V"))

        self.retranslateUi(thirdDialog)
       
        QtCore.QMetaObject.connectSlotsByName(thirdDialog)

    def retranslateUi(self, thirdDialog):
        thirdDialog.setWindowTitle(_translate("thirdDialog", "Dialog", None))
        self.label_2.setText(_translate("thirdDialog", "Calibração Manual", None))
        self.pushButton.setText(_translate("thirdDialog", "+", None))
        self.pushButton_2.setText(_translate("thirdDialog", "-", None))
        self.label_3.setText(_translate("thirdDialog", "Referência", None))
        self.label_4.setText(_translate("thirdDialog", "P. Lida", None))
        self.pushButton_6.setText(_translate("thirdDialog", "PARAR", None))
        self.pushButton_7.setText(_translate("thirdDialog", "SALVAR", None))
        self.label_8.setText(_translate("thirdDialog", "Tensão Salva", None))
        self.label_9.setText(_translate("thirdDialog", "Corrente", None))
        self.label_V.setText(_translate("thirdDialog", "Tensão", None))
        self.label_temp.setText(_translate("thirdDialog", "Corrente Salva", None))

        QtCore.QObject.connect(self.pushButton , QtCore.SIGNAL("clicked()") , self.initial_button_Plus_click)
        QtCore.QObject.connect(self.pushButton_2 , QtCore.SIGNAL("clicked()") , self.initial_button_Minus_click)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL("clicked()") , self.parar_click)
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL("clicked()") , self.salva)


    def salva(self):
        global voltage_input, voltage_save, current_save, var0, sheet1, voltage_filter, current_filter

        self.lcdTemp.display(current_save)
        self.lcdNumber_2.display(voltage_save)

        #Salvando valores na tabela excel
        sheet1.write(var0,0,voltage_input)
        sheet1.write(var0,1,voltage_save)
        sheet1.write(var0,2,current_save)
        sheet1.write(var0,3,voltage_filter)
        sheet1.write(var0,4,current_filter)
        print "Index:" + str(var0)
        var0 += 1   
        wb1.save('Teste_save_data.xls')


    def initial_button_Plus_click(self):
        global voltage_input      
        if voltage_input<255:
            voltage_input +=1
        print voltage_input
        self.lcdNumber.display(voltage_input)
        self.setPower()

    def initial_button_Minus_click(self):
        global voltage_input       
        if voltage_input>0:
            voltage_input -=1
        print voltage_input
        self.lcdNumber.display(voltage_input)
        self.setPower()

    def parar_click(self):
        global voltage_input       
        print'========== swithing off ADC ==========='
        voltage_input = 0
        self.lcdNumber.display(voltage_input)
        if (RPI_ON):
            try:
                bus.write_byte_data(address1, 0x44, 0)     #1.0 V
            except Exception, e:
                raise e
        GPIO.output(RELE_PIN1, 0)       #ajusta os reles (nível alto) - Fechando relés
        GPIO.output(RELE_PIN2, 0)       #ajusta os reles (nível alto) - Fechando relés

    def setPower(self):
        global voltage_input    
        print '========== set Power==========='
        if (RPI_ON):
            for x in xrange(0,10):
                try:
                    bus.write_byte(address2, 3)
                    bus.read_byte(address2)
                    dac_aux = bus.read_byte(address2)
                    dac_aux = dac_aux*5/255
                    break
                    # print "Tensão no DAC: " + str(dac_aux)
                except Exception, e:
                    # raise e
                    print "erro no DAC"
                time.sleep(0.5)
               
            if dac_aux > 0.8:
                    GPIO.output(RELE_PIN1, 1)
                    GPIO.output(RELE_PIN2, 1)
                    print "RELE FECHADO"
            else:
                    print "RELE ABERTO"
                    GPIO.output(RELE_PIN1, 0)
                    GPIO.output(RELE_PIN2, 0)

            for x in xrange(0,10):
                try:
                    bus.write_byte_data(address1, 0x44, voltage_input)  # ajuste de 0.8 de offset
                    break
                except Exception, e:
                    # raise e
                    print"erro no DAC"
                time.sleep(0.5)

    def interrupt(self):
            global interrupt_flag
            print'========== Interrupção Acionada ==========='
            GPIO.output(RELE_PIN1, 0)        #ajusta os reles 
            GPIO.output(RELE_PIN2, 0)        # Abrindo relés

            print "Algum problema aconteceu, coleguinha!"
            interrupt_flag =  True
                
            
    #if(RPI_ON):
        #GPIO.add_event_detect(17, GPIO.FALLING, callback=interrupt)


def getPower(threadname, delay):

    global voltage_save, current_save, voltage_filter, current_filter

    while (1):

            voltage = 0;
            current = 0;
            dac_aux_bleh = 0 
            for k in range (0,10):
                try:
                    if (RPI_ON):
                        for x in range(0,10):
                            #Leitura de Tensao
                            bus.write_byte(address2, 0)
                            bus.read_byte(address2)
                            ADCvoltageTemp = bus.read_byte(address2)
                            voltage += ADCvoltageTemp*5.0/255.0
                        voltage = voltage/x
                        voltage_save = voltage
                        #b, a = signal.butter(3, 0.05)
                        voltage_filter = voltage_save#signal.filtfilt(b, a, voltage)
                        
                        for x in range(0,10):
                            #Leitura de Corrente
                            bus.write_byte(address2, 1)
                            bus.read_byte(address2)
                            ADCcurrentTemp = bus.read_byte(address2)
                            current += ADCcurrentTemp*50.0/255.0
                        current = current/x
                        current_save = current
                        #b, a = signal.butter(3, 0.05)
                        current_filter = current_save#signal.filtfilt(b, a, current)
                        #time.sleep(1)
                        #Leitura de Temperatura
                        #bus.write_byte(address2, 2)
                        #bus.read_byte(address2)
                        #temperatura = bus.read_byte(address2)

                        #Leitura de Tensão no DAC
                        #for x in range(0,10):
                            #bus.write_byte(address2, 3)
                            #bus.read_byte(address2)
                            #dac_auxTemp = bus.read_byte(address2)
                            #dac_aux_bleh += (dac_auxTemp*5/255.0)
                        #dac_aux_bleh = dac_aux_bleh/x

                        #impedancia = voltage/current
                        #power =  voltage*current
                        #parametros.todos['power'] = power
                        
                        ui.lcdCurrent.display(current)
                        ui.lcdVoltage.display(voltage)
                        #ui.lcdTemp.display(dac_aux_bleh)
                        #ui.lcdNumber_2.display(parametros.todos['power'])


                        break
                except ZeroDivisionError:
                    impedancia =10E9
                except IOError as e:
                    print "ADC I/O ERRO({0}): {1}".format(e.errno, e.strerror)
                time.sleep(0.5)
            time.sleep(1)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    thirdDialog = QtGui.QDialog()
    ui = Ui_manualDialog()
    ui.setupUi(thirdDialog)
    thirdDialog.show()
    
    t1 = Thread(target = getPower, args = ("GetPowerThread",1))
    t1.daemon = True
    t1.start()
    sys.exit(app.exec_())
       
