#valores iniciais (default) dos parametros do sistema



todos = {
'potenciaInicial': 10,
'potenciaRT': 10,
'potenciaStep':5, 
'potenciaFinal': 40,
'potenciaMax':50,
'potenciaMin':5,
'tempo':10,
'tempoStep':5,
'temperaturaMax':60,
'temperaturaLimSup':100,
'temperaturaLimInf':20,
'modo': 1};

flag = {
	'impedance':False,
	'temperature':False,
	'endOfOperation':False,
	'manualMode':False,
	'stepDown':False,
	'veraFlag':False,
	'callErrorWindow' : False}


#Valores de Acordo com Modo [Modo1, Modo2, Modo3]
potenciaInicial =[10,20,30]
potenciaFinal = [20,40,50]
potenciaStep = [5,5,5]
tempo = [10,8,4]
tempoStep = [5,2,1]
modo = [1,2,3]