from array import array
import numpy as np
import random

#1- Escribir una función que reciba un número​n y devuelva ​true si​ es primo o ​false en caso ​contrario​.  
# def esPrimo(n):
#     contador=0
#     for i in range(2, n):
# 	    if(n % i == 0):
#                 contador+=1
#     if(contador > 1):
#         return False
#     else:
#         return True
			
# print(esPrimo(65))

# n = int(input("Ingrese un numero: "))
# for i in range(1, n):
#     print(n)

########################################################################################################

# 2- Escribir una función que calcule la suma de los múltiplos de 3 y 5, mayores o                                 iguales que 0 y menores que un parámetro ​n​.

# def suma(n):
#     suma=0    
#     for i in range(1, n):
#         if(i%3==0):
#             print("Multiplo 3:",i)
#             suma=suma+i
#         if(i%5==0):
#             print("Multiplo 5:",i)
#             suma=suma+i
#     return suma        

# print(suma(10))

########################################################################################################

#3- Escribir una función que reciba un arreglo de enteros y devuelva​ true si el arreglo está ordenado de mayor a menor y ​false​  si está desordenado.  

# def array_ordenado(array):

#         new_array=array.copy()
#         new_array.sort()
#         print(new_array)
#         if(array==new_array):
#             return True
#         else:
#             return False


# array=[1,2,3]

# print(array)
# print(array_ordenado(array))

########################################################################################################

#4- Escribir una función que reciba un arreglo de enteros y devuelva la suma de los elementos que se encuentran en posiciones pares (incluido el elemento de la posición 0)

# def sumaElementos(array):
#     evenIndex=[]
#     for i in range(0, len(array),2):
#         evenIndex.append(array[i])
#     return sum(evenIndex)

# listaA = [1, 2, 13 ,4, 8, 6]
# # suma=[listaA[i] for i in range(0, len(listaA),2)]

# # print(sum(suma))
# print(sumaElementos(listaA))

########################################################################################################

#5-Escribir una función que reciba dos matrices de ​NxN y devuelva la suma de las mismas. Podemos considerar que las matrices se representan como un arreglo bidimensional. 


# matriz1=[[1,2,3],[4,5,6],[7,8,9]]
# matriz2=[[1,2,3],[4,5,6],[7,8,9]]

# def sumaMatrices(matriz1, matriz2):
#     suma=[]
#     for i in range(len(matriz1)):
#         suma.append([])
#         for j in range(len(matriz1[i])):
#             suma[i].append(matriz1[i][j]+matriz2[i][j])
#     return suma

#print(sumaMatrices(matriz1,matriz2))


#Mismo Ejercicio pero usando la libreria numpy

# def sumaMatricesNumpy(matriz1, matriz2):
#     suma=np.add(matriz1, matriz2)
#     return suma

# print(sumaMatricesNumpy(matriz1, matriz2))

########################################################################################################

#6 Escribir una función que reciba dos arreglos ​a1 y ​a2​, de enteros ordenados de mayor a menor e intercale los elementos de los arreglos que recibe en un nuevo arreglo, tal que el arreglo resultante también esté ordenado

# def ordenarArrays(a1,a2):
#     new_array=[]
#     for i in range(0, len(a1)):
#         new_array.append(a1[i])
#     for i in range(0, len(a2)):
#         new_array.append(a2[i])
#     new_array.sort()
#     return new_array


# array1=[-5, 0, 0, 1, 5]
# array2=[-10, 0, 7]
# print(ordenarArrays(array1, array2))


########################################################################################################

#7 Escribir un programa que genere un número entero aleatorio entre ​0 y​ 1000 y le pida al usuario que lo adivine, si el usuario acierta debe responder con la cantidad de intentos y si el usuario no quiere continuar adivinando debe ingresar ​'*' y entonces debe mostrar cuál era el número.  

