# -*- coding: utf-8 -*-

#from __future__ import division
from PyQt4 import QtCore, QtGui
from xlwt import Workbook
import sys
import parametros
import controller
import time
import math
import os
import logging
import PID
import numpy as np 
from scipy import signal
from numpy import convolve
#from serial_setup import Vera_Communication

# import Adafruit_ADS1x15

# adc = Adafruit_ADS1x15.ADS1115()
adc = None

GAIN = 2/3

# import RPi.GPIO as GPIO
# import smbus
# #setando GPIOs utilizados
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)

#---------------------------------------------------------------------------------------
#configurando arquivo de log
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
#criando handler file
handler = logging.FileHandler('Teste.log')
handler.setLevel(logging.INFO)
#Formatacao das mensagens de log
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

#configurando o Log para printar no terminal
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
#---------------------------------------------------------------------------------------

#if rasp conectado
RPI_ON = False 
pause = False

if (RPI_ON):
    
    RELE_PIN1 = 16
    GPIO.setup(RELE_PIN1, GPIO.OUT) #Relé de Segurança
    GPIO.output(RELE_PIN1, 0)       #ajusta os reles (nível alto) - Fechando relés
    

#-------------------------------------------------------------------------------------
#planilha no excel com os parametros do sistema
#criada com a finalidade de calibrar os parametros

# variavel de escrita na planilha de dados   
excel_var = 2

wb1 = Workbook()
sheet1 = wb1.add_sheet('sheet1')

for index in range(8):
    sheet1.col(index).width = 7000
sheet1.write(0,2,"Tabela de Calibracao")
sheet1.write(1,0,"Minuto")
sheet1.write(1,1,"Segundo")
sheet1.write(1,2,"DAC")
sheet1.write(1,3,"Tensao")
sheet1.write(1,4,"Corrente")
sheet1.write(1,5,"Potencia")
sheet1.write(1,6,"Impedancia")
sheet1.write(1,7,"Temperatura")


#-------------------------------------------------------------------------------------
#variaveis de contagem do tempo de operação
time_before= 0
time_beginning = 0
minute = 0
seconds = 0
stop_press = 1
initial_press = 1
time_old = 0
restart = 0
time_off = 0
time_now = 0
cont = 0
teste = 22
first_2_seconds = 0

#--------------------------------------------------------------------------------------
#flag de monitoramento de erro
parametros.flag['callErrorWindow'] = False

#Parametros do PID
P = 0.20928  
I = 0.59511
D= 0.18399
#P=0.5
#I=0.5
#D=0
pid = PID.PID(P, I, D)

#variavel utilizada para gerar o valor de tensao a ser enviado no DAC
#afim de gerar a potencia desejada na carga
actuatorValue = 0

if (RPI_ON):
    #variaveis de endereçamento dos PCF's
    bus = smbus.SMBus(1)
    #endereço do DAC (escrita)
    address1 = 0x49
    #endereço do ADC (leitura)
    #address2 = 0x48

#------------------------------------------------------------------------------------------
#codigo de interface do QT
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

