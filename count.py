import math

from math import ceil, degrees, fabs, fmod, frexp, fsum, hypot, sqrt

print('Hello')#string
print(78)#integer
print(12.4)#float
print(12*2)#daugyba
print(12**2)#kelti kvadratu
print(11//2)#floor division = 5, oposite to ceil
print(10%3)#liekana
print(10/2)#dalyba
print(10 + 10)#sudetis
print(10-3)#atimtis
print('Hello', 78)#string and int
print([13,56,67,'as'])#list
print({'gh': 1,'df': 3})#dict

name = 'Marius'
age = 32
print(f"Hello, my name is {name} and i'm {age} years old")
print("Hello, my name is " + name, "and i'm", + age, "years old")# space before last " adds space in print result

print(name[1])#prints 2nd char of string Marius

a = 13
print(int(a))
print(str(a))
print(float(a))
print(abs(a)) # is -17 i 17 
print(degrees(a)) # radians to degrees 1radian = 57degrees
print(sqrt(a)) #kvadratine saknis
print(ceil(a)) #integer that is greater than a/ sveikas skaicius kuris yra lygus arba daugiau uz a
print(fabs(a)) # -17.1 i 17.1
print(round(a)) # suapvalina
print()

print(sorted(range(a))) #isrikiuoja didejimo tvarka ir konvertoja 5 lista
print(type(sorted(range(a)))) #pasako kokio tipo kintamasis
print(set(sorted(range(a)))) #konvertuoja i seta
print(tuple(sorted(range(a)))) #konvertuoja i tuple
print(list(sorted(range(a)))) #konvertuoja i lista
print(len(list(sorted(range(a)))))
print()


print(sum(sorted(range(a)))) #sudeda narius
print(sorted(range(a))[slice(1,13,1)]) # nuo 0 iki 16-ojo nario atspausdina kas antra nari 
print(sorted(range(a))[slice(1,6,2)])
print(list(reversed(sorted(range(a))[slice(1,13,1)]))) # atvirkstine tvarka/mazejimo
print(max(list(reversed(sorted(range(a))[slice(1,13,1)]))))# max
print()

#-----------------------------------------------.funkcijos----nepakeiciamas listas-------------------------------------------------------------------


print(list(reversed(sorted(range(a))[slice(1,13,1)])).index(5)) # grazina iteravimo numeri ties kuria vieta buvo 5 liste, pvz 3-ias skaicius yra 5 gr 3
print(list(reversed(sorted(range(a))[slice(1,13,1)])).count(5)) # suskaiciuja kiek 5 narys psikartoja
print()
#-----------------------------------------------funkcijos.funkcijos----pakeiciama liistas, o ne funkcija todel grazinama none------------------------

x = list(sorted(range(a))[slice(1,13,1)])
x_1 = list(sorted(range(a))[slice(1,13,1)])
x_2 = list(range(a))[slice(1,13,1)]
x_3 = list(sorted(range(a))[slice(1,13,1)])
x_4 = list(sorted(range(a))[slice(1,13,1)])
x_5 = list(sorted(range(a))[slice(1,13,1)])
x_6 = list(sorted(range(a))[slice(1,13,1)])
x_7 = list(sorted(range(a))[slice(1,13,1)])

func = x.append(56) # ikelia
func1 = x_1.extend("d") # only for string
func2 = x_2.sort() # isrikiuoja 
func3 = x_3.clear() # istrina viska is listo
func4 = x_4.copy() # padaro listo kopija
func5 = x_5.insert(4,[98,56,55]) # ikisa skaiciu: 1 skaicius = numeris nuo priekio, antras - skaicius arba list'as
func6 = x_6.pop(9) # nario skaicius nuo priekio kuris pasalinamas
func6 = x_7.remove(1) # pasalina nari

print(x)
print(x_1)
print(x_2)
print(x_3)
print(x_4)
print(x_5)
print(x_6)
print(x_7)
print()
#--------------------------------------------------------------------------------------------------------------------------------------------------------


g = list(sorted(range(a))[slice(1,13,1)])

print (g[0:1:1] + g[2:3:1] + g[4:5:1] + g[5:6:1] + g[7:8:1] + g[9:10:1] + g[11:12:1]) # atspausdina reikiama narius kaip muzikos teorijoj
print (g[0:6:2] + g[5:13:2]) # equivavelnt
print (g[5])
print()

#---------------------------------------------------------------------------------------------------------------------------------------------------------

tuple_1 = (11,56,24)
tuple_2 = (True,False,False)
tuple_3 = ("apple","bananna","carrot")
tuple_4 = ("abc", 34, True, 40, "male")
tuple_5 = ("mouse", [8,4,6], (1,2,3))

print(tuple_5[0:3]) #atspausdina nuo pirmo iki trecio
print(tuple_5[:2]) #atspausdina viska iki 2 nario
print(tuple_5[2:]) #atspausdina viska nuo antro iki galo 
print(tuple_5[0]) # atspausdina 1 nari
print(tuple_5[1][2]) #atspausdina 2 nari ir trecia nested nari
print(tuple_5[-1][2]) #atspasudina 2 nari nuo galo ir trecia nested nari nuo priekio

#nario, esancio tuple pakeitimas
c1 = list(tuple_1)
c1[1] = 76
tuple_1 = tuple(c1)
print(c1)

#nario ikelimas i tuple
c2 = list(tuple_2)
c2.append(45)
tuple_2 = tuple(c2)
print(c2)

#nario istrynimas is tuple
c3 = list(tuple_2)
c3.remove(45)
tuple_2 = tuple(c3)
print(c3)

#tuple sudetis
tuple_4 += tuple_3
print(tuple_4)

#unpacking
(green,yeallow,red) = tuple_5
print(green)
print(yeallow)
print(red)

#kiekvienam nariu pridedam 'fg'
for x in tuple_5:
	print(x,'fg') 

#
i = 0
while i < len(tuple_5):
	print (tuple_5[i])
	i = i + 1
#
def divide(k,l):
	ty = k*l
	return ty
print(divide(5, 7))
#
f = lambda ee,ii : ee*ii
print(f(5,6))

