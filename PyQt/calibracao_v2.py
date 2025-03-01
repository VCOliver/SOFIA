# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from xlwt import Workbook
import math, time
import icons_sofia_software_rc


cont = 0
voltage_input = 0
var0 = 2

wb1 = Workbook()
sheet1 = wb1.add_sheet('sheet1')


RPI_ON = True
interrupt_flag = False

time_stamp = time.time() #Utilizada na Interrupt para Deboucing

if (RPI_ON):
    import RPi.GPIO as GPIO
    import smbus
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    # GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Pino de interrupção
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Pino de interrupção
    RELE_PIN1 = 23
    RELE_PIN2 = 24
    GPIO.setup(RELE_PIN1, GPIO.OUT) #Relé de Segurança
    GPIO.setup(RELE_PIN2, GPIO.OUT) #Relé de Segurança
    GPIO.output(RELE_PIN1, 0)       #ajusta os reles (nível alto) - Fechando relés
    GPIO.output(RELE_PIN2, 0)       #ajusta os reles (nível alto) - Fechando relés
    bus = smbus.SMBus(1)
    address1 = 0x48
    address2 = 0x49


for index in range(5):
    sheet1.col(index).width = 7000
sheet1.write(0,0,"Tabela de Calibracao")
sheet1.write(1,0,"Pot(Ref)")
sheet1.write(1,1,"Tensao")
sheet1.write(1,2,"Corrente")
sheet1.write(1,3,"Pot(Calculada)")

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

