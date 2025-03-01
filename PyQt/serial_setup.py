#!/usr/bin/env python
          
import time
import serial
from serial import SerialException
import parametros


class Vera_Communication(object):
  
  #Estabelece comunicacao com o Vera
  def serial_setup(self):
    self.conected_flag = False
    import glob
    #locations = glob.glob('/dev/tty*') + glob.glob('/dev/ttyAMA*') + glob.glob('/dev/ttyUSB*')
    locations = glob.glob('/dev/ttyAMA0')
    
    for device in locations:
        try:
            print 'Tentando conexao com Vera...'
            print device
            self.ser = serial.Serial(
            port= device,
            baudrate = 9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=0.5)
            break
        except Exception as e:
            print "ERRO NA CONEXAO SERIAL I/O ERRO({0}): {1}".format(e.errno, e.strerror)
            #return self.conected_flag

    #self.conected_flag = True(
        #return self.conected_flag
    
  def connect(self):#Pete

    #time.sleep(2)

    self.ser.write('start')

    self.conected_flag = False
    # Read serial port with timeout
    timeout = time.time() + 5   # 5 s from now
    while time.time() < timeout:
        receive = self.ser.readline()
        if "start" in receive:
            print "receive:" + str(receive)
            self.conected_flag = True
            break
    print "FLag: " + str(self.conected_flag)
    return self.conected_flag

  #Funcao para escrita das variaveis de controle na serial
  def write_data(self,Volt_value,Curr_value,Temp_value):    

    if (self.conected_flag):
        self.ser.write('Tensao: %f \n Corrente: %f \n Temperatura: %f \n'%(Volt_value,Curr_value,Temp_value))  
        print 'Conexao estabelecida.'
    else:
        print 'Atencao sua conexao nao foi estabelecida, por favor, reinicie o equipamento ou procure a assistencia tecnica'

  def serial_close(self):
    if(parametros.flag['veraFlag']):
        self.ser.close()
    

################Utilizado para teste individual da funcao##############################

if __name__ == "__main__":
        ui = Vera_Communication()
        ui.serial_setup()
        ui.connect()
        ui.write_data(5,4,2)
# # # # #     # SecDialog.show()
        #sys.exit(app.exec_())