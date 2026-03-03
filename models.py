#Creamos la clase llamada "Material"
class Material :
    #se llama al "contructor" (__init__) con el objetio (self) y los atributos  con las condiciones (str para texto y float para numeros)
    def __init__(self, nombre : str, precio: float , provedor : str , stock :int ):
        self.nombre = self.validacion_nombre(nombre)
        self.precio = self.validacion_precio(precio)
        self.provedor = self.validacion_prov(provedor)
        self.stock = self.validacion_stock(stock)
    def validacion_nombre(self, nombre):
        if not isinstance (nombre , str) or not nombre.strip():
            raise ValueError("Ingresa un nombre correcto")
        return (nombre)
    def validacion_precio(self, precio):
        if not isinstance(precio, (float, int) ) or (precio) < 0:
            raise ValueError ("Ingresa un numero entero valido")
        return (precio)
    def validacion_prov(self, provedor):
        if not isinstance(provedor, str) or not provedor.strip():
            raise ValueError("Ingresa un nombre de provedor valido")
        return(provedor)
    def validacion_stock(self, stock):
        if not isinstance(stock, (int, float) ) or (stock) < 0:
            raise ValueError ("Ingresa un numero de stock valido")
        return (stock)
    #Una fucnion para que se repita con todos los materiales y se imprima el objeto definido y sus atributos
    def __str__(self):
        return f'Material:{self.nombre}| Precio:${self.precio}| Provedor :{self.provedor}'