class Ui_moniDialog(object):
    def setupUi(self, moniDialog,vera_connect):
    	self.vera_connect = vera_connect
        self.setObjectName(_fromUtf8("moniDialog"))
        self.resize(800, 480)
        #self.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);color:white"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(170, 50, 441, 71))
        self.label_2.setStyleSheet(_fromUtf8("font: 22pt \"Arial\";font-weight:bold;"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_14 = QtGui.QLabel(self)
        self.label_14.setGeometry(QtCore.QRect(760, 240, 47, 13))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(_fromUtf8("font: 75 12pt \"Arial\";"))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self)
        self.label_15.setGeometry(QtCore.QRect(168, 280, 500, 90))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_15.setStyleSheet("font-weight:bold;")
        self.pushButton_7 = QtGui.QPushButton(self)
        self.pushButton_7.setGeometry(QtCore.QRect(450, 400, 181, 51))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_7.setStyleSheet("font-weight:bold;background-color: green;border-radius: 10px;")
        self.label_20 = QtGui.QLabel(self)
        self.label_20.setGeometry(QtCore.QRect(550, 240, 55, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet(_fromUtf8("font: 75 12pt \"Arial\";"))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.lcd_tempo = QtGui.QLCDNumber(self)
        self.lcd_tempo.setGeometry(QtCore.QRect(640, 180, 111, 81))
        self.lcd_tempo.setStyleSheet(_fromUtf8("background-color: blue;"))
        self.lcd_tempo.setObjectName(_fromUtf8("lcd_tempo"))
        self.pushButton_8 = QtGui.QPushButton(self)
        self.pushButton_8.setGeometry(QtCore.QRect(160, 400, 181, 51))
        self.pushButton_8.setStyleSheet(_fromUtf8("font-weight:bold;background-color: blue;border-radius: 10px;"))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.lcd_temp = QtGui.QLCDNumber(self)
        self.lcd_temp.setGeometry(QtCore.QRect(430, 180, 111, 81))
        self.lcd_temp.setStyleSheet(_fromUtf8("background-color: blue;"))
        self.lcd_temp.setObjectName(_fromUtf8("lcd_temp"))
        self.lcd_imp = QtGui.QLCDNumber(self)
        self.lcd_imp.setGeometry(QtCore.QRect(220, 180, 111, 81))
        self.lcd_imp.setStyleSheet(_fromUtf8("alternate-background-color: rgb(0, 0, 0);background-color: blue;"))
        self.lcd_imp.setObjectName(_fromUtf8("lcd_imp"))
        self.label_23 = QtGui.QLabel(self)
        self.label_23.setGeometry(QtCore.QRect(150, 240, 55, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet(_fromUtf8("font: 75 12pt \"Arial\";"))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.label_24 = QtGui.QLabel(self)
        self.label_24.setGeometry(QtCore.QRect(340, 240, 55, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet(_fromUtf8("font: 75 12pt \"Arial\";"))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.lcd_potencia = QtGui.QLCDNumber(self)
        self.lcd_potencia.setGeometry(QtCore.QRect(30, 180, 111, 81))
        self.lcd_potencia.setStyleSheet(_fromUtf8("background-color:blue;"))
        self.lcd_potencia.setObjectName(_fromUtf8("lcd_potencia"))
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.control)

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("moniDialog", "Dialog", None))
        self.label_2.setText(_translate("moniDialog", "TELA DE MONITORAMENTO", None))
        self.label_14.setText(_translate("moniDialog", "min", None))

        self.pushButton_7.setText(_translate("moniDialog", "INICIAR ", None))
        self.label_20.setText(_translate("moniDialog", "ºC", None))
        self.pushButton_8.setText(_translate("moniDialog", "MENU INICIAL", None))
        self.label_23.setText(_translate("moniDialog", "W", None))
        self.label_24.setText(_translate("moniDialog", "Ω", None))
        QtCore.QObject.connect(self.pushButton_7 , QtCore.SIGNAL("clicked()") , self.start)
        self.lcd_temp.display("---")
        self.lcd_imp.display("---")
        self.label_15.setText(_translate("moniDialog", "Modo de Operação: Aguardando INICIAR", None))
        self.lcd_potencia.display(parametros.todos['potenciaInicial'])
       

#---------------------------------------------------------------------------------------------------------

    #Metodo de controle
    def control(self):
        #variaveis de contagem do tempo
        global time_before, time_beginning, minute, seconds, stop_press, initial_press,time_old, restart, time_off, time_now, cont,old_impedance
        global first_2_seconds, excel_var,GAIN
        global pause
        if(not(pause)):
            if(RPI_ON):
                global bus, address, actuatorValue
            self.pushButton_7.setText(_translate("moniDialog", "PARAR ", None))
            self.pushButton_7.setStyleSheet("font-weight:bold;background-color: red;border-radius: 10px;")
            
            ADCvoltage = 0
            ADCcurrent = 0
            temperature = 0
            GAIN = 2/3

            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)

            #bus.write_byte_data(address1, 0x44, 0)
            GPIO.output(RELE_PIN1, 1)
            

            cont += 1

#---------------------------------------------------------------------------------------------------------
            if cont == 500:

                if(RPI_ON):
                    ADCvoltage = 0
                    ADCcurrent = 0
                    voltage_filtrada = 0
                    current_filtrada = 0
                    dac_aux = 0
                    voltage_filter=[0 for i in range(15)]
                    current_filter=[0 for i in range(15)]

                    for x in xrange(0,10):
                        try:
                            for var0 in range(0,15):
                                #Leitura de Tensão
                                ADCvoltageTemp = adc.read_adc(0, gain=GAIN)
                                voltage_filter[var0] = ADCvoltageTemp
                                ADCvoltage += ADCvoltageTemp
                            callErrorWindow = False
                            ADCvoltage = ADCvoltage/(var0+1)
                            b, a = signal.butter(3, 0.05)
                            voltage_filter_media = signal.filtfilt(b, a, voltage_filter)
                            for var0 in range(0,15):
	                            voltage_filtrada += voltage_filter_media[var0]
                            voltage_filtrada = voltage_filtrada/(var0+1)

                            break #sai do for se chegar aqui
                        except Exception, e:
                            logger.error('Erro na leitura ADC Tensao', exc_info=True)
                            callErrorWindow = True

                    if(callErrorWindow):
                        logger.error('Nao foi possivel realizar a leitura da Tensao - ADC')
                        GPIO.cleanup()
                        self.goError()

                    for x in xrange(0,10):
                        try:
                            for var0 in range(0,15):
                                #Leitura de corrente
                                ADCcurrentTemp = adc.read_adc(1, gain=GAIN)
                                current_filter[var0] = ADCcurrentTemp
                                ADCcurrent += ADCcurrentTemp
                            callErrorWindow = False
                            ADCcurrent = ADCcurrent/(var0+1)
                            b, a = signal.butter(3, 0.05)
                            current_filter_media = signal.filtfilt(b, a, current_filter)
                            for var0 in range(0,15):
	                            current_filtrada += current_filter_media[var0]
                            current_filtrada = current_filtrada/(var0+1)

                            break #sai do for se chegar aqui
                        except Exception, e:
                            logger.error('Erro na leitura ADC Corrente', exc_info=True)
                            callErrorWindow = True

                    if(callErrorWindow):
                        logger.error('Nao foi possivel realizar a leitura da Corrente - ADC')
                        GPIO.cleanup()
                        self.goError()


                    for x in xrange(0,10):
                        try:
                            for var0 in range(0,15): #Leitura de Temperatura
                                temp_aux = adc.read_adc(2, gain=GAIN)
                                temperature += temp_aux
                            temperature = float(temperature)/(var0+1)
                            temperature = 0.0044*temperature-6.216
                            self.lcd_temp.display(temperature)
                            callErrorWindow = False
                            break #sai do for se chegar aqui
                        except Exception, e:
                            logger.error('Erro na leitura ADC Temperatura', exc_info=True)
                            callErrorWindow = True

                    if(callErrorWindow):
                        logger.error('Nao foi possivel realizar a leitura da Temperatura - ADC')
                        GPIO.cleanup()
                        self.goError()

                    #tempo = minute*60 + seconds
                    #temperature = 0.000008*tempo*tempo*tempo - 0.004*tempo*tempo + 0.885*tempo +16.37
                    #if(tempo!=0):
                    	#temperature = 17.95*np.log(tempo) - 25.43
                    #self.lcd_temp.display(temperature)

                    #valor de tensao estimada na carga
                    if(parametros.todos['potenciaRT'] >= 5 and parametros.todos['potenciaRT'] <20):
                    #5w
                        voltage = 0.0061*voltage_filtrada + 10.008 #controller.getInterpVoltage(ADCvoltage,old_impedance)
          
                        #valor de corrente estimada na carga
                        current = 0.00004*current_filtrada + 0.0692 #controller.getInterpCurrent(ADCcurrent,old_impedance)

                    if(parametros.todos['potenciaRT'] >= 20 and parametros.todos['potenciaRT'] <= 30):
                        voltage = 0.0056*voltage_filtrada + 12.58 #controller.getInterpVoltage(ADCvoltage,old_impedance)
          
                        #valor de corrente estimada na carga
                        current = 0.00004*current_filtrada + 0.0151

                    if(parametros.todos['potenciaRT'] > 30):
                        voltage = 0.006*voltage_filtrada + 3.1099 #controller.getInterpVoltage(ADCvoltage,old_impedance)
          
                        #valor de corrente estimada na carga
                        current = 0.00004*current_filtrada + 0.0125
                    
                    print "Vera flag: " + str(parametros.flag['veraFlag'])
                    if(parametros.flag['veraFlag']):
                    	self.vera_connect.write_data(voltage,current,temperature)
                    	print "Mandou pro Vera"
                    else:
                   		print "Nao mandou pro Vera"

                    #controller.mapo(voltage,0,255,0,5)
                    #controller.mapo(current,0,255,0,5)
       	            impedance = controller.getImpedance(voltage,current) #calculando impedancia
                
                    print "Voltage: " + str(voltage)
                    print "Current: " + str(current)

                    #potencia estimada na carga
                    power =  controller.getPower(voltage,current) #calculando potencia
                    self.lcd_imp.display(impedance) #Print Impedancia
                    self.lcd_potencia.display(power) #Print power
                    pid.SetPoint = controller.voltageDACalc(parametros.todos['potenciaRT'],voltage,current)
                    pid.setSampleTime(0.01)

                	#CONTROLE DE TENSAO
                	#Calculando o novo valor de tensao que deve ser colocado


    				#tensao desejada
                    #newVoltage = controller.voltageDACalc(parametros.todos['potenciaRT'],voltage,current)
                	
                	
                    #END = 1
                    #tensao na carga
                    feedback = voltage
                    #nova tensao a ser enviada no DAC afim de corrigir a potencia
                    #for i in range(1, END):
                    pid.update(feedback)
                    measuredError = pid.outp
                    absError = abs(measuredError)
                    errorBits = int(absError)

                    smallestError = 0.02

                    #testa se o erro esta em um range aceitavel e o atribui para a variavel "increment"
                    if (absError<smallestError): #Erro menor que resolucao
                    	increment = 0 #Nada a fazer aqui
                    else: #Erro pode ser corrigido
					  if(absError>=255): #Caso o erro seja maior do que a saída máx. do DAC
					     errorBits = 255
					     #errorBits = 2
					     increment = errorBits
					  elif(measuredError > 0.0): #Erro positivo
					     print "Positive Error!"
					     increment = errorBits
					  elif(measuredError < 0.0): #Erro negativo
					     print "Negative Error!"
					     increment = -errorBits
					  else:
					     increment = 0
					

                    #actuatorValue += controller.errorCalc(voltage,newVoltage)
                    actuatorValue += increment
                    #actuatorValue = 52
                    print "Atuador: " + str(increment)
                    print "DAC: " +str(actuatorValue)
                    if (actuatorValue < 0):
                        actuatorValue = 0
                    elif(actuatorValue>150):
                        actuatorValue = 150
                    else:
                        pass
                    #atualização do valor de tensão no DAC
                    if(RPI_ON):
                        for x in xrange(0,10):
                            try:
                                bus.write_byte_data(0x49, 0x44, actuatorValue)
                                DAC_volts = float(actuatorValue)*5/255
                                print "DAC: " +str(actuatorValue) #depois das condicoes
                                callErrorWindow = False
                                break #sai do for se chegar aqui
                            except Exception, e:
                                logger.error('Erro na escrita do DAC', exc_info=True)
                                callErrorWindow = True

                        if(callErrorWindow):
                            logger.error('Nao foi possivel realizar a escrita no DAC')
                            GPIO.cleanup()
                            self.goError()

                #CONTROLE DE TEMPERATURA
                    #if (controller.controlTemperature(temperature)):
                        #GPIO.output(19,1)                     #ATIVAR RELÉ DE TEMPERATURA
                        #print "TEMPERATURA MÁXIMA"
                        #logger.warn('Temperatura muito alta - %s',temperature)
                        #self.goEnd()
                        # self.timer.stop()
                    #else:
                        #print "TEMPERATURA OK!"
                        #GPIO.output(19,0)                     #DESATIVAR RELÉ DE IMPEDÂNCIA

#---------------------------------------------------------------------------------------------------

            if restart == 0:
                time_now = time.time() - time_off
                seconds = round(time_now - time_beginning,0)
                if minute == 0: # Só atualiza esta variavel nos primeiros dois segundos de operação
                    first_2_seconds = seconds

            if restart == 1 :
                time_off = time.time() - time_old   #duracao do botao desligado
                time_now = time_old                  #ultimo tempo no qual botao foi desligado
                seconds = round(time_now - time_beginning,0)
                restart = 0
                time_old = 0

            stop_press = seconds
            if seconds >= 60:
                minute +=1
                seconds = 0
                time_beginning = time_now
            if seconds < 10:
                str_count = str(minute) + ':0' + str(int(seconds))

            else:
                str_count = str(minute) + ':' + str(int(seconds))
            self.lcd_tempo.display(str_count)

            
            if ( time_now - time_before > float(parametros.todos['tempoStep']*60) ):
                print "TEMPO DE STEP"
                if (minute >= parametros.todos['tempo']):
                    print "FIM DA OPERAÇÃO"
                    self.timer.stop() #"Desligar"
                    parametros.flag['endOfOperation'] = True # Flag do fim da operacao
                    self.goEnd()
                else:
                    parametros.todos['potenciaRT'] += parametros.todos['potenciaStep']
                time_before = time_now #Atualizar contagem

#--------------------------------------------------------------------------------------------------

            #CONTROLE DE IMPEDÂNCIA
            if cont == 500: #Esta verificacao é feita a cada 60 ms
                #if(controller.controlImpedance(impedance)):
                    #print "IMPEDANCIA MUITO ALTA/BAIXA"
                    #logger.warn('Nivel de Impedancia muito Alto/Baixo - %s',impedance)
                    #GPIO.output(RELE_PIN1,0)         #ATIVAR RELÉ DE POTÊNCIA (DESLIGAR APARELHO)
                    #self.timer.stop() #"Desligar"
                #else:
                    #print "IMPEDANCIA OK!"
                    #GPIO.output(RELE_PIN1,1)         #DESATIVAR RELÉ DE POTÊNCIA (DESLIGAR APARELHO)

                sheet1.write(excel_var,0,minute)
                sheet1.write(excel_var,1,seconds)
                sheet1.write(excel_var,2,DAC_volts)
                sheet1.write(excel_var,3,voltage)
                sheet1.write(excel_var,4,current)
                sheet1.write(excel_var,5,power)
                sheet1.write(excel_var,6,impedance)
                sheet1.write(excel_var,7,temperature)
              
                wb1.save('Protocolo.xls')
                excel_var += 1

                cont = 0
                print "Tempo: " + str(minute)+ ":" +str(int(seconds))
                print "__________________________________"
        else:
            self.timer.stop()
            self.resetParameters()     #coloca as variaveis no padrao default
            self.goError()

#-------------------------------------------------------------------------------------------------

    def stop(self):
        global time_before, stop_press,initial_press, time_old,restart,time_off,time_now
        logger.info('Operação pausada')
        logger.info('Potencia RT: %s  Tempo: %s  Modo: %s',parametros.todos['potenciaRT'],parametros.todos['tempo'],parametros.todos['modo'])
        self.pushButton_7.setText(_translate("moniDialog", "INICIAR ", None))
        self.pushButton_7.setStyleSheet("font-weight:bold;background-color: green;border-radius: 10px;")
        time_old = time_now
        self.timer.stop()

        #seta as flags usadas
        time_off = 0
        stop_press = 1
        initial_press = 0
        restart = 1

#-------------------------------------------------------------------------------------------------

    def start(self):
        global time_before,time_beginning,stop_press, initial_press,pwm_pin1
        global RPI_ON
        
        global pause

        read = 0
        if read:
            pause = True
        logger.info('Operação iniciada')
        logger.info('Potencia Inicial: %s  Potencia Final: %s  Step de Potencia: %s  Tempo: %s  Step de Tempo: %s  Modo: %s',parametros.todos['potenciaInicial'],parametros.todos['potenciaFinal'],parametros.todos['potenciaStep'],parametros.todos['tempo'],parametros.todos['tempoStep'],parametros.todos['modo'])
        # if(parametros.flag['veraFlag']):
	       #  self.vera_connect.serial_setup()
        if((initial_press == 0) and (stop_press == 1)) :               #condicao para reiniciar a contagem
            self.timer.start(1) #1 miliseconds

        if ((initial_press == 1) and (stop_press == 1)):                #condicao para o primeiro acionamento
        	if(parametros.flag['manualMode']):
        		self.label_15.setText(_translate("moniDialog", "Modo de Operação: Manual", None))
        		self.label_15.setGeometry(QtCore.QRect(220, 280, 500, 90))
        		#self.label_15.setGeometry(QtCore.QRect(168, 280, 500, 90))
        	else:
        		self.label_15.setText(_translate("moniDialog", "Modo de Operação: " + str (parametros.todos['modo']), None))
        		self.label_15.setGeometry(QtCore.QRect(280, 280, 300, 90))
        	time_before = time.time()
        	time_beginning = time_before
        	self.timer.start(1) #1 miliseconds

        if stop_press != 1:                                             #condicao para parar a contagem
            self.stop()
            GPIO.output(RELE_PIN1,0)
            if(RPI_ON):
                for x in xrange(0,10):
                    try:
                        bus.write_byte_data(address1, 0x44, 0)

                        callErrorWindow = False
                        break #sai do for se chegar aqui
                    except Exception, e:
                        logger.error('Erro na escrita do DAC', exc_info=True)
                        callErrorWindow = True

                if(callErrorWindow):
                    logger.error('Nao foi possivel realizar a escrita no DAC')
                    GPIO.cleanup()
                    self.goError()

#-----------------------------------------------------------------------------------------------------------

    def resetParameters(self):
        global time_before,time_beginning,minute,stop_press,initial_press,time_old,restart,time_off,time_now
        global first_pause,pause

        # Set Offset Voltage
        if(RPI_ON):
            for x in xrange(0,10):
                try:
                    GPIO.output(RELE_PIN1, 0)
                    bus.write_byte_data(address1, 0x44, 0)
                    callErrorWindow = False
                    break #sai do for se chegar aqui
                except Exception, e:
                    logger.error('Erro na escrita do DAC', exc_info=True)
                    callErrorWindow = True

            if(callErrorWindow):
                logger.error('Nao foi possivel realizar a escrita no DAC')
                GPIO.cleanup()
                self.goError()

        time_before= 0
        time_beginning = 0
        minute = 0
        stop_press = 1
        initial_press = 1
        time_old = 0
        restart = 0
        time_off = 0
        time_now = 0

        first_pause = True
        pause = False

        m1 = 0 #Indice para valores default
        parametros.todos['modo'] = parametros.modo[m1]
        parametros.todos['potenciaInicial'] = parametros.potenciaInicial[1]
        parametros.todos['potenciaFinal'] = parametros.potenciaFinal[1]
        parametros.todos['potenciaRT'] = parametros.potenciaInicial[1]
        parametros.todos['potenciaStep'] = parametros.potenciaStep[m1]
        parametros.todos['tempo'] = parametros.tempo[m1]
        parametros.todos['tempoStep'] = parametros.tempoStep[m1]

#------------------------------------------------------------------------------------------------
    