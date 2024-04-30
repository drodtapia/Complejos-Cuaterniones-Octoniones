#!/usr/bin/python3
#importamos la clase complejos.py para utilizarla nuevamente
from complejos import *
#se importa el modulo math para utilizar la raiz
import math
#Se crea la clase de cuaterniones con sus operaciones basicas.
class Cuaterniones:	
	#Constructor, que instancia los objetos
	def __init__(self, real, imaginario):
		self.real = real	
		self.imaginario = imaginario
	#Representacion en formato string del complejo.
	def __str__(self):
		#Se establece el formato de salida, siendo self.real el primer complejo y self.imaginario el segundo complejo.
			return "["+str(self.real)+","+str(self.imaginario)+"]"
	#Se utilizan metodos especiales para establecer las operaciones basicas de la clase
	#suma
	def __add__(self,C):
		return Cuaterniones(self.real+C.real,self.imaginario+C.imaginario)
	#resta
	def __sub__(self,C):
		return Cuaterniones(self.real-C.real,self.imaginario-C.imaginario)
	#multiplicacion
	def __mul__(self,C):
		return Cuaterniones(self.real*C.real-C.imaginario.conjugado()*self.imaginario,C.imaginario*self.real+self.imaginario*C.real.conjugado())
	#conjugado del cuaternion
	def conjugado(self):
		return Cuaterniones(self.real.conjugado(),Complejos(-1,0)*self.imaginario)
	#modulo del cuaternion
	def __pow__(self):
		return math.sqrt(self.real.__pow__()**2+self.imaginario.__pow__()**2)
	#division del cuaternion
	def __truediv__(self,C):
 		return (self*C.conjugado()*Cuaterniones(Complejos(C.__pow__()**(-2), 0), Complejos(0, 0)))