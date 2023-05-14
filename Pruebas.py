import os 
import sys
import random as rd
sys.setrecursionlimit(9999999)             # Para resolver problemas de recursividad

nombre_archivo = "cards.txt"
os.chdir("C:\\Users\\Luis\\Desktop\\Ing. Computacion\\1 semestre\\Proga\\")

def retornar_contenido_archivo(nombre_archivo):
    "Retorna el contenido adentro de los archivos"
    manejador_archivo = open(nombre_archivo, encoding="iso-8859-1")
    contenidos = manejador_archivo.read()
    return contenidos
Cartas= retornar_contenido_archivo(nombre_archivo)

def buscar_en_archivos(texto, palabra):                           # Esta funcion lo que hace es buscar que una palabra se encuentre dentro de un texto
    """compara la palabra en un texto"""                          # se piensa utilizar para poder darle una descripcion a las cartas segun sus acciones
    if type(texto) != str:
        return False
    elif type(palabra) != str:
        return False
    else:
        return buscar_en_archivos_aux(texto, palabra)

def buscar_en_archivos_aux(texto, palabra):
    """funcion aux"""
    if len(texto) < len(palabra):
        return False
    elif texto[:len(palabra)] == palabra:
        return True
    else:
        return buscar_en_archivos_aux(texto[1:], palabra)
    
def Sacar_Cartas(Texto, inicio,final):
    """Corta cada 2 /n para separar cartas"""
    if type (Texto) != str:
        return "error 1"
    if type (inicio) != str:
        return "error 1"
    if type (final) != str:
        return "error 1"
    else:
        return Sacar_Cartas_Aux(Texto, inicio, final,"" ,0 )

def Sacar_Cartas_Aux(texto, inicio, final, res, Indice):      # Esta funcion lo que hace es separar todas la cartas del archivo de texto, lo realiza cada que encuentra 
    """Funcion aux"""                                         # 2 /n segidos y los mete dentro de una lista

    if Indice >= len(texto):
        return []
    if texto[Indice:Indice+len(final)] == final:
        return [res] + Sacar_Cartas_Aux(texto[Indice+len(final):], inicio, final, "", 0)
    else:
        return Sacar_Cartas_Aux(texto, inicio, final, res+texto[Indice], Indice+1)

def organizador(lista):                                     # Esta funcion es meramente estetica, ordena la lista de las cartas para que se 
    """ordena la lista"""                                   # mas legible a simple vista

    if type(lista)!=list:
        return "error-01"
    else:
        return organizador_aux(0,lista)

def organizador_aux(num,lista):
    """aux"""

    if lista==[]:
        return ""
    print (f"{num}-{lista[0]}") 
    print ("") 
    return organizador_aux(num+1,lista[1:])

def pasar_al_establo(unicornio,Establo):
    """Funcion para pasar al establo el unicornio que el jugador eliga de su mazo"""
    if type(unicornio)!=str:
        return "error-01"
    if unicornio!="Unicornio Bebe" and unicornio!="Unicornio Basico" and unicornio!="Unicornio Magico":
        return "error-02"
    if type(Establo)!=list:
        return "error-03"
    else:
        return pasar_al_establo_Aux(unicornio,Establo,[])

def pasar_al_establo_Aux(unicornio,Establo,nuevo_Establo):
    """Pasa al establo la carta que el jugador seleccione siempre y cuando sea un unicornio de cualquier tipo"""

    nuevo_Establo= Establo + [unicornio]
    return nuevo_Establo                #nuevo establo pasa a ser el mazo del jugador con el unicornio agreagado
    
def desventaja(desventaja,mazo):
    """"Funcion inutil que rebaja una carta de su propio mazo"""

    largo=len(mazo)-1    #cantidad de cartas en el mazo 
    carta_eliminada= rd.randint(0,largo)  #carta random del mazo
    if desventaja!="Desventaja":
        return "error-01"
    elif type(mazo)!=list:
        return "error-02"
    elif mazo==[]:
        return []
    else:
        return desventaja_aux(desventaja,mazo,largo,[],rd.randint(0,largo),0)

def desventaja_aux(desventaja,mazo,largo,nuevo_mazo,carta_a_eliminar,indice):  #escoge una carta random del mazo para eliminar, tras de que es
    """"funncion aux para eliminar la carta del mazo"""           #una carta poco util la hacemos peor al no poder eligir que carta 
    print(mazo,nuevo_mazo,carta_a_eliminar)
    if indice > largo:
        return nuevo_mazo    #nuevo mazo con la carta ya eliminada
    elif indice!=carta_a_eliminar:
        return desventaja_aux(desventaja,mazo,largo,nuevo_mazo+[mazo[indice]],carta_a_eliminar,indice+1)
    else:
        return desventaja_aux(desventaja,mazo,largo,nuevo_mazo,carta_a_eliminar,indice+1)
    
