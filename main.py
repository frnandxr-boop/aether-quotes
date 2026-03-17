from models import Material
import json
from services import InventarioService
 
#trata de:
try: 
    #Ver y/o leer el archivo existente antes de agregar mas datos y en caso de estar vacio o no existir se creara uno vacio
    with open ('inventario.json' , 'r') as mat:
        datos_guardados=json.load(mat)
except FileNotFoundError:
    datos_guardados=[]

datos_objetos = [Material.from_inventario(d) for d in datos_guardados]
total_dinero = 0
total_truper = 0
for m in datos_objetos:
    total_dinero += m.precio * m.stock
    if m.proveedor.lower() == 'truper':
        total_truper += m.precio * m.stock
print(f"--- Sistema Iniciado: Valor Total en Almacén: ${total_dinero} , valor de truper : ${total_truper} ---")
#Nuestra lista vacia 
list_mat = []
#Se inicia un bucle while para que se puedan agregar mas datos a nuestra lista
while True:
    
    try:
        #Se le muestra al usuario las acciones que puede realizar
        print("Acciones : Agregar material | Editar valores | Eliminar material | Buscar Material | Salir ")
        #Se crea la variable 'accion' para guardar la respuesta del usuario
        accion = input("¿Que accion deseas realizar?: ")
        #Para buscar un material la respues guardada en "accion" debe ser "buscar material"
        if accion.lower() == 'buscar material':
            print("Buscador")
            busqueda=input("¿Que material buscas?")
            InventarioService.buscar_material(datos_objetos, busqueda)
            
            
        elif accion.lower()  == 'agregar material':
            print("Agregar Materiales")
            #se le pregunta al usuario el nombre del material 
            nombre = str(input('Escribe el nombre del material: '))
            #se pregunta el costo 
            precio = float(input(f"Ingresa el precio de {nombre}: "))
            #provedor
            proveedor = str(input('Nombre del proveedor: '))
            #se define mat, es la que junta todo (clase,objeto,atributos)
            stock = int(input(f'Ingresa la cantidad de {nombre} en stock: '))
            InventarioService.agregar_materiales(datos_objetos, nombre, precio, proveedor, stock)
            
        elif accion.lower()  == 'editar material':
            buscado = input("¿Qué material buscas para editar?: ")
            
            # Primero verificamos si existe antes de preguntar qué editar
            print("Editor de Materiales")
            opcion = input("¿Qué deseas editar (stock, proveedor, precio, todo)?: ").lower()

            if opcion == "stock":
                valor = int(input(f"Ingresa el nuevo stock: "))
                InventarioService.editar_materiales(datos_objetos, buscado, opcion, valor)
            
            elif opcion == "precio":
                valor = float(input(f"Ingresa el nuevo precio: "))
                InventarioService.editar_materiales(datos_objetos, buscado, opcion, valor)
            
            elif opcion == "proveedor":
                valor = input(f"Ingresa el nuevo proveedor: ")
                InventarioService.editar_materiales(datos_objetos, buscado, opcion, valor)
                
            elif opcion == "todo":
                # Creamos un pequeño paquete con los 3 datos
                valores_todo = {
                    'stock': int(input("Nuevo stock: ")),
                    'precio': float(input("Nuevo precio: ")),
                    'proveedor': input("Nuevo proveedor: ")
                }
                InventarioService.editar_materiales(datos_objetos, buscado, opcion, valores_todo)
        
        elif accion.lower() == "eliminar material" :
            print("Eliminar Materiales")
            busqueda=input("¿Que material quieres eliminar?")
            InventarioService.eliminar_materiales(datos_objetos, busqueda)
        
        elif accion.lower() == "salir":
            break
    #si un dato esta mal, salta error y se apoda 'e' asi sabemos exactamente cual fue el error
    except ValueError as e:
        print(f'error {e} ')
#se crea el diccionario recorriendo la lista con todos sus datos 
datos_g=[m.to_dict() for m in datos_objetos]
#-----Creacion de .JSON----
#Se define una lista a la cual se agregaran los nuevos datos
#se abre el archivo .JSON y se escriben los nuevos materiales agregando los que ya estaban anteriormente
with open ('inventario.json', 'w') as mat:
   json.dump(datos_g, mat, indent=2)
lista_mat_final =[]