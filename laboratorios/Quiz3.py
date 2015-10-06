#Quiz #3
#Dado un intervalo de tiempo en segundos, calcular los segundos restantes que
#corresponden para convertirse exactamente en minutos. 
#Este programa debe funcionar para 5 oportunidades

for oport in range (1, 6):
	num = input ("\nIntroduzca un numero:")
	mins = int (num)/60
	if mins != 0:
		sec = 60 - int (num) %60
		print ("Los segundos que te faltan son " + str(sec)+ " segundos. ")