def magia(mazo):                                       #resive una carta random del mazo
    """funcion que toma una carta extra del mazo"""    #carta extra con una carta de magia
                                                    
    if type(mazo)!=list:
        return "error-01"
    else:
        mazo= mazo + [Lista_de_Cartas[rd.randint(0,107)]]
        return mazo
    
def ventaja(ventaja,establo):
    """mata a un unicornio del establo enemigo siempre y cuando haya un unicornio"""
    largo=len(establo)-1    #cantidad de unicornios en el establo
    if ventaja!="Ventaja":
        return "error-01"
    elif type(establo)!=list:
        return "error-02"
    elif largo==-1:
        return "error-03" #caso de que el establo enemigo este vacio, abra que arreglar a futuro para que o tire lista vacia o que devuleva
    else:
        return ventaja_aux(ventaja,establo,largo,[],rd.randint(0,largo),0)

def ventaja_aux(desventaja,establo,largo,nuevo_establo,unicornio_a_eliminar,indice): 
    """"funncion aux para eliminar la carta del mazo"""            
    print(establo,nuevo_establo,unicornio_a_eliminar)
    if indice > largo:
        return nuevo_establo    #nuevo establo con el unicornio ya eliminado
    elif indice!=unicornio_a_eliminar:
        return ventaja_aux(desventaja,establo,largo,nuevo_establo + [establo[indice]],unicornio_a_eliminar,indice+1)
    else:
        return ventaja_aux(desventaja,establo,largo,nuevo_establo,unicornio_a_eliminar,indice+1)

def descripcion(lista_de_cartas):
    """les da un el nombre de las cartas segun sus acciones y les da el numero de carta que es segun el mazo"""
    if type(lista_de_cartas)!=list:
        return "error-01111"
    else:
        return descripcion_aux(lista_de_cartas,[],0,0,len(lista_de_cartas)-1)

def descripcion_aux(lista_de_cartas,nueva_lista,indice,num_de_carta,largo):
    """funcion aux"""
    if indice > largo:
        return nueva_lista
    elif buscar_en_archivos(lista_de_cartas[indice], "Sacrificar")==True:
        return descripcion_aux(lista_de_cartas,nueva_lista +[f"Desventaja {num_de_carta}"],indice+1,num_de_carta+1,largo)
    elif buscar_en_archivos(lista_de_cartas[indice], "Descartar")==True:
        return descripcion_aux(lista_de_cartas,nueva_lista +[f"Ventaja {num_de_carta}"],indice+1,num_de_carta+1,largo)
    elif buscar_en_archivos(lista_de_cartas[indice], "Magic\n")==True:
        return descripcion_aux(lista_de_cartas,nueva_lista +[f"Magia {num_de_carta}"],indice+1,num_de_carta+1,largo)
    elif buscar_en_archivos(lista_de_cartas[indice], "Baby Unicorn")==True:
        return descripcion_aux(lista_de_cartas,nueva_lista +[f"Unicornio Bebe {num_de_carta}"],indice+1,num_de_carta+1,largo)
    elif buscar_en_archivos(lista_de_cartas[indice], "Basic Unicorn")==True:
        return descripcion_aux(lista_de_cartas,nueva_lista +[f"Unicornio Basico {num_de_carta}"],indice+1,num_de_carta+1,largo)
    elif buscar_en_archivos(lista_de_cartas[indice], "Magical Unicorn")==True:
        return descripcion_aux(lista_de_cartas,nueva_lista +[f"Unicornio Magico {num_de_carta}"],indice+1,num_de_carta+1,largo)
    else:
        return "error-01"

