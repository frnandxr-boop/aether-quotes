#Creamos la clase llamada "Material"
class Material :
    #se llama al "contructor" (__init__) con el objetio (self) y los atributos  con las condiciones (str para texto y float para numeros)
    def __init__(self, nombre : str, precio: float , provedor : str , stock :int ):
        self.nombre = self.validacion_nombre(nombre)
        self.precio = self.validacion_precio(precio)
        self.provedor = self.validacion_prov(provedor)
        self.stock = self.validacion_stock(stock)
    def validacion_nombre(self, nombre):
        if not isinstance (nombre , str):
            raise ValueError("Ingresa un nombre correcto")
        return (material)
    def validacion_precio(self, precio):
        if not isinstance(precio, float ) or (precio) < 0:
            raise ValueError ("Ingresa un numero entero valido")
        return (costo)
    def validacion_prov(self, provedor):
        if not isinstance(provedor, str):
            raise ValueError("Ingresa un nombre de provedor valido")
        return(prov)
    def validacion_stock(self, stock):
        if not isinstance(stock, int ) or (stock) < 0:
            raise ValueError ("Ingresa un numero de stock valido")
        return (stk)
    #Una fucnion para que se repita con todos los materiales y se imprima el objeto definido y sus atributos
    def __str__(self):
        return f'Material:{self.nombre}| Precio:${self.precio}| Provedor :{self.provedor}'
list_mat = []
while True:
    try:
        material = str(input('Escribe el nombre del material: '))
        #se pregunta el costo 
        costo = float(input("Ingresa el precio del material: "))
        #provedor
        prov = str(input('Nombre del proveedor: '))
        #se define mat, es la que junta todo (clase,objeto,atributos)
        stk = int(input(f'Ingresa la cantidad del {material} en stock: '))
        mat = Material(material, costo, stk, prov)
        print(mat)
        list_mat.append(mat)
        print("lista actualizadac exitosamente:",list_mat)
        respuesta= input("¿Deseas agregar un nuevo material o salir?")
        if respuesta.lower() == 'salir':  
            break
    except ValueError:
        print("Ingresa los datos correctamente")


