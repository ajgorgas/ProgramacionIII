#Quiz #5
#Arquimedes Escartín

import os
import Hola as n

mensaje = ""

def mostrarMenu():
	print('\n1. Ingresar mensaje')
	print('2. Comparar')
	print('3. Guardar')
	print('4. Contador')
	print('5. Salir')
	print()
		

if __name__ == '__main__': 
	a = n.Hola()
	e = n.Hola()
	opcion_menu = 0
	while True:
		mostrarMenu()
		try:
			opcion_menu = int(input("\nIntroduzca una opcion (1-5): "))
		except:
			print("Opcion no valida")
		else:
			if opcion_menu == 1:
				os.system('cls')
				print("Opcion 1: Ingresar mensaje.")
				mensaje = input("\n\nIngrese Mensaje: ")
				a.contar()
			elif opcion_menu == 2:
				os.system('cls')
				if mensaje == "":
					print("No, no, no! Escriba un mensaje primero. >.>")
				else:	
					print("Opcion 2: Comparar mensajes\n")
					e.comparar_mensaje(mensaje)
			elif opcion_menu == 3:
				os.system('cls')
				if mensaje == "":
					print("No, no, no! Escriba un mensaje primero. >.>")
				else:
					print("Opcion 3: Guardar mensaje")
					e.guardar_mensaje(mensaje)
					print("...Guardado.")
			elif opcion_menu == 4:
				os.system('cls')
				print("Opcion 4: Mostrar Contador")
				a.mostrar_contador()
			elif opcion_menu == 5:
				break
			else:
				os.system('cls')
				print("Error_ No es aceptable este comando.")
				mostrarMenu()

print("Muchas gracias por el uso del programa.")
