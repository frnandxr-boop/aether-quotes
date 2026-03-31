import sqlite3
import json

def migrar_datos():
    # 1. Cargar los datos del JSON antiguo
    try:
        with open('inventario.json', 'r') as f:
            materiales_json = json.load(f)
    except FileNotFoundError:
        print("No se encontró el archivo JSON para migrar.")
        return

    # 2. Conectar a la Base de Datos
    conexion = sqlite3.connect('aether_inventario.db')
    cursor = conexion.cursor()

    # 3. Insertar cada material
    for m in materiales_json:
        # Preparamos la orden con '?' por seguridad
        query = "INSERT INTO materiales (nombre, precio, proveedor, stock) VALUES (?, ?, ?, ?)"
        
        # Extraemos los valores del diccionario
        valores = (m['nombre'], m['precio'], m['proveedor'], m['stock'])
        
        cursor.execute(query, valores)

    # 4. GUARDAR CAMBIOS (Muy importante)
    conexion.commit()
    
    # 5. Verificar cuántos se movieron
    print(f"Éxito: Se migraron {len(materiales_json)} materiales a SQL.")
    
    conexion.close()

if __name__ == "__main__":
    migrar_datos()