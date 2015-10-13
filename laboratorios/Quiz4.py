>>>#Desarrolle una aplicacion que guarde, en un archivo de texto, las calificaciones
>>> #de los 5 quizzes realizados por 3 estudiantes. Cada estudiante tendrá su propio
>>> #archivo de texto, cuyo nombre de archivo será igual al nombre del estudiante.
>>> #Además debe mostrar en pantalla el valor promedio de las calificaciones
>>> #de cada estudiante. Utilice todos los conceptos aprendidos hasta el momento.
>>> 
>>> #Arquimedes Escartin 8-863-235 - Lloyd Perez 10-707-572
>>> #Archivo de texto de Estudiantes
>>> #Quiz #4
>>> 
>>> def	saveStudent(student)
	file = open(student, "w")
	file.write(student + ": \nPromedio: " + str(prom) +"\n")
	flie.close
>>> while student <= 3
	student = student+1
	name = input("Nombre: ")
	q1 = input(float("Ingrese nota de Quiz #1 "))
	q2 = input(float("Ingrese nota de Quiz #2 "))
	q3 = input(float("Ingrese nota de Quiz #3 "))
	q4 = input(float("Ingrese nota de Quiz #4 "))
	q5 = input(float("Ingrese nota de Quiz #5 "))
		prom = (q1+q2+q3+q4+q5)/5
def showMenu():
print('1. MEREB de Notas')
print('2. Salir')

if __name__ == '__main__':
	student_notes = {}
	sel_menu = 0
	while True:
		showMenu()
		try:
			sel_menu = int(input("Selecciona con numero (1-2): "))
		except:
			print("No es valida! Intente nuevamente.")
		else:
			if sel_menu == 1:
				saveStudent(student)
			elif sel_menu == 2:
				break
			else:
				print("Comando no valido. Intente de nuevo.")
				showMenu():
	

	print("Gracias. Vuelva pronto!")
