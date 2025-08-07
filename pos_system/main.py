# Punto de Venta (POS) System

class Producto:
    """Representa un producto con nombre y precio."""
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre}: ${self.precio:.2f}"

class Carrito:
    """Representa el carrito de compras."""
    def __init__(self):
        self.items = []

    def agregar_producto(self, producto):
        """Agrega un producto al carrito."""
        self.items.append(producto)
        print(f"'{producto.nombre}' ha sido añadido al carrito.")

    def calcular_total(self):
        """Calcula el precio total de todos los los productos en el carrito."""
        return sum(producto.precio for producto in self.items)

    def ver_carrito(self):
        """Muestra los productos en el carrito y el total."""
        if not self.items:
            print("El carrito está vacío.")
            return

        print("--- Carrito de Compras ---")
        for producto in self.items:
            print(f"- {producto}")
        print("--------------------------")
        print(f"Total: ${self.calcular_total():.2f}")

def main():
    """Función principal para ejecutar la aplicación de POS."""
    # Inventario de productos
    inventario = [
        Producto("Manzana", 0.5),
        Producto("Pan", 1.5),
        Producto("Leche", 2.0),
        Producto("Cereal", 3.0),
        Producto("Huevo", 0.25)
    ]

    carrito = Carrito()

    while True:
        print("\n--- Bienvenido al Sistema de Punto de Venta ---")
        print("Productos Disponibles:")
        for i, producto in enumerate(inventario):
            print(f"  {i + 1}: {producto}")

        print("\nOpciones:")
        print(" - Escriba el número del producto para añadirlo al carrito.")
        print(" - Escriba 'ver' para mostrar el carrito.")
        print(" - Escriba 'salir' para finalizar la compra.")

        eleccion = input("Su elección: ").lower()

        if eleccion == 'salir':
            break
        elif eleccion == 'ver':
            carrito.ver_carrito()
        elif eleccion.isdigit():
            try:
                indice_producto = int(eleccion) - 1
                if 0 <= indice_producto < len(inventario):
                    producto_elegido = inventario[indice_producto]
                    carrito.agregar_producto(producto_elegido)
                else:
                    print("Error: Número de producto no válido.")
            except ValueError:
                print("Error: Entrada no válida.")
        else:
            print("Error: Opción no reconocida.")

    print("\n--- Resumen Final de la Compra ---")
    carrito.ver_carrito()
    print("¡Gracias por su compra!")


if __name__ == "__main__":
    main()
