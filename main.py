from models import Material
from collections import defaultdict
import json
#trata de:
try: 
    #Ver y/o leer el archivo existente antes de agregar mas datos y en caso de estar vacio o no existir se creara uno vacio
    with open ('inventario.json' , 'r') as mat:
        datos_guardados=json.load(mat)
except FileNotFoundError:
    datos_guardados=[]

#Nuestra lista vacia 
list_mat = []
#Se inicia un bucle while para que se puedan agregar mas datos a nuestra lista
while True:
    try:
        #se le pregunta al usuario el nombre del material 
        nombre = str(input('Escribe el nombre del material: '))
        #se pregunta el costo 
        precio = float(input(f"Ingresa el precio del {nombre}: "))
        #provedor
        provedor = str(input('Nombre del proveedor: '))
        #se define mat, es la que junta todo (clase,objeto,atributos)
        stock = int(input(f'Ingresa la cantidad de {nombre} en stock: '))
        mat = Material(nombre,precio,provedor,stock)
        print(mat)
        list_mat.append(mat)
        #Se pregunta si desea continuar o salir 
        respuesta= input("¿Deseas agregar un nuevo material o salir? ")
        #si la respuesta es 'salir' entonces el bucle acaba 
        if respuesta.lower() == 'salir':  
            break
    #si un dato esta mal, salta error y se apoda 'e' asi sabemos exactamente cual fue el error
    except ValueError as e:
        print(f'error {e} ')
#se crea el diccionario recorriendo la lista con todos sus datos 
#__dict__ se utiliza para 'transformar' los datos de la lista en texto que el json pueda leer
dic_mat_list= [material.__dict__ for material in list_mat]
#-----Creacion de .JSON----
#Se define una lista a la cual se agregaran los nuevos datos
lista_final= datos_guardados + dic_mat_list
#se abre el archivo .JSON y se escriben los nuevos materiales agregando los que ya estaban anteriormente
with open ('inventario.json', 'w') as mat:
   json.dump(lista_final, mat, indent=2)
