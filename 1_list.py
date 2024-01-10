#https://www.youtube.com/watch?v=HGOBQPFzWKo&ab_channel=freeCodeCamp.org


#1. LISTAS: orderred, mutable, allows duplicate elements

""""
mylist = [1,2,3,4,5,6,7,8,9]
print(mylist)

# opciones para copiar
mylist_copy = mylist[:]  #Para realizar una copia independiente se puede emplear el método =mylist.copy(), =list(mylist) y el tercer método es =mylist[:]
mylist_copy.append(20)
print(mylist_copy)

print(mylist)


#Funciones sobre una lista
b = [x*x for x in mylist]
print(b)
"""

#2. TUPLAS: ordered, inmutable(no se pueden cambiar luego de creadas), allows duplicate elements
"""
mytuple = ("Max", 28, "Boston")  #el uso del paréntesis es opcional. Si fuese una tupla de un sólo elemento, entonces se debe escribir ("Max",)
print(mytuple)

mytuple2 = tuple(["Max",28,"Boston"])  #la función tuple sólo permite un argumento
print(mytuple2)

item = mytuple2[-2]
print(item)

if "Max" in mytuple2:
    print("yes")
else:
    print("no")

mytuple3 = ('a','p','p','l','e')
print(mytuple3.index('l'))

#se puede convertir una lista en tupla y viceversa
mylist = list(mytuple3)
print(mylist)

mytuple4 = tuple(mylist)
print(mytuple4)

a = (1,2,3,4,5,6,7,8,9,10)
b = a[::-1]
print(b)

mytuple5 = "Max",28,"Boston"
name, age, city = mytuple5
print(name)
print(age)
print(city)

mytuple6 = (0,1,2,3,4,5,6)
i1,*i2,i3 = mytuple6
print(i1)
print(i2)
print(i3)
"""
"""
#Vamos a comparar cuál es más eficiente entre una lista y una tupla
import sys
my_list = [0,1,2,"Hello",True]
my_tuple = (0,1,2,"Hello",True)
print(sys.getsizeof(my_list),"bytes")  #104 bytes
print(sys.getsizeof(my_tuple),"bytes")  #80 bytes

import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]",number=1000000))   #0.0464694
print(timeit.timeit(stmt="(0,1,2,3,4,5)",number=1000000))   #0.0096414
"""

# 3. DICTIONARIES: Key-Values pairs, unordered, mutable
"""
mydict = {"name": "Max", "age": 28, "city": "Boston"}
print(mydict)

#mydict2 = dict(name="Valeria", age=25, city = "New York")
#print(mydict2)
"""
"""
#Como es mutable, puede adicionar o sobreescribir nuevos elementos
mydict["email"] = "abc@xyz"
print(mydict)

mydict["email"] = "pqrs@xyz"
print(mydict)

#Borrar elementos
del mydict["name"]
print(mydict)

mydict.pop("city")
print(mydict)

mydict.popitem()  #borra el último elemento insertado
print(mydict)
"""
"""
# Opciones para validar si una key se encuentra en el diccionario
if "name" in mydict:
    print(mydict["name"])

try:
    print(mydict["citi"])
except:
    print("Error")
"""
"""
#Opciones para buscar los elementos del diccionario
#for key in mydict:
#    print(key)

for key in mydict.keys():
    print(key)

for value in mydict.values():
    print(value)

for key, value in mydict.items():
    print(key,value)
"""
"""
# Copiar diccionarios
#mydict_copy = mydict #afecta también al original porque apuntan a la misma dirección de memoria
#mydict_copy = mydict.copy() #este sí genera una copia independiente del original
mydict_copy = dict(mydict) #También genera una copia independiente

mydict_copy["email"] = "abc@xyz.com" 
print(mydict_copy)
print(mydict)
"""
"""
#Realizar actualizaciones del diccionario
mydict2 = dict(name="Valeria", age=25, email = "abc@xyz.com")
print(mydict2)

mydict.update(mydict2)
print(mydict)
"""
"""
mydict1 = {1:1,2:4,3:9,4:16}
print(mydict1)

value = mydict1[3]
print(value)
"""
"""
#Inclusión de tuplas en el diccionario (no puede ser listas porque son mutables)
mytuple = (7,8)
mydict[mytuple] = 12
print(mydict)
"""

#4. SETS: unorder, mutable, no duplicates (no arroja error si se duplica, sólo que no los toma en cuenta)
#declaración:   
#myset = {1,1,2,3,5} #Pilas que si quieres declarar un set vacío no puedes hacerlo así {} porque lo tomará como un diccionario. #Toca que sea set()
#print(myset)

#myset = set("Hello")
#print(myset)  #No le interesa el orden
"""
myset = set()

myset.add(1)
myset.add(1)
myset.add(2)
myset.add(3)
myset.add(5)
"""

#myset.remove(1)  #remueve el valor indicado. Si no lo encuentra, muestra error
#myset.discard(9) #remueve el valor indicado. Si no lo encuentra, NO muestra error
#print(myset)

#borrar a todos los elementos del set
#myset.clear()
#print(myset)

#print(myset.pop(3)) #borra un elementoaleatorio del set
#print(myset)

#buscar elementos dentro del set
#for x in myset:
#    print(x)

#if 3 in myset:
#    print("yes")

""""
#Unión and intersection of sets
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7,11,13,17}         

u = odds.union(evens)
print(u)

i = evens.intersection(primes)
print(i)

#retirar los elementos comunes que están en "u"
diff = u.difference(primes)
print(diff)

#dejar solamente los elementos diferentes de ambos sets
diff_2 = u.symmetric_difference(primes)
print(diff_2)
"""
"""
#hasta ahora no estamos nodificando los sets originales. Para hacerlo tenemos estas ocpiones:
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

#setA.update(setB)  # se adicionan los elementos diferentes
#print(setA)

#setA.intersection_update(setB)
#print(setA)

#setA.difference_update(setB)
#print(setA)

#setA.symmetric_difference_update(setB)
#print(setA)
"""
"""
setA = {1,2,3,4,5,6}
setB = {1,2,3}

print(setA.issubset(setB)) #si está incluido
print(setA.issuperset(setB)) #si lo contiene
print(setA.isdisjoint(setB)) #si no tienen ningún elemento común da True
"""
"""
#Al igual que en los casos anteriores, tener en cuenta al copiar:

setA = {1,2,3,4,5,6}
#setB = setA  #el cambio en el setB afecta al setA
#setB = setA.copy()
setB = set(setA)

setB.add(7)
print(setB)
print(setA)

#Frozen sets: sets inmutables. NO se puede adicionar nio borrar
a = frozenset([1,2,3,4])

print(a)
"""
#5. STRINGS: ordered, inmutable, text representation
#myString = 'I\'m programmer' #se puede usar comillas simples o dobles; pero si requieres una comilla dentro del srting. usar \
#print(myString)

#myString = """Hello
#World"""
#print(myString)

#myString = """Hello \
#World"""
#print(myString)

#string is inmutable

myString = "Go fast!"
#char = myString[0]
#print(char)

#myString[0] = "g"  #arroja error porque strings son inmutables
#print(myString)

#substring = myString[::-1]
#print(substring)

"""
if 'ast' in myString:
    print('yes')
else:
    print('no')
"""

"""
myString2 = "    Hello Word!    "
myString2.strip()
print(myString2)    #Como string es inmutable, strip no la afecta a menos que sobreescribas

myString2 = myString2.strip()
print(myString2)
"""
#métodos de tratamiento
print(myString.upper())
print(myString.lower())

