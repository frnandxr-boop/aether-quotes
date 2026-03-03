from models import Material
from collections import defaultdict
import json

try: 
    with open ('inventario.json' , 'r') as mat:
        datos_guardados=json.load(mat)
except FileNotFoundError:
    datos_guardados=[]

#Nuestra lista vacia 
list_mat = []
#Se inicia un bucle while para que se puedan agregar mas datos a nuestra lista
while True:
    try:
        nombre = str(input('Escribe el nombre del material: '))
        #se pregunta el costo 
        precio = float(input("Ingresa el precio del material: "))
        #provedor
        provedor = str(input('Nombre del proveedor: '))
        #se define mat, es la que junta todo (clase,objeto,atributos)
        stock = int(input(f'Ingresa la cantidad del {nombre} en stock: '))
        mat = Material(nombre,precio,provedor,stock)
        print(mat)
        list_mat.append(mat)
        #Se pregunta si desea continuar o salir 
        respuesta= input("¿Deseas agregar un nuevo material o salir? ")
        #si la respuesta es 'salir' entonces el bucle acaba 
        if respuesta.lower() == 'salir':  
            break
    except ValueError as e:
        print(f'error {e} ')
#se crea el diccionario recorriendo la lista con todos sus datos 
#__dict__ se utiliza para 'transformar' los datos de la lista en texto que el json pueda leer
dic_mat_list= [material.__dict__ for material in list_mat]
#Creacion de .JSON
lista_final= datos_guardados + dic_mat_list
with open ('inventario.json', 'w') as mat:
   json.dump(lista_final, mat, indent=2)
