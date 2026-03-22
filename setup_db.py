import sqlite3

# 1. Conectar (Crea el archivo si no existe)
conexion = sqlite3.connect('aether_inventario.db')

# 2. Crear el cursor (El ejecutor de órdenes)
cursor = conexion.cursor()

# 3. Definir la orden para crear la tabla
tabla_materiales = """
CREATE TABLE IF NOT EXISTS materiales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL,
    proveedor TEXT,
    stock INTEGER DEFAULT 0
)
"""

# 4. Ejecutar y Guardar
cursor.execute(tabla_materiales)
conexion.commit()

# 5. Cerrar conexión
conexion.close()

print("Base de datos y tabla creadas con éxito.")