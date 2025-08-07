-- Eliminar la tabla si ya existe para evitar errores en ejecuciones repetidas
DROP TABLE IF EXISTS products;

-- Crear la tabla de productos
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    stock INTEGER NOT NULL DEFAULT 0,
    barcode TEXT UNIQUE
);
