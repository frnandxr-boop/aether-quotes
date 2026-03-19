from models import Material
class InventarioService:
    @classmethod
    def buscar_material(cls, datos_objetos,busqueda):
        material_buscado = []
        encontrado = False
        for material in datos_objetos :
            if material.nombre.lower() == busqueda:
                print(material)
                encontrado = True
                break 
        if not encontrado:
            print(f'{busqueda} no encontrado')
    
    @classmethod
    def agregar_materiales(cls, list_mat, nombre, precio, proveedor, stock):
            mat = Material(nombre,precio,proveedor,stock)
            print(mat)
            list_mat.append(mat)
                
    @classmethod
    def editar_materiales(cls, datos_objetos, mat_buscado, opcion, nuevo_valor):
        encontrado = False
        material_a_editar = None

        # 1. Buscar el material en la lista
        for m in datos_objetos:
            if m.nombre.lower() == mat_buscado.lower():
                material_a_editar = m
                encontrado = True
                break 
        
        if not encontrado:
            print(f'Error: {mat_buscado} no encontrado')
            return False

        # 2. Aplicar el cambio dependiendo de la opción
        if opcion == "stock":
            material_a_editar.stock = nuevo_valor
        elif opcion == "precio":
            material_a_editar.precio = nuevo_valor
        elif opcion == "proveedor":
            material_a_editar.proveedor = nuevo_valor
        elif opcion == "todo":
            # En 'todo', nuevo_valor será una lista o diccionario con los 3 datos
            material_a_editar.stock = nuevo_valor['stock']
            material_a_editar.precio = nuevo_valor['precio']
            material_a_editar.proveedor = nuevo_valor['proveedor']

        print(f"Cambio aplicado con éxito a: {material_a_editar.nombre}")
        return True
            
                
    @classmethod
    def eliminar_materiales(cls,datos_objetos, busqueda):
            encontrado = False
            material_a_eliminar = None
            for material in datos_objetos :
                if material.nombre.lower() == busqueda:
                    print(material)
                    encontrado = True
                    material_a_eliminar = material
                    break
            if encontrado == True :
                datos_objetos.remove(material_a_eliminar)
                print(f"{material_a_eliminar.nombre} eliminado con exito ")
            else:
                print(f"{material_a_eliminar} no encontrada en lista")
    @classmethod
    def estadistica(cls, datos_objetos, total_dinero,max_stock,max_nom,min_stock,min_nom,opcion):
        while True:
            print("Estadísticas del Inventario")        
            for m in datos_objetos:
                try:
                    if opcion.lower()== "total":
                        total_dinero += m.precio * m.stock
                    elif opcion.lower() == "max":
                        if m.stock > max_stock:
                            max_stock = m.stock
                            max_nom = m.nombre
                    elif opcion.lower() == "min":
                        if min_stock == 0 or m.stock < min_stock:
                            min_stock = m.stock
                            min_nom = m.nombre
                    elif opcion.lower() == "salir":
                        break
                except Exception as e:
                    print(f"Error al procesar {m.nombre}: {e}")
            if opcion.lower() == "total":
                print(f"Valor Total en Almacén: ${total_dinero} ")
                break
            if opcion.lower() == "max":
                print(f'el material con el numero en stock mas alto es :{max_nom}, con: {max_stock} en stock')
                break
            if opcion.lower() == "min":
                print(f'el material con el numero en stock mas bajo es :{min_nom}, con: {min_stock} en stock')
                break

