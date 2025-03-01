# coding=utf-8
import math
import numpy as np
import parametros

#flags que acusam problema nos parametros do circuito
parametros.flag['impedance'] = False
parametros.flag['temperature'] = False
parametros.flag['callErrorWindow'] = False

#metodo que calcula a impedancia estimada na carga
def getImpedance(measuredVoltage,measuredCurrent):
   if(measuredCurrent>0.0):
      impedance = measuredVoltage/measuredCurrent
   else:
      impedance = "INF"
      parametros.flag['impedance'] = True
   return impedance

#metodo que calcula a potencia estimada na carga
def getPower(measuredVoltage,measuredCurrent):
   power = measuredVoltage*measuredCurrent
   print "Potencia Calculada: " + str(power)
   return power

def mapo(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

#metodo que calcula a tensao a ser enviada no DAC para a potencia desejada
def voltageDACalc(powerValue,measuredVoltage,measuredCurrent):
   print "Potencia Desejada: " + str(powerValue)
   #valor de tensao estimada na carga
   print "Tensao Medida: " + str(measuredVoltage)
   #valor de corrente estimada na carga
   print "Corrente Medida: " + str(measuredCurrent)
   if (measuredCurrent < 0.2) or (measuredVoltage<0.2): #Se a corrente for desprezível
      impedance = 50 # impedancia base (chutando impedancia)
   else:
      #calculo de impedancia a partir dos valores de tensao e corrente estimados na carga
      impedance = measuredVoltage/measuredCurrent
   print "Impedancia calculada: " + str(impedance)
   #calcula a tensao ideal na carga para a potencia desejada a partir da impedancia calculada
   newVoltage = math.sqrt(abs(powerValue*impedance))
   #retorna tensao ideal no carga
   return newVoltage

#metodo para calcular o erro entre o valor de tensao medido e o valor de tensao desejado(ideal)
#retorna o valor a ser incrementado com o intuito de se alcançar o valor ideal
def errorCalc(measuredValue,idealValue):
   #convertendo valores na carga para range de entrada (0-5V)
   measuredValue = ((measuredValue-10.008)/0.0061)#getInterpRevVoltage(measuredValue,calculatedImpedance)
   idealValue = ((idealValue-10.008)/0.0061)

   dacResolution = 0.01960784314
   # dacResolution = 0.02450980392
   # dacResolution = 0.01568627451
   smallestError = 0.02

   #valor de tensao lido(medido)
   print "Valor Medido: "+str(measuredValue)
   #valor de tensao desejado(ideal)
   print "Valor Ideal: " + str(idealValue)

   #calculo do erro entre o valor ideal e o valor medido
   measuredError = idealValue - measuredValue
   print "Erro Medido: " + str(measuredError)
   absError = abs(measuredError)
   print "Erro Medido(Abs): " + str(absError)
   errorBits = int(absError)
   print "Erro Medido(Bits): " + str(errorBits)

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
   print "Error (bits) modificado: " + str(increment)
   #retorna o valor a ser incrementado ou decrementado no DAC (bits 0-255)
   #com o intuito de se aproximar ao valor ideal
   return increment 

#Metodo que monitora o valor de impedancia calculado
#com o intuito de detectar caso ocorra algum problema 
#como curto-cicuito ou circuito aberto
def controlImpedance(measuredImpedance):
   impMinValue = 0.5
   impMaxValue = 700
   if(measuredImpedance<impMinValue): #Impedancia muito baixa (Curto-circuito)
      parametros.flag['impedance'] = True
   elif(measuredImpedance>=impMaxValue): # Impedancia muito alta (Circuito aberto)
      parametros.flag['impedance'] = True
   else:
         parametros.flag['impedance'] = False
   return parametros.flag['impedance']

#Metodo que monitora o valor de temperatura na carga
#com o intuito de detectar temperatura muito alta (necrose)
def controlTemperature(measuredTemperature):
   tempMaxValue = parametros.todos['temperaturaMax']
   if(measuredTemperature>=tempMaxValue): # Temperatua muito alta
      parametros.flag['temperature'] = True
   else:
      parametros.flag['temperature'] = False
   return parametros.flag['temperature']
