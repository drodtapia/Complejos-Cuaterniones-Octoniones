#!/usr/bin/python3
import sys
sys.stdout.reconfigure(encoding='utf-8')
#se importa el modulo math para ocupar la raiz cuadrada en el modulo.
import math
#Se crea la clase de complejos
class Complejos:
	#Constructor, que instancia los objetos.	
	def __init__(self, real, imaginario):
		self.real = int(real)	
		self.imaginario = int(imaginario)
	#Representacion en formato string del complejo.
	def __str__(self):
		#Se establece el formato de salida, sumando o restando la parte real e imaginaria en cada caso.
		if (self.imaginario < 0):
			return "("+str(self.real)+""+str(self.imaginario)+"i"+")"
		else:
			return "("+str(self.real)+"+"+str(self.imaginario)+"i"+")"
	#
	#suma
	def __add__(self,z):
		return Complejos(self.real+z.real,self.imaginario+z.imaginario)
	#resta
	def __sub__(self,z):
		return Complejos(self.real-z.real,self.imaginario-z.imaginario)
	#multiplicaion
	def __mul__(self,z):
		return Complejos(self.real*z.real-self.imaginario*z.imaginario,self.real*z.imaginario+self.imaginario*z.real)
	#division
	def __truediv__(self,z):
		return Complejos((z.__pow__()**(-2)), 0)*self*z.conjugado()
	#conjugado del numero complejo
	def conjugado(self):
		return Complejos(self.real,-self.imaginario)
	#modulo complejo
	def __pow__(self):
		return math.sqrt(self.real**2+self.imaginario**2)