# def adivinaNumero(n):
#     bucle=0
#     corte='*'
#     contador=0
#     nrandom=(random.randint(0,1000))
#     while nrandom!=bucle:
#         print(nrandom)
#         print("Numero incorrecto, si desea terminar oprima la tecla *")
#         bucle=input("Ingrese numero: ")
#         if(bucle==corte):
#             contador=contador+1
#             print("El numero era",nrandom)
#             break
#         bucle=int(bucle)
#     contador=contador+1
#     print("El numero de intentos fue", contador)


# numero=int(input("Ingrese Numero: "))
# adivinaNumero(numero)

########################################################################################################

#8-Escribir un método que reciba como parámetro una matriz cuadrada de números reales y devuelva true (o false), si todos los elementos fuera de la diagonal principal están por encima de la media de los elementos de la diagonal principal. 

# matriz=[[1,2,3],[4,5,6],[10,8,9]]

# def media(matriz):
#     cantidad = sumaDiagonalPrincipal = promedioDiagonalPrincipal = sumaDiagonalPrincipal = sumaFueraDiagonal = promedioFueraDiagonal = 0

#     for i in range(len(matriz)):
#         sumaDiagonalPrincipal=sumaDiagonalPrincipal+matriz[i][i]
#         cantidad=cantidad+1
#     promedioDiagonalPrincipal=sumaDiagonalPrincipal/cantidad
#     cantidad=0

#     for i in range(len(matriz)):
#         for j in range(len(matriz)):
#             if(i!=j):
#                 sumaFueraDiagonal=sumaFueraDiagonal+matriz[i][j]
#                 cantidad=cantidad+1
#                 promedioFueraDiagonal=sumaFueraDiagonal/cantidad

#     if(promedioDiagonalPrincipal<promedioFueraDiagonal):
#         return True
#     else:
#         return False

# # print("SumaDiagonalPrincipal:",sumaDiagonalPrincipal)
# # print("PromedioDiagonalPrincipal:",promedioDiagonalPrincipal)
# # print("SumaFueraDiagonal:",sumaFueraDiagonal)
# # print("CantidadFueraDiagonal:",cantidad)
# # print("PromedioFueraDiagonal:",promedioFueraDiagonal)

# print(media(matriz))

########################################################################################################

#9-Una señal de audio digitalizada puede representarse como un arreglo de enteros,que oscilan entre ‘0’ (silencio) y ‘65536’ (tono agudo).Se desea construir un software que dada la señal, aplique un filtro pasa-banda definido por dos tonos(inferior y superior),que deja en silencio todo valor fuera de ese rango. El resultado debe compactarse, eliminando los silencios generados por este filtro. 
#Nota 1: Es estrictamente necesario aplicar el filtro primero, y luego compactar la SeñalOriginal. 
#Nota 2: No debe perderse la Señal original.

# def filtroPasaBanda(SeñalOriginal, inferior, superior):
#     nuevaSeñal=[]
#     señalFiltrada=[]
#     print("Señal Original:",SeñalOriginal)
#     for i in range(len(señalOriginal)):
#         if(señalOriginal[i]>inferior and señalOriginal[i]<superior):
#             nuevaSeñal.append(señalOriginal[i])
#         else:
#             señalFiltrada.append(señalOriginal[i])
#             señalOriginal[i]=0
            
            
#     print("Señal Filtrada:",señalFiltrada)
#     print("Señal Original con filtro:", señalOriginal)
#     return nuevaSeñal

# señalOriginal=[]
# for i in range(0, 10):
#     señalOriginal.append(random.randint(-65536,70000))

# inferior=0
# superior=65536


# print("Señal compactada:",filtroPasaBanda(señalOriginal, inferior, superior))

########################################################################################################

#10-Escribir una función ​consonantes que recibe una cadena de caracteres y devuelve la cadena que resulta de eliminar todas las vocales de la cadena recibida. Por ejemplo:consonantes("hola como estas"); // devuelve "hl cm sts"  

