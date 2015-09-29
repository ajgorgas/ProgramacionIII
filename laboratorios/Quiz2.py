#Quiz #2
#Almacen "El Emperador"
#Programador y empleado del almacen El Emperador:
#Arquimedes Escartin
#
#>= $500, 30% Desc
# < $500 pero >= $200, 20% Desc
# < $200 >= $100, 10% Desc

user = 5
x = 1

while x <= user:
	compra = int(input("Introduzca cifra: "))

	if compra >= 500:
		desc = compra * 0.3
		montof = compra + desc
		print("Descuento de 30% para la compra. El total es " +str(montof)+ " dolares.")
	
	if compra < 500 && >= 200:
		desc = compra * 0.2
		montof = compra + desc
		print("Descuento de 20% para la compra. El total es " +str(montof)+ " dolares.")

	if compra < 200 && >= 100:
		desc = compra * 0.1
		montof = compra + desc
		print("Descuento de 10% para la compra. El total es " +str(montof)+ " dolares.")

	else:
		print("El total de la compra es " +str(compra)+ " dolares. ")
