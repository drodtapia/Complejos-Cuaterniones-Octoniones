#!/usr/bin/python3
#importamos la clase cuaterniones.py para utilizarla nuevamente
from cuaterniones import *
#se importa el modulo math para utilizar la raiz
import math
#Se crea la clase de Octoniones con sus operaciones basicas.
class Octoniones:	
	#Constructor, que instancia los objetos
	def __init__(self, real, imaginario):
		self.real = real	
		self.imaginario = imaginario
	#Representacion en formato string del complejo.
	def __str__(self):
		#Se establece el formato de salida, siendo self.real el primer cuaternion y self.imaginario el segundo cuaternion.
			return "{"+str(self.real)+","+str(self.imaginario)+"}"
	#Se utilizan metodos especiales para establecer las operaciones basicas de la clase
	#suma
	def __add__(self,O):
		return Octoniones(self.real+O.real,self.imaginario+O.imaginario)
	#resta
	def __sub__(self,O):
		return Cuaterniones(self.real-O.real,self.imaginario-O.imaginario)
	#multiplicacion
	def __mul__(self,O):
		return Octoniones(self.real*O.real-O.imaginario.conjugado()*self.imaginario,O.imaginario*self.real+self.imaginario*O.real.conjugado())
	#Modulo del octanion
	def __pow__(self):
		return math.sqrt(self.real.__pow__()**2+self.imaginario.__pow__()**2)
