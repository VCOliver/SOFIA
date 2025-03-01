import matplotlib.pyplot as plt
import parametros
import os,sys



# 1 W/ minuto
def plotMode(mode):
#DELETAR ARQUIVOS PRE-EXISTENTES
	os.listdir(os.getcwd())
	img = "mode" + str(mode) + ".png"
	# print img
	# sentence = [
	# "[ -f mode1.png ] && rm mode1.png",
	# "[ -f mode2.png ] && rm mode2.png",
	# "[ -f mode3.png ] && rm mode3.png"
	# ]

	sentence = "[ -f "+img+" ] && rm "+img
	# print sentence
	os.system(sentence)
	# print sentence
	# for k in range(len(sentence)):
	# 	os.system(sentence[k])


	time_step = parametros.tempoStep[mode-1]
	timeValue = 0 	#Tempo sempre inicia
	potStep = parametros.potenciaStep[mode-1]
	potValue = parametros.potenciaInicial[mode-1]
	y = [potValue]
	x=[timeValue]
	interval = parametros.tempo[mode-1]

	for n in range(interval/time_step):
	# for n in range(int(interval/time_step)):
	# for n in range(interval):
		potValue += potStep
		y.append(potValue)
		timeValue += time_step
		x.append(timeValue)

	# print x
	# print y

	if mode == 1:
		color = 'blue'
	elif mode == 2:
		color = 'green'
	else:
		color = 'red'

	fig = plt.figure(1)
	ax = fig.add_subplot(111)	
	ax.plot(x,y,color,drawstyle='steps-post')
	ax.patch.set_facecolor('gray')
	plt.xticks(x, range(interval+1))
	plt.ylabel('Potencia (W)',fontsize=16)
	plt.xlabel('Tempo (min)',fontsize=16)
	plt.grid(color='white')
	# plt.axis([0, (interval), 0, 50])
	fig.savefig(img, facecolor='gray', edgecolor='black')
	plt.close()
