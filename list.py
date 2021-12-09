


from collections import deque


list_a = ['ionian',15, 13.5,'phrygian','lydian',(14,5),'myxolydian',['aeolian','locrian'],'88','19.1',{'home':20}]
list_b = ['a',12,'[c]',13.9]



a_0 = list_a[1]###<-------------------------------------------------index[int]-------------------->integer
a_1 = list_a[2]###<-------------------------------------------------index[int]-------------------->float
a_2 = list_a[5]###<-------------------------------------------------index[int]-------------------->(tuple)
a_3 = list_a[2:5]#<-------------------------------------------------index[int]:index[int]--------->[list]
a_4 = list_a[-1]##<-------------------------------------------------index[int]-------------------->{dict}
a_5 = list_a[-4][1]#<-----------------------------------------------index[int]\index[int]--------->string


b_0 = list_a.index('ionian')#<--------------------------------------string------------------------>index[int]
b_1 = list_a.index(13.5)#-------------------------------------------float------------------------->index[int]
b_2 = list_a.index(['aeolian','locrian'])#--------------------------[list]------------------------>index[int]
b_3 = list_a.index({'home':20})#------------------------------------dictionary-------------------->index[int]
b_4 = list_a.index((14,5))#-----------------------------------------tuple------------------------->index[int]


c_0 = int(list_a[8])#-----------------------------------------------index[int]-------------------->string------------------------------>integer
c_1 = float(list_a[9])#---------------------------------------------index[int]-------------------->string------------------------------>float
c_2 = str(list_a[1])#-----------------------------------------------index[int]-------------------->integer----------------------------->string
c_3 = complex(list_a[1])#-------------------------------------------index[int]-------------------->integer----------------------------->complex
c_4 = ascii(list_a[1])#---------------------------------------------index[int]-------------------->integer----------------------------->string
c_5 = repr(list_a[0])#----------------------------------------------index[int]-------------------->integer----------------------------->string


g_0 = list(iter(list_a[0]))#----------------------------------------index[int]-------------------->string-----------'x'--xx--'x'------->[list]
g_1 = list(deque(str(list_a[1]),2))#--------------------------------(index[int]),:int------------->string-----------'x'--xx--'x'------->[list]
g_2 = list(zip(list_a[0:3],range(8),range(7),range(7)))#--------------index[int]-------------------->string----tuple('x')-xx-('x')------->[list]
g_3 = list(enumerate(list_a[0]))#-----------------------------------index[int]-------------------->string----tuple('x')-xx-('x')------->[list]


d_1 = list_b.insert(list_a.index('phrygian'),19)#pozicija,skaicius
d_2 = list_b.insert(list_a.index('phrygian'),list_a.index('phrygian'))#pozicija,skaicius
d_3 = list_b.insert(list_a.index('phrygian'),19)#pozicija,skaicius


print(a_0)
print(a_1)
print(a_2)
print(a_3)
print(a_4)
print(a_5)

print(b_0)
print(b_1)
print(b_2)
print(b_3)
print(b_4)

print(c_0)
print(c_1)
print(c_2)
print(c_3)
print(c_4)
print(c_5)


print(g_0)
print(g_1)
print(g_2)
print(g_3)

print(list_b)

