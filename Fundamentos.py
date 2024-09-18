from Funciones import nuevo_tema,nuevo_subtema


print("Hola mundo")
print("saludos")

#print("======== creando función ========")





def factorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n - 1)
numero = 5
print("factorial de ", numero, "es ", factorial(numero))



nuevo_tema("variables")
numero=5
print('edad: ',numero)

altura=1.70
print('altura:',altura)

edad=27
print("edad: ",edad)

nombre="Jesús"
print("nombre ",nombre)

esTrabajador= True
print("trabajador: ",esTrabajador)







nuevo_tema("listas")

frutas = ['manzanas','peras','piñas','naranjas','guayabas','papayas']
print("frutas: ", frutas)

varias_cosas = ["escuela",23, True, frutas]#permite un arreglo dentro de otro arreglo
print("varias cosas: ",varias_cosas)
#seleccionando un elemento
"""
    seleccionando un elemento
    comentario de multiples lineas
"""

print("frutas[0]: ", frutas[0])
#si quieres el ultimo elemento del arreglo, puedes escribir -1
#print("frutas[-1]: ", frutas[-1]) imprimiría papayas
print("frutas[-1]: ", frutas[-1])
print("frutas[-2]: ", frutas[-2])


print("frutas[1:5]: ", frutas[1:5])#del 1 hasta antes del 5/número que se escribe
print("frutas[0:5]: ", frutas[0:5])#del 1 hasta antes del 5/número que se escribe
print("frutas[1:5:2]: ", frutas[1:5:2])#salteado de 2 en 2

#agregando un elemento al final
frutas.append("fresas")
print("frutas: ",frutas)

#eliminano un elemento
frutas.remove("naranjas")
print("frutas: ", frutas)

#agregando un elemento en un lugar en específico/ en un a posición(recorre los elementos, no lo elimina)
frutas.insert(4,"kiwi")
print("frutas: ", frutas)

#creando una lista vacía
calificaciones = []
libros = list()
print("calificaciones: ", calificaciones)
print("libros: ", libros)

frutas.reverse()#te lo despliega de atras para adelante
print("frutas: ", frutas)
frutas.sort()#ordena alfabeticamente
print("frutas: ", frutas)
#frutas2 = frutas.sort()
#print ("frutas: ", frutas2)



nuevo_tema("diccionarios")
persona = {"nombre": "Pedro", "apellido":"Pérez","edad":"48","estatura":170, "hijos": ["Casimira", "Bryan","Eliud"]}#las llaves indican que es un diccionario \\hijos va entre corchetes porque es una lista



print("persona", persona)
print("persona.keys(): ", persona.keys())
print("persona.values(): ", persona.values())

print('persona.get("nombre"): ', persona.get("nombre"))#dame la llave nombre
print('persona.get("estatura"): ', persona.get("estatura"))#dame la llave estatura

print("persona.items(): ", persona.items())#Dame\da los elementos

nuevo_tema("Ciclos")
nuevo_subtema("for")
for i in range(10):
    print (i)
print("#######")
for i in range(3,10):
    print (i)
print("#######")
for i in range(3,10,2):
    print (i)


len(frutas)
print("len(frutas): )",len(frutas))

for fruta in frutas: #De la lsiat de frutas dame un elemento uno por uno// te mueves por elemento
    print(fruta)## despues del for ese "fruta" es una variable el "frutas" es el arreglo

print("#####con len")
for indice in range(len(frutas)):
    print("Indice ", indice, frutas[indice])

print("#####con enumerate")
for indice, fruta in enumerate(frutas):#otro forma de obtener el indice/enumerar la lista
    print(indice, fruta)

print("#####for en un diccionario")
for key, value in persona.items():#Un for puede regresar dos cosas al mismo tiempo
    print(key, value)#un diccionario sólo tiene llave y valor