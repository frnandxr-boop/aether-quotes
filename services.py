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
    def editar_materiales(cls, datos_objetos, material_a_editar, edit):
            nvo_precio =[]
            nvo_stock=[]
            nvo_proveedor=[]
            todo=[]
            material_edit=next((m for m in datos_objetos if m.nombre == material_a_editar), None)
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
                
    @classmethod
    def eliminar_materiales(cls,datos_objetos, busqueda):
            material_a_eliminar.buscar_material(busqueda)
            for material in datos_objetos :
                if material.nombre.lower() == busqueda:
                    print(material)
                    encontrado = True
                    material_a_eliminar = material
                    break
            if encontrado == True :
                datos_objetos.remove(material_a_eliminar)
                print(f"{material_a_eliminar} eliminado con exito ")
            else:
                print(f"{material_a_eliminar} no encontrada en lista")
    
