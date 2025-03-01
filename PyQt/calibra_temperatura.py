# coding=utf-8

from __future__ import division
import smbus
import time
#import controller
import math
import os
from xlwt import Workbook

bus = smbus.SMBus(1)
address2 = 0x49

var0 = 2
temp = 0
wb1 = Workbook()
sheet1 = wb1.add_sheet('sheet1')
sheet1._cell_overwrite_ok = True

for index in range(2):
    sheet1.col(index).width = 7000
sheet1.write(0,0,"Tabela de Calibracao")
sheet1.write(1,0,"Temperatura")
sheet1.write(1,1,"Leitura ADC")

temp = input("Digite a Temperatura Inicial: ")

while True:

    ADCtemp = 0
	# Temperatura 
    try:
        input("Aperte Enter para escrever no arquivo...")
    except SyntaxError:
        pass

    try:
        for x in range(0,15):
            #Leitura de temperatura
            bus.write_byte(address2, 2)
            #bus.read_byte(address2)
            ADCtemp_Temp = bus.read_byte(address2)
            print ADCtemp_Temp
            ADCtemp += ADCtemp_Temp
        ADCtemp = ADCtemp/(x+1)
    except Exception, e:
        print "Erro na leitura"
                        
    print "Temperatura: " + str(temp) + "    Valor lido: " + str(ADCtemp)
    sheet1.write(var0,0,temp)
    sheet1.write(var0,1,ADCtemp)
    var0 += 1  
    temp += 1 
    wb1.save('calibracao_temperatura.xls')
	