class Ui_autoDialog(object):

    def setupUi(self, autoDialog):

        autoDialog.setObjectName(_fromUtf8("autoDialog"))
        autoDialog.resize(800, 480)
        autoDialog.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);color: rgb(255,255,255);"))

        font = QtGui.QFont()
        font.setPointSize(18)
        autoDialog.setFont(font)

        self.label_2 = QtGui.QLabel(autoDialog)
        self.label_2.setGeometry(QtCore.QRect(240, 10, 301, 71))
        self.label_2.setStyleSheet(_fromUtf8("font: 26pt \"Arial\";\n""font-weight:bold;"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.lcdRef = QtGui.QLCDNumber(autoDialog)
        self.lcdRef.setGeometry(QtCore.QRect(120, 150, 130, 150))
        # self.lcdRef.setStyleSheet(_fromUtf8("border: 2px solid gray;\n""background-color: rgb(0, 0, 0);\n"))
        self.lcdRef.display(cont)
        self.lcdRef.setStyleSheet(_fromUtf8("background-color: blue;color:white"))
        self.lcdRef.setObjectName(_fromUtf8("lcdRef"))

        self.lcdVoltage = QtGui.QLCDNumber(autoDialog)
        self.lcdVoltage.setGeometry(QtCore.QRect(380, 110, 121, 81))
        self.lcdVoltage.setStyleSheet(_fromUtf8("background-color: blue;color:white"))

        self.lcdCurrent = QtGui.QLCDNumber(autoDialog)
        self.lcdCurrent.setGeometry(QtCore.QRect(380, 250, 121, 81))
        self.lcdCurrent.setStyleSheet(_fromUtf8("background-color: blue;color:white"))

        self.label_3 = QtGui.QLabel(autoDialog)
        self.label_3.setGeometry(QtCore.QRect(120, 120, 120, 21))
        self.label_3.setStyleSheet(_fromUtf8("font: 16pt \"Arial\";\n"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))


        self.label_4 = QtGui.QLabel(autoDialog)
        self.label_4.setGeometry(QtCore.QRect(620, 80, 91, 21))
        self.label_4.setStyleSheet(_fromUtf8("font: 16pt \"Arial\";\n"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))


        self.lcdPower = QtGui.QLCDNumber(autoDialog)
        self.lcdPower.setGeometry(QtCore.QRect(620, 110, 121, 81))
        self.lcdPower.setStyleSheet(_fromUtf8("border: 2px solid gray;\n""background-color: rgb(0, 0, 0);\n"))
        self.lcdPower.setStyleSheet(_fromUtf8("background-color: blue;color:white"))
        self.lcdPower.setObjectName(_fromUtf8("lcdPower"))
        self.lcdPower.display(cont)

        self.pushButton_5 = QtGui.QPushButton(autoDialog)
        self.pushButton_5.setGeometry(QtCore.QRect(250, 380, 151, 71))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_5.setStyleSheet("font-weight:bold;background-color: rgb(40, 255, 0); border-radius: 10px;")

        self.pushButton_6 = QtGui.QPushButton(autoDialog)
        self.pushButton_6.setGeometry(QtCore.QRect(420, 380, 151, 71))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_6.setStyleSheet("font-weight:bold;background-color: red; border-radius: 10px;")

        self.pushButton_2 = QtGui.QPushButton(autoDialog) # "Back" Button 
        self.pushButton_2.setGeometry(QtCore.QRect(20, 400, 61, 51))
        self.pushButton_2.setStyleSheet(_fromUtf8("font: 20pt \"Arial\";\n""background-color: red;color:bla;\n""border-radius: 5px;"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        icon_power = QtGui.QIcon()
        icon_power.addPixmap(QtGui.QPixmap(_fromUtf8(":/general_icons/back_button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon_power)
        self.pushButton_2.setIconSize(QtCore.QSize(35, 35))

        self.label_8 = QtGui.QLabel(autoDialog)
        self.label_8.setGeometry(QtCore.QRect(750, 180, 40, 13))
        self.label_8.setStyleSheet(_fromUtf8("font: 12pt \"Arial\";\n"))
        self.label_8.setObjectName(_fromUtf8("label_8"))

        self.label_9 = QtGui.QLabel(autoDialog)
        self.label_9.setGeometry(QtCore.QRect(390, 215, 100, 30))
        self.label_9.setStyleSheet(_fromUtf8("font: 16pt \"Arial\";\n"))
        self.label_9.setObjectName(_fromUtf8("label_9"))

        self.label_V = QtGui.QLabel(autoDialog)
        self.label_V.setGeometry(QtCore.QRect(390, 70, 100, 40))
        self.label_V.setStyleSheet(_fromUtf8("font: 16pt \"Arial\";\n"))
        self.label_V.setObjectName(_fromUtf8("label_V"))

        self.lcdTemp = QtGui.QLCDNumber(autoDialog)
        self.lcdTemp.setGeometry(QtCore.QRect(620, 250, 121, 81))
        self.lcdTemp.setStyleSheet(_fromUtf8("background-color: blue;color:white"))

        self.label_temp = QtGui.QLabel(autoDialog)
        self.label_temp.setGeometry(QtCore.QRect(620, 215, 120, 30))
        self.label_temp.setStyleSheet(_fromUtf8("font: 16pt \"Arial\";\n"))
        self.label_temp.setObjectName(_fromUtf8("label_V"))

        self.retranslateUi(autoDialog)
        self.timer = QtCore.QTimer(autoDialog)
        self.timer.timeout.connect(self.setPower)
        QtCore.QMetaObject.connectSlotsByName(autoDialog)

    def retranslateUi(self,autoDialog):
        self.label_2.setText(_translate("autoDialog", "Calibração ", None))
        self.label_3.setText(_translate("autoDialog", "Referência", None))
        self.label_4.setText(_translate("autoDialog", "Potência", None))
        self.pushButton_5.setText(_translate("autoDialog", "INICIAR", None))
        self.pushButton_6.setText(_translate("autoDialog", "PARAR", None))
        self.label_8.setText(_translate("autoDialog", "W", None))
        self.label_9.setText(_translate("autoDialog", "Corrente", None))
        self.label_V.setText(_translate("autoDialog", "Tensão", None))
        self.label_temp.setText(_translate("autoDialog", "Temperatura", None))

        QtCore.QObject.connect(self.pushButton_5 , QtCore.SIGNAL("clicked()") , self.iniciar_click)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL("clicked()") , self.parar_click)


    def iniciar_click(self):
        print '========== Calibração Iniciada ==========='
        self.timer.start(1000) #1 seconds
        self.target = open("calibracao_data.txt", 'w')
        self.target.write("================================= Nova Calibração Iniciada =================================\n")
        self.pushButton_5.setStyleSheet("font-weight:bold;background-color: red; border-radius: 10px;")
        # GPIO.add_event_detect(17, GPIO.RISING, callback=self.interrupt,bouncetime=10000)




    def parar_click(self):
        print'========== swithing off ADC ==========='
        global voltage_input,interrupt_flag
        self.pushButton_5.setStyleSheet("font-weight:bold;background-color: rgb(40, 255, 0); border-radius: 10px;")
        self.timer.stop()
        self.target.close()
        voltage_input = 0 
        self.lcdRef.display(voltage_input)
        interrupt_flag = False
        if (RPI_ON):
            GPIO.output(RELE_PIN1, 0)       #ajusta os reles (nível alto) - Fechando relés
            GPIO.output(RELE_PIN2, 0)       #ajusta os reles (nível alto) - Fechando relés
            try:
                bus.write_byte_data(address1, 0x44, 51)     #1.0 V

            except Exception, e:
                raise e
        


    def setPower(self):
       
        global cont, voltage_input, target, var0, sheet1, interrupt_flag
        # print cont 
        cont += 1
        self.lcdRef.display(voltage_input)

        # if cont == 5:
        print '========== set Power==========='
        # print cont 
        if (interrupt_flag):
            self.parar_click()        

        elif (RPI_ON):
            # print "oi"
            voltage_input += 1
            print "Tensão Ajustada: %d" %(voltage_input)
            self.lcdRef.display(voltage_input)

            if voltage_input > 36:
                print "Tensão Máxima - vamos acabar o processo, coleguinha!"
                self.parar_click()

            for x in xrange(0,10):
                try:
                    bus.write_byte(address2, 3)
                    bus.read_byte(address2)
                    dac_aux = bus.read_byte(address2)
                    dac_aux = dac_aux*5/255
                except Exception, e:

                    print "erro no DAC"

               
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
                    bus.write_byte_data(address1, 0x44, voltage_input*5 + 51)  # ajuste de 0.8 de offset
                    break
                except Exception, e:
                    # raise e
                    print"erro no DAC"
            

        # if cont == 7:
            print '========== Reading Power==========='

            for k in range (0,10):
                try:
                    # if (RPI_ON&~(interrupt_flag)):

                        #Leitura de Corrente
                        bus.write_byte(address2, 1)
                        bus.read_byte(address2)
                        current = bus.read_byte(address2)
                        current = current*5.0/255.0

                        #Leitura de Tensao
                        bus.write_byte(address2, 0)
                        bus.read_byte(address2)
                        voltage = bus.read_byte(address2)
                        voltage = voltage*5.0/255.0

                        #Leitura de Temperatura
                        bus.write_byte(address2, 2)
                        bus.read_byte(address2)
                        temperatura = bus.read_byte(address2)

                        impedancia = voltage/current
                        power =  voltage*current
                        
                        print "Corrente Lida: %.2f" %(current)
                        print "Tensão Lida: %.2f" %(voltage)
                        print "Potencia Lida: %.2f" %(power)
                        self.lcdCurrent.display(current)
                        self.lcdVoltage.display(voltage)
                        self.lcdTemp.display(temperatura)
                        self.lcdPower.display(power)

                        data = ('Vref: '+ str(voltage_input) + ' Vread: ' + str(voltage) + ' Cread: '+ str (current) + ' Pread: '  +str(power)+ '\n')
                        #Salvando valores na tabela excel
                        sheet1.write(var0,0,voltage_input)
                        sheet1.write(var0,1,voltage)
                        sheet1.write(var0,2,current)
                        sheet1.write(var0,3,power)
                        print "Index:" + str(var0)
                        var0 += 1   
                        self.target.write(data)
                        wb1.save('calibracao_alt.xls')
                        cont = 0
                        break
                except ZeroDivisionError:
                    impedancia =10E9
                except IOError as e:
                    print "ADC I/O ERRO({0}): {1}".format(e.errno, e.strerror)
        cont = 0
               
    def interrupt(self):
        # GPIO.remove_event_detect(17)
        global interrupt_flag
        print'========== Interrupção Acionada ==========='
        GPIO.output(RELE_PIN1, 0)        #ajusta os reles 
        GPIO.output(RELE_PIN2, 0)        # Abrindo relés

        print "Algum problema aconteceu, coleguinha!"
        interrupt_flag =  True

      
    # def interrupt(self):  
    #     global time_stamp       # put in to debounce  
    #     global interrupt_flag
    #     time_now = time.time()  
    #     if (time_now - time_stamp) >= 2:  #DEBOUNCING
    #         print "INTERRUPCAO DETECTADA!"  
    #         GPIO.output(RELE_PIN1, 0)        #ajusta os reles 
    #         GPIO.output(RELE_PIN2, 0)        # Abrindo relés
    #         interrupt_flag =  True
            
    #     time_stamp = time_now  
    
# if(RPI_ON):
#     #     print "interrupt"
#     # GPIO.add_event_detect(17, GPIO.FALLING, callback=interrupt)
#     #     # GPIO.add_event_detect(17, GPIO.RISING, callback=interrupt)
#     GPIO.add_event_detect(17, GPIO.RISING, callback=interrupt,bouncetime=10000)
#      # GPIO.add_event_detect(17, GPIO.BOTH, callback=interrupt)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    autoDialog = QtGui.QDialog()
    ui = Ui_autoDialog()
    ui.setupUi(autoDialog)
    autoDialog.show()
    sys.exit(app.exec_())
       
