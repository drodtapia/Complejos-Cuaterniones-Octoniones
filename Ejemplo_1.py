#!/usr/bin/python3
from complejos import Complejos
a = input("Introducir real z1: ")
b = input("Introducir imaginario z1: ")
c = input("Introducir real z2: ")
d = input("Introducir imaginario z2: ")
f = input("Introducir real z3: ")
g = input("Introducir imaginario z3: ")
print()
z1 = Complejos(a,b)
z2 = Complejos(c,d)
z3 = Complejos(f,g)
s = z1+z2
s1 = s+z3
r = z1-z2
r1 = r-z3
m = z1*z2
m1 = m*z3
div = z1/z2
div1 = div/z3
print ("Primer complejo z1:",z1)
print ("Segundo complejo z2:",z2)
print ("Tercer complejo z3:",z3)
print ("Suma z1 + z2:",z1+z2)
print ("Suma z2 + z3:",z2+z3)
print ("Suma z1 + z3:",z1+z3)
print ("Suma de z1+z2+z3:",s1)
print ("Resta de z1 - z2:",z1-z2)
print ("Resta de z2 - z3:",z2-z3)
print ("Resta de z1 - z3:",z1-z3)
print ("Resta de z1-z2-z3:",r1)
print ("Multiplicacion de z1*z2",z1*z2)
print ("Multiplicacion de z2*z3",z2*z3)
print ("Multiplicacion de z1*z3",z1*z3)
print ("Multiplicacion de z1*z2*z3",m1)
print ("Division de z1/z2",z1/z2)
print ("Division de z2/z3",z2/z3)
print ("Division de z1/z3",z1/z3 )
print ("Division de (z1/z2)/z3",)
print ("conjugado z1:",z1.conjugado())
print ("conjugado z2:",z2.conjugado())
print ("conjugado z3:",z3.conjugado())
print ("Modulo de z1:",z1.__pow__())
print ("Modulo de z2:",z2.__pow__())
print ("Modulo de z3:",z3.__pow__())
print ()