# cadena = "HOLA MUNDO"

# def consonantes(cadena):
#     cadena=cadena.lower()
#     for consonante in cadena:
#         if(consonante=="a" or consonante=="e" or consonante=="i" or consonante=="o" or consonante=="u"):
#             cadena=cadena.replace(consonante,"")
#     return cadena

# print(consonantes(cadena))

########################################################################################################

#11-Escribir una función que reciba una cadena de caracteres muestre por pantalla la frecuencia de aparición de cada letra. Por ejemplo: frecuencias("hola como estas..."); // debe mostrar por               pantalla:    >  a: 2  c: 1  e: 1  h: 1  l: 1  m: 1  o: 3  s: 2  t: 1  

# cadena = "HOLA MUNDO"

# def frecuencia(cadena):
#     letras=[]
#     cadena=cadena.lower()
#     cadena=cadena.replace(" ","")
#     cadena=list(cadena)
#     for letra in cadena:
#         print(letra)
    
# frecuencia(cadena)

########################################################################################################

#12-Implementar la clase Hotel tal que tenga operaciones para:   
# a. Crearla con la cantidad de habitaciones que tiene.  
# b. Ocupar una habitación disponible indicando la cantidad de personas mayores y menores (máximo 8 en total) que la ocuparán. void ocuparHabitacionCon(int mayores, int menores)  
# c. Devolver la cantidad total de personas que ocupan todas las habitaciones del hotel.  
# d. Devolver la cantidad de habitaciones que están ocupadas por tantos mayores como los indicados por parámetro.  int contarHabitacionesCon(int mayores)  
# e. Devolver un arreglo de enteros de longitud 9, tal que en la posición i del arreglo se guarde la cantidad de habitaciones con i personas.  

# habitaciones={[],[],[],[],[],[],[],[],[],[]}

# Hotel=Hotel(habitaciones)
# print(Hotel.habitaciones)


# class Hotel:

#     def __init__(self, cantidadHabitaciones):
#         self.cantidadHabitaciones = cantidadHabitaciones
#         self.habitaciones = []
#         for i in range(cantidadHabitaciones):
#             self.habitaciones.append(Habitacion(i))
    
#     def ocuparHabitacionCon(self, mayores, menores):
#         for habitacion in self.habitaciones:
#             if(habitacion.ocupada==False):
#                 habitacion.ocupar(mayores, menores)
#                 break
        
#     def contarHabitacionesCon(self, mayores):
#         contador=0
#         for habitacion in self.habitaciones:
#             if(habitacion.cantidadMayores==mayores):
#                 contador=contador+1
#         return contador
    
#     def contarPersonas(self):
#         contador=0
#         for habitacion in self.habitaciones:
#             contador=contador+habitacion.cantidadPersonas
#         return contador
    
#     def contarHabitaciones(self):
#         contador=0
#         for habitacion in self.habitaciones:
#             if(habitacion.ocupada==True):
#                 contador=contador+1
#         return contador
    
#     def contarHabitacionesDisponibles(self):
#         contador=0
#         for habitacion in self.habitaciones:
#             if(habitacion.ocupada==False):
#                 contador=contador+1
#         return contador
    
#     def contarHabitacionesOcupadas(self):
#         contador=0
#         for habitacion in self.habitaciones:
#             if(habitacion.ocupada==True):
#                 contador=contador+1
#         return contador
    
#     def contarHabitacionesDisponiblesCon(self, mayores):
#         contador=0
#         for habitacion in self.habitaciones:
#             if(habitacion.ocupada==False and habitacion.cantidadMayores==mayores):
#                 contador=contador+1
#         return contador
    
#     def contarHabitacionesOcupadasCon(self, mayores):
#         contador=0
#         for habitacion in self.habitaciones:
#             if(habitacion.ocupada==True and habitacion.cantidadMayores==mayores):
#                 contador=contador+1
#         return contador
