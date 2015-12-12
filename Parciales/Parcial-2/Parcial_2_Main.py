#!/usr/bin/python
# -*- coding: utf-8 -*-

from kivy.app import App
from  kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from precios import Precio
class Ventana(Screen):
	precio = ObjectProperty
	origen=""
	destino=""
	def Origen(self, origen):
			self.origen = origen
			print (origen)
	def Destino(self, destino):
			self.destino = destino
			print (destino)	
	def CalcularPrecio(self):
			if self.origen != "" and self.destino != "":
                                costo = ""+Precio(self.origen,self.destino)
                                if costo == "null":
                                        self.precio.text ="Precio Aun No Disponible."
                                else:
                                        self.precio.text = "El Precio Aproximadamente Es $ "+costo	
													
			else:
				self.precio.text = "No A Seleccionado Nada."

class AplicacionApp(App): 
	def build(self):  
		return Ventana()
	def on_pause(self):
		return True



if __name__ == '__main__':
	AplicacionApp().run()
