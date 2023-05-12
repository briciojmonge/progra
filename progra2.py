#básicamente codigo de la progra
#_______________variable global______________________________________________________________
global archivoori
archivoori=input()


#____________________dale el contenido del archivo como texto________________________________
def retornar_contenido_arch(nombre_archivo):#da los contenidos como un string
    "retorna el texto"
    manejador_arch=open(nombre_archivo, encoding="utf-8")
    contenidos=manejador_arch.read()
    return contenidos
#si sirve por cualquier cosa
#______voy a ver si logro dividir y meterlo en una lista o algo_______________________________
def dividisor(contenidos):
    contenidos=retornar_contenido_arch(archivoori)
    if type(contenidos)!=str:
        return False
    else:
        return divisor(contenidos,0,len(contenidos),"")
def divisor(texto,ind,largo,lista):
    if ind>largo:
        return lista
    if texto[ind]!="\n\n":
        return divisor(texto,ind+1,largo,lista+texto[ind])
    else:
        return divisor(texto,ind+1,largo,lista)
#________________________area de pruebas generales________________________________________________

nombre_archivo=archivoori
#print (retornar_contenido_arch(nombre_archivo))
print(dividisor(nombre_archivo))
"C:\Users\fabri\OneDrive\Escritorio\clases\progra2\newCards.txt"

"""estoy viendo si puedo arreglar esto"""
#si puede fijese si no hay alguna configuracion que me permita correr el codigo, ya que no me deja con su archivo xdxd
"listo"
"escriba algo si ve mi cambio"

"""problema 1: máxima recusividad con ""dividisor"", picha, 
basicamente aumentar el maximo de recursividad tampoco me sirvió, hay que encontrar otra forma o no sé jaja"""