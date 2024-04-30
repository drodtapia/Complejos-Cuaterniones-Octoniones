#!/usr/bin/python3
from cuaterniones import *
a = input("Introducir real z1: ")
b = input("Introducir imaginario z1: ")
c = input("Introducir real z2: ")
d = input("Introducir imaginario z2: ")
f = input("Introducir real z3: ")
g = input("Introducir imaginario z3: ")
print
z1 = Complejos(a,b)
z2 = Complejos(c,d)
z3 = Complejos(f,g)

C1 = Cuaterniones(z1, z2)
C2 = Cuaterniones(z2, z3)
C3 = Cuaterniones(z1, z3)
S = C1+C2
S1 = S+C3
R = C1-C2
R1 = R-C3
M = C1*C2
M1 = M*C3
DIV = C1/C2
DIV1 = DIV/C3
print ("Primer Cuaternion C1=(z1,z2):",C1)
print ("Segundo Cuaternion C2=(z2,z3):",C2)
print ("Tercer Cuaternion C3=(z1,z3):",C3)
print ("Suma de C1 + C2:",C1+C2)
print ("Suma de C2 + C3:",C2+C3)
print ("Suma de C1 + C3:",C1+C3)
print ("Suma de C1+C2+C3:",S1)
print ("Resta de C1 - C2:",C1-C2)
print ("Resta de C2 - C3:",C2-C3)
print ("Resta de C1 - C3:",C1-C3)
print ("Resta de C1-C2-C3:",R1)
print ("Aqui demostraremos que los cuaterniones no son conmutables")
print ("Multiplicacion de C1*C2",C1*C2)
print ("Multiplicacion de C2*C1",C2*C1)
print()
print ("Multiplicacion de C2*C3",C2*C3)
print ("Multiplicacion de C3*C2",C3*C2)
print()
print ("Multiplicacion de C1*C3",C1*C3)
print ("Multiplicacion de C3*C1",C3*C1)
print ("Como pudimos notar los resultados son distintos, con distintos componentes, por lo tanto no es conmutativa")
print ("Multiplicacion de C1*C2*C3",M1)
print ("conjugado C1:",C1.conjugado())
print ("conjugado C2:",C2.conjugado())
print ("conjugado C3:",C3.conjugado())
print ("Modulo de C1:",C1.__pow__())
print ("Modulo de C2:",C2.__pow__())
print ("Modulo de C3:",C3.__pow__())
print ("Division de C1/C2",C1/C2)
print ("Division de C2/C3",C2/C3)
print ("Division dee C1/C3",C1/C3)
print ("Division de (C1/C2)/C3",DIV1)


