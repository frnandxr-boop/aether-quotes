from models import Material
import json
 
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
        if  accion.lower() == 'buscar material':
            print("Buscador")
            material_buscado = []
            encontrado = False
            busqueda=input("¿Que material buscas?")
            for material in datos_objetos :
                if material.nombre.lower() == busqueda:
                    print(material)
                    encontrado = True
                    break 
            if not encontrado:
                print(f'{busqueda} no encontrado')
        elif accion.lower()  == 'agregar material':
            #se le pregunta al usuario el nombre del material 
            nombre = str(input('Escribe el nombre del material: '))
            #se pregunta el costo 
            precio = float(input(f"Ingresa el precio de {nombre}: "))
            #provedor
            proveedor = str(input('Nombre del proveedor: '))
            #se define mat, es la que junta todo (clase,objeto,atributos)
            stock = int(input(f'Ingresa la cantidad de {nombre} en stock: '))
            mat = Material(nombre,precio,proveedor,stock)
            print(mat)
            list_mat.append(mat)
            
        #Para editar los materiales en el json ("editar material")  
        elif accion.lower()  == 'editar material':
            nvo_precio =[]
            nvo_stock=[]
            nvo_proveedor=[]
            todo=[]
            material_a_editar= input("Escribe el material a editar: ")
            
            material_edit=next((m for m in datos_objetos if m.nombre == material_a_editar), None)
            edit=input("¿Que deseas editar(stock,proveedor,precio,todo)? ")
            #funciones para todas los posibles cambios/ediciones
            def editar_stock(material):
                    nvo_stock = int(input(f"Ingresa la cantidad en stock de {material.nombre}: "))
                    material_edit.stock = nvo_stock
                    print(f'stock actualizado con exito: {material.nombre} -- {material.stock}')
                    
            def editar_precio(material):    
                    nvo_precio = float(input(f"Ingresa el nuevo precio de {material.nombre}: "))
                    material_edit.precio= nvo_precio
                    print(f'Precio actualizado con exito: {material.nombre} -- {material.precio}')
                    
            def editar_proveedor(material):       
                    nvo_proveedor = str(input(f'ingresa el nuevo proveedor de {material.nombre}: '))
                    material_edit.proveedor = nvo_proveedor
                    print(f'Provedor actualizado con exito: {material.nombre} -- {material.proveedor}')
            #Se crea una funcion que englobe todo 
            def editar_todo(material):
                    editar_stock(material_edit)
                    editar_precio(material_edit)
                    editar_proveedor(material_edit)
                    print(f"{material.nombre} editado con exito : {material.nombre}-- {material.precio}--{material.proveedor}--{material.stock}")
            #Se llaman y activan las funciones 
            if edit.lower() == 'stock':
                editar_stock(material_edit)
            elif edit.lower() == 'precio':
                editar_precio(material_edit)
            elif edit.lower() == 'proveedor':
                editar_proveedor(material_edit)
            elif edit.lower() == 'todo':
                editar_todo(material_edit)
            #Aqui terminan las acciones y se pregunta si quiere salir o realizar una nueva accion
            
        elif accion.lower() == "salir":
            break
    #si un dato esta mal, salta error y se apoda 'e' asi sabemos exactamente cual fue el error
    except ValueError as e:
        print(f'error {e} ')
#se crea el diccionario recorriendo la lista con todos sus datos 
#__dict__ se utiliza para 'transformar' los datos de la lista en texto que el json pueda leer
####dic_mat_list= [material.to_dict() for material in datos_objetos + list_mat]###
datos_g=[material.to_dict() for material in datos_objetos + list_mat]
#-----Creacion de .JSON----
#Se define una lista a la cual se agregaran los nuevos datos
###lista_final= datos_guardados + dic_mat_list##
#se abre el archivo .JSON y se escriben los nuevos materiales agregando los que ya estaban anteriormente
with open ('inventario.json', 'w') as mat:
   json.dump(datos_g, mat, indent=2)
lista_mat_final =[]