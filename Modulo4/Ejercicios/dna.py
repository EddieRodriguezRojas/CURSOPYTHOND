# Importando librerias
import csv
import re

#Declarando funciones
def conteomaxstr(patron, texto):
    maxrep = 0
    count = 0
    fin = 0
    
    while True:
        encontrado = re.search(patron, texto)
        if encontrado:
            inicio = encontrado.start()
            end = encontrado.end()
            if fin == 0:
                count = 1
                fin = end
                texto = texto.replace(patron, patron.lower(), 1) #hacer un replace del patron para que no vuelva a ser encontrado en la siguiente iteración
            else:
                if inicio == fin:
                    texto = texto.replace(patron, patron.lower(), 1) #hacer un replace del patron para que no vuelva a ser encontrado en la siguiente iteración
                    count = count + 1
                    fin = end
                else:
                    #Se reinicia el conteo para los patrones restantes
                    fin = 0
                    if count > maxrep:
                        maxrep = count
                    count = 0
        else:
            if count > maxrep:
                maxrep = count
            break
    
    return maxrep

def busqueda_dna():
    nombre = "No match"
    
    try:
        #Se pide el nombre del archivo de .csv
        csvname = input("Introduce el nombre del archivo CSV que contiene los recuentos de STR para la lista de individuos:")
        #Se abre el archivo .csv y se guarda en una colección de datos similar a un diccionario gracias al método csv.DictReader
        with open('./data/dna/databases/' + csvname, newline='') as csvfile:
            try:
                #Se pide el nombre del archivo de .txt
                txtname = input("Introduce el nombre del archivo de texto que contiene la secuencia ADN a indentificar:")
                #Se abre el archivo de texto que contiene el ADN del individuo y se guarda el texto en un string ADN
                with open('./data/dna/sequences/' + txtname, mode = 'r') as txtfile:
                    ADN = txtfile.read()
                    for fila in csv.DictReader(csvfile):
                        cadena = ADN
                        if nombre == "No match":
                            for patron in fila:
                                if patron != 'name':
                                    if int(fila[patron]) == int(conteomaxstr(patron, cadena)):
                                        nombre = fila['name']
                                    else:
                                        nombre = "No match"
                                        break
                        else:
                            break
                print(nombre)
            except:
                print(f"El archivo {txtname} no existe")
    except:
        print(f"El archivo {csvname} no existe")

busqueda_dna()