Lista_de_Cartas=Sacar_Cartas(Cartas,"Nombre","\n\n")   # Variable creada con el fin de usarla en la funcion random
Cartas_abreviadas=descripcion(Sacar_Cartas(Cartas,"Nombre","\n\n"))
def contenido_de_carta(mazo):
    """Devuelve el contenido general de una carta, el nombre, tipo, y descripcion"""
    print (mazo)
    largo=len(mazo)-1
    Carta_a_leer = input("Elige el número de la posición de la carta: ")
    if Carta_a_leer!="0" and Carta_a_leer!="1" and Carta_a_leer!="2" and Carta_a_leer!="3" and Carta_a_leer!="4" and Carta_a_leer!="5":
        return contenido_de_carta(mazo)
    elif Carta_a_leer=="1" and largo < 1:
        print ("No tienes tantas cartas")
        return contenido_de_carta(mazo)
    elif Carta_a_leer=="2" and largo < 2:
        print ("No tienes tantas cartas")
        return contenido_de_carta(mazo)
    elif Carta_a_leer=="3" and largo < 3:
        print ("No tienes tantas cartas")
        return contenido_de_carta(mazo)
    elif Carta_a_leer=="4" and largo < 4:
        print ("No tienes tantas cartas")
        return contenido_de_carta(mazo)
    elif Carta_a_leer=="5" and largo < 5:
        print ("No tienes tantas cartas")
        return contenido_de_carta(mazo)
    elif int(Carta_a_leer) < 0:
        print ("No puedes no tener cartas")
        return contenido_de_carta(mazo)
    else:
        return contenido_de_carta_aux(mazo,0,Cartas_abreviadas,0,int(Carta_a_leer))

def contenido_de_carta_aux(mazo,indice,cartas_abreviadas,posicion,carta_a_leer):
    """Funcion aux"""
    if mazo[carta_a_leer]!=Cartas_abreviadas[indice]:
        return contenido_de_carta_aux(mazo,indice+1,cartas_abreviadas,posicion,carta_a_leer)
    else:
        print (Lista_de_Cartas[indice])
        return ""


Lista_de_Cartas=Sacar_Cartas(Cartas,"Nombre","\n\n")   # Variable creada con el fin de usarla en la funcion random
#eliminar esta variable ya no es util 
"Mazo de cartas de los jugadores"                                   
Cartas_Jugador1=["","",""]
Cartas_Jugador2=["","",""]

Cartas_Jugador1[0]=Cartas_abreviadas[rd.randint(0,107)]    # Escoge aleratoriamente una carta del mazo y se la asigna al jugador
Cartas_Jugador1[1]=Cartas_abreviadas[rd.randint(0,107)]
Cartas_Jugador1[2]=Cartas_abreviadas[rd.randint(0,107)]

Cartas_Jugador2[0]=Cartas_abreviadas[rd.randint(0,107)]
Cartas_Jugador2[1]=Cartas_abreviadas[rd.randint(0,107)]
Cartas_Jugador2[2]=Cartas_abreviadas[rd.randint(0,107)]

#print(Cartas_Jugador1)
#print(Cartas_Jugador2)                         #pasar el establos y mazo al final del codigo en el de fabri

"Establos de unicornios de los jugadores"   
Establo_jugador1=[]
Establo_jugador2=[]

"""Turno de:         [Establo 1]                [Establo 2]
                     [{Establo_jugador1[0]}]      [{Establo_jugador2[0]}]
                     [{Establo_jugador1[1]}]      [{Establo_jugador2[1]}]
                     [{Establo_jugador1[2]}]      [{Establo_jugador2[2]}]
                     [{Establo_jugador1[3]}]      [{Establo_jugador2[3]}]
                     [{Establo_jugador1[4]}]      [{Establo_jugador2[4]}]
                                
                    Mazo jugador 1:             Mazo jugador 2:                   
                    [{Cartas_Jugador1[0]}]        [{Cartas_Jugador2[0]}]
                    [{Cartas_Jugador1[1]}]        [{Cartas_Jugador2[1]}]
                    [{Cartas_Jugador1[2]}]        [{Cartas_Jugador2[2]}]
                    [{Cartas_Jugador1[3]}]        [{Cartas_Jugador2[3]}]
                    [{Cartas_Jugador1[4]}]        [{Cartas_Jugador2[4]}]
                    [{Cartas_Jugador1[5]}]        [{Cartas_Jugador2[5]}]
"""


#os.system("cls") #en linux seria ("clear")

#print(contenido_de_carta(Cartas_Jugador1))
#print (Cartas_Jugador1) 
#print (Cartas)
#print (Lista_de_Cartas)
#print (Cartas_abreviadas)   
#print (descripcion(Sacar_Cartas(Cartas,"Nombre","\n\n")))
#print (organizador(descripcion(Sacar_Cartas(Cartas,"Nombre","\n\n"))))
#print(retornar_contenido_archivo(nombre_archivo))
#print (ventaja("Ventaja",[1,2,3,4]))
#print (magia(Cartas_Jugador1))
#print (desventaja("Desventaja",[1,2,3,4,5]))
#print (pasar_al_establo("Unicornio Bebe",Establo_jugador1))
#print (organizador(Sacar_Cartas(Cartas,"Nombre","\n\n")))

